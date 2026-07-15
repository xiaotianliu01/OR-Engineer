#!/usr/bin/env python3
"""Probe supplied data files before OR formulation.

The script uses the Python standard library where possible and reports JSON to
stdout. It is intentionally conservative: when it cannot load a file, it reports
the error instead of guessing contents from the filename.

Creator and maintainer: Xiaotian Liu <xiaotianliu01@gmail.com>
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sqlite3
import struct
import sys
import wave
import zipfile
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET


TABLE_EXTS = {".csv", ".tsv", ".txt"}
JSON_EXTS = {".json", ".jsonl", ".ndjson"}
EXCEL_EXTS = {".xlsx"}
DOC_EXTS = {".docx"}
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".bmp"}
VIDEO_EXTS = {".mp4", ".mov", ".avi", ".mkv", ".webm"}
AUDIO_EXTS = {".wav", ".mp3", ".flac", ".m4a", ".ogg"}
GRAPH_EXTS = {".edgelist", ".edges", ".mtx", ".graphml", ".gexf"}
ARRAY_EXTS = {".npy", ".npz"}
SQLITE_EXTS = {".sqlite", ".sqlite3", ".db"}


def text_preview(path: Path, limit: int) -> str:
    with path.open("r", encoding="utf-8", errors="replace") as handle:
        return handle.read(limit)


def probe_csv(path: Path, max_rows: int) -> dict[str, Any]:
    sample_text = text_preview(path, 8192)
    try:
        dialect = csv.Sniffer().sniff(sample_text)
    except csv.Error:
        dialect = csv.excel_tab if path.suffix.lower() == ".tsv" else csv.excel

    rows: list[list[str]] = []
    with path.open("r", encoding="utf-8", errors="replace", newline="") as handle:
        reader = csv.reader(handle, dialect)
        for i, row in enumerate(reader):
            if i >= max_rows:
                break
            rows.append(row)

    header = rows[0] if rows else []
    lower_header = {col.strip().lower() for col in header}
    network_like = bool(
        {"source", "target"} <= lower_header
        or {"from", "to"} <= lower_header
        or {"u", "v"} <= lower_header
        or {"node1", "node2"} <= lower_header
    )
    return {
        "loaded": True,
        "kind": "table",
        "delimiter": getattr(dialect, "delimiter", None),
        "columns": header,
        "sample_rows": rows[1:] if header else rows,
        "semantic_hint": "network_edges" if network_like else "structured_table",
    }


def probe_json(path: Path, max_rows: int, max_bytes: int) -> dict[str, Any]:
    if path.suffix.lower() in {".jsonl", ".ndjson"}:
        records: list[Any] = []
        with path.open("r", encoding="utf-8", errors="replace") as handle:
            for i, line in enumerate(handle):
                if i >= max_rows:
                    break
                line = line.strip()
                if line:
                    records.append(json.loads(line))
        return {
            "loaded": True,
            "kind": "json_records",
            "sample_count": len(records),
            "sample": records,
        }

    if path.stat().st_size > max_bytes:
        return {
            "loaded": False,
            "kind": "json",
            "error": f"file exceeds max_bytes={max_bytes}",
        }

    data = json.loads(path.read_text(encoding="utf-8"))
    summary: dict[str, Any] = {"loaded": True, "kind": "json", "top_level_type": type(data).__name__}
    if isinstance(data, dict):
        summary["keys"] = list(data.keys())[:50]
    elif isinstance(data, list):
        summary["length"] = len(data)
        summary["sample"] = data[:max_rows]
    return summary


def probe_docx(path: Path, max_chars: int) -> dict[str, Any]:
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    with zipfile.ZipFile(path) as zf:
        xml = zf.read("word/document.xml")
    root = ET.fromstring(xml)
    paragraphs: list[str] = []
    for para in root.findall(".//w:p", ns):
        parts: list[str] = []
        for node in para.iter():
            tag = node.tag.rsplit("}", 1)[-1]
            if tag == "t" and node.text:
                parts.append(node.text)
            elif tag == "tab":
                parts.append("\t")
            elif tag == "br":
                parts.append("\n")
        text = "".join(parts).strip()
        if text:
            paragraphs.append(text)
    return {
        "loaded": True,
        "kind": "document_text",
        "paragraph_count": len(paragraphs),
        "text_preview": "\n".join(paragraphs)[:max_chars],
    }


def xlsx_shared_strings(zf: zipfile.ZipFile) -> list[str]:
    try:
        root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
    except KeyError:
        return []
    values: list[str] = []
    for si in root:
        texts = [node.text or "" for node in si.iter() if node.tag.endswith("}t")]
        values.append("".join(texts))
    return values


def probe_xlsx(path: Path, max_rows: int) -> dict[str, Any]:
    ns = {
        "main": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
        "rel": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    }
    with zipfile.ZipFile(path) as zf:
        workbook = ET.fromstring(zf.read("xl/workbook.xml"))
        shared = xlsx_shared_strings(zf)
        sheets = []
        for sheet in workbook.findall(".//main:sheet", ns):
            sheets.append(
                {
                    "name": sheet.attrib.get("name"),
                    "sheetId": sheet.attrib.get("sheetId"),
                    "relationship": sheet.attrib.get(f"{{{ns['rel']}}}id"),
                }
            )
        worksheet_names = sorted(name for name in zf.namelist() if name.startswith("xl/worksheets/sheet"))
        worksheet_summaries = []
        for sheet_path in worksheet_names[:10]:
            root = ET.fromstring(zf.read(sheet_path))
            dimension = root.find(".//main:dimension", ns)
            rows_out: list[list[str]] = []
            for row in root.findall(".//main:sheetData/main:row", ns)[:max_rows]:
                row_values: list[str] = []
                for cell in row.findall("main:c", ns):
                    cell_type = cell.attrib.get("t")
                    value_node = cell.find("main:v", ns)
                    value = value_node.text if value_node is not None else ""
                    if cell_type == "s" and value.isdigit():
                        idx = int(value)
                        value = shared[idx] if idx < len(shared) else value
                    row_values.append(value)
                rows_out.append(row_values)
            worksheet_summaries.append(
                {
                    "path": sheet_path,
                    "dimension": dimension.attrib.get("ref") if dimension is not None else None,
                    "sample_rows": rows_out,
                }
            )
    return {
        "loaded": True,
        "kind": "workbook",
        "sheets": sheets,
        "worksheets": worksheet_summaries,
    }


def probe_sqlite(path: Path) -> dict[str, Any]:
    conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    try:
        rows = conn.execute("select name, type from sqlite_master where type in ('table','view')").fetchall()
        tables = []
        for name, obj_type in rows:
            cols = conn.execute(f"pragma table_info({quote_identifier(name)})").fetchall()
            tables.append(
                {
                    "name": name,
                    "type": obj_type,
                    "columns": [{"name": col[1], "type": col[2]} for col in cols],
                }
            )
        return {"loaded": True, "kind": "sqlite", "tables": tables}
    finally:
        conn.close()


def quote_identifier(value: str) -> str:
    return '"' + value.replace('"', '""') + '"'


def png_size(path: Path) -> tuple[int, int] | None:
    with path.open("rb") as handle:
        sig = handle.read(24)
    if sig.startswith(b"\x89PNG\r\n\x1a\n") and len(sig) >= 24:
        return struct.unpack(">II", sig[16:24])
    return None


def gif_size(path: Path) -> tuple[int, int] | None:
    with path.open("rb") as handle:
        sig = handle.read(10)
    if sig[:6] in {b"GIF87a", b"GIF89a"}:
        return struct.unpack("<HH", sig[6:10])
    return None


def bmp_size(path: Path) -> tuple[int, int] | None:
    with path.open("rb") as handle:
        sig = handle.read(26)
    if sig.startswith(b"BM") and len(sig) >= 26:
        return struct.unpack("<ii", sig[18:26])
    return None


def jpeg_size(path: Path) -> tuple[int, int] | None:
    with path.open("rb") as handle:
        if handle.read(2) != b"\xff\xd8":
            return None
        while True:
            marker_start = handle.read(1)
            if not marker_start:
                return None
            if marker_start != b"\xff":
                continue
            marker = handle.read(1)
            while marker == b"\xff":
                marker = handle.read(1)
            if marker in {b"\xc0", b"\xc1", b"\xc2", b"\xc3", b"\xc5", b"\xc6", b"\xc7", b"\xc9", b"\xca", b"\xcb", b"\xcd", b"\xce", b"\xcf"}:
                length = struct.unpack(">H", handle.read(2))[0]
                data = handle.read(length - 2)
                if len(data) >= 5:
                    height, width = struct.unpack(">HH", data[1:5])
                    return width, height
                return None
            length_bytes = handle.read(2)
            if len(length_bytes) != 2:
                return None
            length = struct.unpack(">H", length_bytes)[0]
            handle.seek(length - 2, os.SEEK_CUR)


def probe_image(path: Path) -> dict[str, Any]:
    suffix = path.suffix.lower()
    size = None
    if suffix == ".png":
        size = png_size(path)
    elif suffix in {".jpg", ".jpeg"}:
        size = jpeg_size(path)
    elif suffix == ".gif":
        size = gif_size(path)
    elif suffix == ".bmp":
        size = bmp_size(path)
    return {
        "loaded": size is not None,
        "kind": "image",
        "width": size[0] if size else None,
        "height": size[1] if size else None,
        "modeling_role": "high_dimensional_feature_input",
    }


def probe_audio(path: Path) -> dict[str, Any]:
    if path.suffix.lower() == ".wav":
        with wave.open(str(path), "rb") as handle:
            return {
                "loaded": True,
                "kind": "audio",
                "channels": handle.getnchannels(),
                "sample_width": handle.getsampwidth(),
                "frame_rate": handle.getframerate(),
                "frames": handle.getnframes(),
                "modeling_role": "high_dimensional_feature_input",
            }
    return {
        "loaded": False,
        "kind": "audio",
        "error": "metadata-only unsupported audio format without optional dependencies",
        "modeling_role": "high_dimensional_feature_input",
    }


def probe_np(path: Path) -> dict[str, Any]:
    if path.suffix.lower() == ".npz":
        with zipfile.ZipFile(path) as zf:
            return {"loaded": True, "kind": "numpy_archive", "members": zf.namelist()}
    with path.open("rb") as handle:
        magic = handle.read(6)
        if magic != b"\x93NUMPY":
            return {"loaded": False, "kind": "numpy_array", "error": "missing numpy magic header"}
        version = tuple(handle.read(2))
        header_len_size = 2 if version == (1, 0) else 4
        header_len = int.from_bytes(handle.read(header_len_size), "little")
        header = handle.read(header_len).decode("latin1", errors="replace")
    return {"loaded": True, "kind": "numpy_array", "version": version, "header": header}


def probe_file(path: Path, max_rows: int, max_bytes: int, max_chars: int) -> dict[str, Any]:
    suffix = path.suffix.lower()
    result: dict[str, Any] = {
        "path": str(path),
        "name": path.name,
        "extension": suffix,
        "size_bytes": path.stat().st_size,
    }
    try:
        if suffix in TABLE_EXTS:
            result.update(probe_csv(path, max_rows))
        elif suffix in JSON_EXTS:
            result.update(probe_json(path, max_rows, max_bytes))
        elif suffix in DOC_EXTS:
            result.update(probe_docx(path, max_chars))
        elif suffix in EXCEL_EXTS:
            result.update(probe_xlsx(path, max_rows))
        elif suffix in SQLITE_EXTS:
            result.update(probe_sqlite(path))
        elif suffix in IMAGE_EXTS:
            result.update(probe_image(path))
        elif suffix in AUDIO_EXTS:
            result.update(probe_audio(path))
        elif suffix in VIDEO_EXTS:
            result.update(
                {
                    "loaded": False,
                    "kind": "video",
                    "error": "metadata-only video format without optional dependencies",
                    "modeling_role": "high_dimensional_feature_input",
                }
            )
        elif suffix in GRAPH_EXTS:
            result.update(
                {
                    "loaded": True,
                    "kind": "graph_or_network_file",
                    "text_preview": text_preview(path, max_chars),
                    "modeling_role": "special_format_structured_input",
                }
            )
        elif suffix in ARRAY_EXTS:
            result.update(probe_np(path))
        else:
            result.update(
                {
                    "loaded": False,
                    "kind": "unknown",
                    "error": "unsupported extension; inspect manually or add a loader",
                }
            )
    except Exception as exc:  # Report load failures instead of guessing.
        result.update({"loaded": False, "error": f"{exc.__class__.__name__}: {exc}"})
    return result


def iter_files(paths: list[Path], recursive: bool, max_files: int) -> list[Path]:
    found: list[Path] = []
    for path in paths:
        if path.is_file():
            found.append(path)
        elif path.is_dir():
            iterator = path.rglob("*") if recursive else path.glob("*")
            for candidate in iterator:
                if candidate.is_file():
                    found.append(candidate)
                    if len(found) >= max_files:
                        return found
        if len(found) >= max_files:
            return found
    return found


def summarize_roles(files: list[dict[str, Any]]) -> dict[str, int]:
    counts = {
        "structured_model_input": 0,
        "special_format_structured_input": 0,
        "high_dimensional_feature_input": 0,
        "unusable_or_blocked_input": 0,
    }
    for item in files:
        role = item.get("modeling_role")
        if not role:
            if item.get("loaded") and item.get("kind") in {"table", "json", "json_records", "workbook", "sqlite", "document_text", "numpy_array", "numpy_archive"}:
                role = "structured_model_input"
            elif item.get("loaded") and item.get("kind") == "graph_or_network_file":
                role = "special_format_structured_input"
            elif item.get("kind") in {"image", "video", "audio"}:
                role = "high_dimensional_feature_input"
            else:
                role = "unusable_or_blocked_input"
        counts[role] = counts.get(role, 0) + 1
        item["modeling_role"] = role
    return counts


def main() -> int:
    parser = argparse.ArgumentParser(description="Probe data files for OR formulation.")
    parser.add_argument("paths", nargs="+", help="Files or directories to inspect.")
    parser.add_argument("--recursive", action="store_true", help="Recursively scan directories.")
    parser.add_argument("--max-files", type=int, default=200)
    parser.add_argument("--max-rows", type=int, default=5)
    parser.add_argument("--max-bytes", type=int, default=5_000_000)
    parser.add_argument("--max-chars", type=int, default=4000)
    args = parser.parse_args()

    input_paths = [Path(p).expanduser().resolve() for p in args.paths]
    files = iter_files(input_paths, args.recursive, args.max_files)
    probed = [probe_file(path, args.max_rows, args.max_bytes, args.max_chars) for path in files]
    role_counts = summarize_roles(probed)
    report = {
        "input_paths": [str(path) for path in input_paths],
        "file_count": len(probed),
        "role_counts": role_counts,
        "files": probed,
    }
    json.dump(report, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
