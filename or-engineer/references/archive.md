# Archive

Creator and maintainer: Xiaotian Liu · xiaotianliu01@gmail.com

## Mission

Create a reproducible final project folder and a transfer-ready final technical document after the user asks for final documentation or accepts the completed development.

## Required Contents

Place these artifacts together:

- Final Python source code
- Input data or documented data references
- Output result files
- Run metadata for jobs expected to exceed 3 minutes: reduced test output, runtime estimate, user-facing `run` command, terminal progress expectations, structured progress/status/result files, checkpoint paths, artifact manifest, and actual runtime
- Process-metric logs for code runs, especially cost/objective/reward over time, evaluation cost, feasibility violations, repair/projection magnitude, loss/gap/solver diagnostics, elapsed time, and current best value where available
- Training convergence logs, curves, seed-level summaries, and convergence status files for learned or training-based methods
- Tuning and model-size records for learned or numerical methods, including tried configurations, selected configuration, tuning budget, and rationale
- Acceptance-criteria records: strong baseline outputs, desired improvement or optimality-gap target, pilot evidence, pass/fail status, and redesign decisions after weak pilots
- Baseline-by-baseline records: every comparator's definition, data/features used, tuning or fixed settings, implementability or hindsight status, runtime status, and metric results. Do not archive only an aggregate comparator result.
- Performance-ceiling versus implementation-effort record from method selection, including rejected or deferred high-ceiling methods and the evidence behind those decisions
- Finalized stage reports: formulation confirmation, method selection, deployment confirmation, Project Delivery And Run Manual, and final results analysis when produced
- Trajectory-level benchmark files, including ex-post optimal or valid lower-bound costs when computed
- Default rendered PDF technical report explaining the finalized data, model, method, deployment project, results from the user's `run`, benchmark gaps, limitations, and reproducibility steps
- Static HTML or Markdown review copy of the technical report when useful for iteration or reproducibility
- Output-file dictionary or manifest explaining the main generated files, their contents, key fields, units, update frequency, and how operators should inspect them
- Optional Word `.docx` export only when explicitly requested or useful for archival delivery
- `requirements.txt`
- Any configuration files required to rerun
- Creator attribution in the final PDF/HTML/Markdown report and archive-level manifest: Xiaotian Liu <xiaotianliu01@gmail.com>.

## Final Technical Document

The final report must be a substantive, polished technical document, not only a cost/result summary. Default to a rendered PDF unless the user requests another format. Keep an HTML or Markdown review copy when useful for review, reproducibility, or later edits. The document should be written for expert OR and operations reviewers who have not followed the conversation and need to evaluate the model, assumptions, method, deployment project, results, and implementation implications.

Include the compact creator attribution required by references/response_style.md in the report metadata or footer. Include the same name and email once in the archive-level artifact manifest; do not duplicate it across run logs or user data.

Write the final PDF text, optional HTML/Markdown copy, Word export text if requested, output-file dictionary explanations, and rerun instructions in the user's target language as defined in `references/response_style.md`. Preserve English technical terms and code-facing identifiers when translation would reduce precision or break reproducibility.

Synthesize all finalized materials rather than rewriting from memory: the final formulation report, method-selection report, deployment confirmation report, Project Delivery And Run Manual, final code/project state, logs and results from the user's `run`, benchmark files, and any final result analyses.

Include:

- Problem statement
- Data description, including sources, loaded files, observed schemas or fields, dimensions, preprocessing, generated data assumptions, and which data are used as structured model inputs
- Final mathematical model or training formulation, including sets, indices, parameters, decision variables, objective, constraints, state transitions when relevant, feasibility rules, and terminal or boundary conventions
- Selected method and why it was chosen over alternatives
- Why the selected method has an acceptable performance ceiling for the problem, or why the user accepted it as a limited interim baseline
- Detailed method explanation, not just the method name
- Important assumptions
- Implementation details and final project structure
- Project delivery guide: major files, folders, scripts, configs, run records, and operator-facing workflow
- Run details for jobs expected to exceed 3 minutes, including test evidence, runtime estimate versus actual runtime, user-facing `run` command, progress/status/result files, checkpoints, and any interruption or restart
- Run logs and output files: which structured files recorded cost/objective/reward, feasibility, loss/gap, status, and model/checkpoint outputs; why the output layout is concise enough for operators to use
- Results
- Training convergence diagnostics when a learned method is used, including learning/evaluation curves, losses where available, feasibility-violation curves, seed variability, stopping reason, and convergence status
- Tuning and model-size audit when a learned, simulation, or numerical method is used, including architecture, batch/rollout/scenario settings, search space or tuning tried, seed count, runtime budget, and why the final settings are appropriate
- Acceptance result: whether the final policy or solution is acceptable, failed, or preliminary relative to strong baselines or lower bounds. Do not present a weak policy as a useful deliverable simply because it is runnable.
- If the final method is a heuristic, random search, differential-evolution-tuned policy, or other low-ceiling approach, explicitly label it as baseline/interim unless the report documents why higher-ceiling DRL/ADP/solver/hybrid alternatives were infeasible, unnecessary, or empirically dominated.
- Ex-post optimal, lower-bound, or baseline benchmark design
- Per-trajectory and aggregate benchmark gaps
- Baseline definitions and individual baseline results. If many baselines were evaluated, list each one separately with its own metrics, status, and notes. Do not add a single aggregate baseline row or summary number in place of the individual rows.
- Validation or sanity checks
- Main generated files table: path, purpose, contents, key columns or fields, units, update frequency, and operator use. Do not force readers to infer file meaning from names alone.
- Limitations
- Future improvements

For expert readability, also include:

- Precise notation and parameter definitions near the model elements where they are used
- Concise technical interpretation after important formulas, policies, benchmark tables, and result metrics
- Implementation implications for the selected method and final results
- Clear distinction between implementable policy performance and hindsight or lower-bound benchmarks
- Clear distinction between individual baseline methods, with no aggregate baseline shortcut replacing the per-method rows
- Practical caveats about data quality, runtime, maintenance, and validity limits

Method explanation requirements depend on the selected approach:

- Analytical or theoretical method: explain the principle, structural property, recurrence, decomposition, bound, theorem, or heuristic rule being used; include the assumptions required for it, a derivation or proof sketch when applicable, and why the method is expected to be correct or useful.
- Dynamic programming or Markov decision process: define state, action, transition, cost/reward, Bellman equation, horizon or discounting convention, approximation or truncation, and convergence or optimality conditions.
- Solver-based optimization: state the model class, variables, constraints, objective, solver choice, solver status, optimality gap, major preprocessing steps, and any relaxation or decomposition.
- Simulation or heuristic method: describe the policy logic, parameter tuning process, random seed handling, evaluation design, and baseline comparisons.
- Training-based method: describe the available data, labels or rewards, model target, train/validation/test protocol, baseline policies, feasibility repair or constraint handling, tuning and model-size choices, convergence diagnostics, stopping rule, seed variability, non-convergence warnings, overfitting risks, and the next iteration when acceptance criteria are not met.

The report should include enough formulas, tables, and explanatory prose that a reader can reconstruct the modeling logic without opening the source code. If the source code is the only place where a variable, cost term, constraint, benchmark, or assumption is defined, the report is incomplete.

Final reports must follow the plain-language terminology rules in `references/response_style.md`. Avoid rare workflow words in user-facing prose when a common localized phrase exists; for example, use `测试用例` or `验证用小样例数据` rather than `fixture` in Chinese prose, unless referring to a literal filename or code identifier.

For any result-bearing final report, benchmark transparency is mandatory. Do not use a single aggregate baseline row or summary number when multiple baselines were run or planned. Include:

- A baseline definition table with one row per baseline.
- A baseline result table using the standard comparison shape from `references/response_style.md`: for Chinese reports, columns must be `实验设置`, `方法`, `结果`, `解释/讨论`; for English reports, use `Experiment Setting`, `Method`, `Result`, `Interpretation / Discussion`.
- One row per baseline per evaluation split, trajectory, scenario group, seed group, or aggregate level as appropriate, with the selected method, fallback methods, peer methods, and lower-bound or hindsight benchmarks shown under the same `实验设置`.
- A status and explanation for failed, infeasible, timed-out, skipped, unavailable, or hindsight-only baselines inside the `结果` or `解释/讨论` cell, not by dropping the row.
- A short interpretation that points to the individual baseline rows when explaining which method performed better on each metric.
- A short interpretation explaining whether the primary method beats each baseline, only some baselines, or none.

The archive should avoid unnecessary clutter. Prefer a concise top-level structure with `run_config.json`, `artifact_manifest.json`, one structured progress file per run or experiment group, status files, result summaries, model/checkpoint folders, and a small set of diagnostic plots. Put verbose raw traces under `raw/` only when they are necessary for debugging or reproducibility.

Mathematical expressions in the report must be visually readable. In PDF, HTML, and Markdown report copies, do not use tables for model notation, objectives, constraints, cost formulas, Bellman equations, or state transitions; use indented definitions and standalone rendered LaTeX equations or rendered equation images instead. Use MathJax, KaTeX, LaTeX, or another reliable renderer when available. Do not leave uncompiled LaTeX source as ordinary visible prose in the final report when a rendered alternative is available.

Any HTML review copy is read-only: do not include input boxes, forms, buttons, clickable choice boxes, comment panels, localStorage state, or editable fields. Generate the PDF by default when the user asks for final documentation. Render and visually inspect any generated PDF or DOCX when rendering tools are available. If PDF export cannot be completed, produce the best available HTML or Markdown version and state the blocker clearly.

## Reproducibility

The archived project should be runnable with Python from the folder, subject to any documented license or installation requirements. If a commercial solver, GPU dependency, or external data source is required, document it clearly.
