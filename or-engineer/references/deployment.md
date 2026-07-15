# Deployment

Creator and maintainer: Xiaotian Liu · xiaotianliu01@gmail.com

## Mission

Implement the user-selected method as a delivery-ready Python project, run smoke and pilot validation, clean the project, and produce a project manual that the user can use to run the code locally. Before implementation, create a concrete implementation plan, pass a pre-deployment reviewer check, return the plan to the user, and wait for user confirmation.

Deployment is responsible for producing a useful, readable, runnable project, not only a loose script or a single result file. Every implementation choice that can materially affect solution quality must be considered explicitly: model capacity, hyperparameters, solver tolerances, scenario count, training budget, reward/objective scaling, normalization, action representation, and benchmark design.

Deployment must preserve the selected method's performance ceiling. Do not simplify a selected high-ceiling method into random parameter search, a narrow handcrafted heuristic, or a toy training run because that is easier to implement. If the selected method cannot be deployed faithfully under the observed environment, return a revised Deployment Confirmation Report that names the blocker and asks the user to choose between installing dependencies, using a licensed solver, allocating more runtime, selecting the closest faithful fallback, or explicitly accepting a low-ceiling interim baseline.

When the selected method includes stochastic or nonconvex training, deployment must implement a credible fallback path as part of the project plan. The fallback may be a tuned structural policy, rolling-horizon or myopic optimizer, sample-average rule, incumbent production rule, lower-risk learned model, residual anchor, or solver-backed repair route, but it must be configured, evaluated, and reported under the same problem contract. Do not wait until a failed pilot to invent the fallback.

Prefer a fallback with a clear reliability guarantee. Deployment configuration must record the fallback guarantee type, guarantee statement, scope, evidence/certificate path, acceptance threshold, and activation trigger. Examples include solver gap certificates for a rolling-horizon MILP, feasibility-by-construction checks for a structural rule, lower/upper-bound comparisons, incumbent-safe switching rules, or confidence intervals from repeated scenario evaluation. If the fallback is empirical-only, record why no stronger guaranteed fallback is available and mark the delivery as preliminary unless the user explicitly accepts that risk.

Deployment must keep the delivered project clean. After generating the initial stage reports and before giving a deployment project or run manual to the user, remove task-irrelevant example data, placeholder demo files, stale scratch outputs, failed-run leftovers, notebook checkpoints, cache files, duplicate logs, useless empty folders, and any fake/sample data that are not required as explicit tests. Do not leave asset-template example datasets in the adapted project unless they are intentionally converted into a small documented test dataset. Smoke and pilot outputs are internal validation evidence; once the code path works and pilot checks have selected the best feasible configuration, delete smoke/pilot run folders, pilot-only configs, temporary models, scratch plots, tuning leftovers, and empty directories that no longer have a documented purpose from the delivered project. Keep only a concise summary of pilot evidence in the workspace-level report or a top-level manifest when needed for audit.

Before choosing a project scaffold, read `assets/asset_registry.md` and inspect every direct child folder under `assets/` that contains `asset_manifest.json`. Treat user-added assets the same way as built-in assets. Select the asset or asset combination whose manifest and guide best match the selected method, confirmed formulation, performance-ceiling target, dependency constraints, and industrial quality policy.

Built-in examples include mathematical programming, reformulation, decomposition, stochastic/robust optimization, simulation optimization, CP/CP-SAT, DRL/MDP, and supervised learning assets. These examples are not a closed list. If a user-added asset better matches the method or local stack, use it and cite its manifest and guide in the Deployment Confirmation Report.

Copy the selected asset into the deployment workspace and adapt its contracts instead of rebuilding plumbing from scratch. The copied asset should define the project skeleton, configuration files, foreground `run` scripts, compact run records, progress output, evaluation protocol, and artifact manifest. If more than one asset is needed, such as supervised forecasting feeding stochastic optimization, state how their data and run-record contracts connect.

Read the selected asset's `asset_manifest.json` and `framework_guide.md` before writing code. Load only the extra catalog, contract, or template files that are relevant to the selected method. If the selected asset's acceptance criteria cannot be satisfied for the confirmed problem and observed environment, do not copy it as a cosmetic shell; revise the method, choose a better asset, or return a Deployment Confirmation Report that asks the user to decide.

## Dependency Check

Before writing final code or returning the Deployment Confirmation Report, inspect the current execution environment for the selected method. The survey must be specific to the deployment plan rather than a generic machine inventory.

Include, when relevant:

- Programming runtime: executable path, language/runtime version, package manager availability, and active environment name or path when discoverable.
- Python environment discovery: if `conda`, `mamba`, or `micromamba` is available, enumerate environments with the appropriate environment-list command and inspect plausible non-default Python environments before concluding that a package, solver, GPU stack, or data reader is missing. For each relevant environment, report the Python executable path, Python version, and method-specific package/solver availability. Do not assume the shell's default Python is the only usable environment.
- Required packages: availability and versions for core libraries, modeling frameworks, RL/ML libraries, solvers, data readers, visualization/reporting libraries, and any package required by the implementation plan.
- Hardware and accelerators: CPU basics when useful, plus GPU/CUDA/MPS/accelerator availability, device model, driver/runtime compatibility, VRAM when discoverable, and framework visibility when training, large simulation, numerical optimization, or deep learning performance depends on it. For Python neural or RL methods, probe both the system and the selected Python environment, such as `nvidia-smi` when available and framework checks like `torch.cuda.is_available()` or the equivalent for the planned library.
- Optimization solvers: installed Python solver packages, command-line solvers, commercial-solver license assumptions, and fallback solver paths.
- System constraints: operating system, writable output locations, expected runtime/memory pressure, and external-service or network needs when applicable.

### Solver Capability Verification

For optimization deployments, solver readiness must be tested carefully because `import gurobipy`, `import cplex`, `import highspy`, or successful construction of a solver/model object does not prove that the solver can actually solve under the current environment, license, path, and sandbox constraints.

Before declaring a solver available, unavailable, or inferior, perform the strongest practical solver audit for the selected method:

- Enumerate plausible Python environments first. If `conda`, `mamba`, or `micromamba` exists, inspect non-default environments for modeling packages and solvers before requesting installation into the active shell environment.
- Check every relevant invocation route, not only package import:
  - direct Python APIs such as `gurobipy`, `cplex`, `mosek`, `highspy`, `pyscipopt`, or `xpress`;
  - modeling-framework adapters such as Pyomo `SolverFactory`, Pyomo Appsi, CVXPY installed solvers, PuLP solver lists, OR-Tools CP-SAT, or python-mip;
  - command-line executables such as `gurobi_cl`, `cplex`, `cbc`, `glpsol`, `highs`, `scip`, `xpress`, or `minizinc`.
- Run a tiny representative solve probe in the same interface planned for deployment: LP for LP models, MILP for mixed-integer models, CP-SAT for CP models, conic/QP/NLP probes when those features are required, and a PWL/indicator/SOS probe when the formulation depends on those solver features.
- Record separate statuses for `package_available`, `executable_available`, `model_creation_ok`, `solve_probe_ok`, `solver_status`, `objective`, `license_status`, `interface_used`, and `failure_message`. Do not collapse these into a single yes/no field.
- Prefer the fastest installed solver that passes the solve probe and supports the required formulation features. For example, use a working Gurobi/CPLEX/Xpress/Mosek/SCIP installation when license terms and user approval allow it; use HiGHS/CBC/GLPK/OR-Tools as faithful open-source routes when they are sufficient or when commercial solvers are not available.
- If a commercial solver or license-managed solver fails with host-resolution, DNS, token-service, WLS, license-server, network, permission, executable-path, or restricted-filesystem symptoms, treat the result as `blocked-by-sandbox-or-license-check` until a minimal solve has been retried through the normal approval/escalation path when that path is available. Do not report the solver as unavailable merely because the sandbox blocked a license token or license server.
- If a non-sandbox or escalated probe succeeds, update the Deployment Confirmation Report and implementation plan to use that solver by default when it materially improves performance and the user has approved the license/network requirement. Keep an open-source fallback configured for users who cannot use that solver locally.
- If a probe requires network access, license credentials, a license server, or writing outside the workspace, ask for user approval through the execution environment's normal approval mechanism before running it. Report the exact reason for the approval request and the fallback if approval is denied.

If a required package or capability is missing:

- Prefer an already installed alternative when it preserves the selected method.
- Ask the user before installing packages.
- Ask the user before using a commercial solver or any tool that may require a license.
- Do not replace a user-selected advanced method such as PPO, actor-critic, fitted value iteration, tree/regression policy learning, PWL/dynamic MILP, decomposition, CP-SAT, or stochastic programming with a simpler heuristic merely to avoid dependency or training complexity. Missing packages, solvers, licenses, or GPU libraries are deployment blockers or install actions, not method-selection evidence that the high-ceiling method is bad.
- In the Deployment Confirmation Report, list every material missing dependency in an explicit dependency action table: missing capability, why the selected method needs it, preferred install or license route, expected command or package family when known, risk if installation fails, and the closest faithful fallback. The report must ask the user whether to approve installation/license setup or choose the fallback.
- After the user approves deployment and explicitly approves dependency installation or license use, attempt the installation or setup through the normal escalation/approval mechanism for the execution environment. If the install or license check fails, record the failure, regenerate or revise the deployment plan, and ask the user whether to retry, provide credentials/licenses, use an already installed equivalent, or proceed with the closest faithful fallback. Do not silently proceed with a lower-ceiling substitute.
- If the user does not approve installing the missing dependency or using the licensed solver/tool, report that decision as the reason the selected high-ceiling method cannot be faithfully deployed in the current environment. Then either use an approved faithful fallback or return to method/deployment selection; do not imply that the high-ceiling method was technically unsuitable.
- If a strong method is feasible in principle but blocked by environment only, keep it visible in reports as `blocked-by-environment`, `requires-install`, or `requires-license`, not `rejected`.
- If supplied project files already contain relevant high-ceiling implementation assets, inspect them before designing from scratch. Examples include RL environments and training scripts, actor/critic checkpoints, solver baselines, PWL linearization utilities, scenario generators, and evaluation scripts.
- For asset-based deployment, inspect the selected asset's `requirements.optional.txt` along with the active Python environment. Report missing packages, solvers, simulation tools, parallel tools, deep-learning libraries, or licensed APIs only when they affect the selected concrete plan.
- If commercial solver or deep-learning dependencies are missing but the selected method needs them, ask for approval or propose a faithful open-source or existing-code fallback. Do not silently substitute random search as the final method.

## Implementation Requirements

Add the creator attribution required by references/response_style.md to generated project-level README files and delivery manuals. Keep code modules, configs, logs, user data, and structured experiment records free of repetitive attribution metadata.

- Before writing final deployment code or running solvers/training, produce a static HTML Deployment Confirmation Report using the fixed structure in `references/workflow.md`.
- The report must be based on the user-confirmed formulation and user-selected method.
- The report must include a concise environment survey showing what was checked, what is available, what is missing, and how those facts affect the implementation plan.
- The report must include a reviewer check confirming that the planned implementation covers the objective, constraints, data preprocessing, benchmark design, dependencies, observed environment readiness, and known risks.
- The HTML report is read-only: do not include input boxes, forms, buttons, clickable choice boxes, comment panels, localStorage state, or editable fields.
- Return the report path/link in chat with a compact text approval prompt. Do not deploy until the user confirms in chat. If the user requests changes, revise the plan and repeat the confirmation step.
- Keep the implementation aligned with the reviewer-approved mathematical logic.
- Separate data loading, model construction, solve or train logic, evaluation, and result export when the project is nontrivial.
- When creating a project codebase, keep the layout concise and easy to inspect, in the style of the BOM example: a small set of obvious folders such as `configs/`, `data/`, `src/` or task modules, `scripts/`, and `runs/`; clear entrypoints; no unnecessary framework layers; and no scattered one-off notebooks or duplicate scripts unless the user asks for them. Do not create a project-local `reports/` folder; all deployment-generated HTML reports belong in the workspace-level `reports/` folder.
- When adapting copied assets, delete unused template example files, fake datasets, generic placeholder configs, and irrelevant demo outputs after replacing them with task-specific files. Keep only real user data references, approved generated synthetic data with documented generation rules, minimal unit-test datasets, and reproducible run artifacts.
- When creating project documentation, README-style notes, run instructions, report text, or operator-facing comments from a selected asset, follow the user-facing language contract in `references/response_style.md`. Keep code identifiers, filenames, package names, config keys, metric keys, and CLI flags in English unless the user explicitly requests localized names.
- Write code for an engineer who may need to modify it later. Comments must be distributed through the implementation, not only placed in file headers. Add module docstrings for module purpose, then add focused comments before or inside non-obvious blocks: data schema assumptions, unit conversions, stochastic scenario generation, objective term construction, variable indexing, constraint blocks, Big-M or bound derivation, state/action/reward definitions, solver status handling, feasibility repair, baseline definitions, fallback activation, run-record schemas, seed handling, and dependency/license branches. Comments should explain the business or mathematical reason for the block, what invariant it preserves, and what can safely be changed. Avoid comments that merely restate a variable assignment, but do not leave dense OR, solver, stochastic, or training logic unexplained.
- User-editable configuration files must explain every material parameter directly where the user edits it. Prefer comment-capable formats such as YAML, TOML, or shell-style `.env` for generated configs. Each tunable field must have a nearby comment explaining what it controls, units, safe ranges or typical values, runtime/quality tradeoff, and when a user should change it. If a library or existing interface requires JSON, also generate a sibling commented template such as `config.example.yaml` or `CONFIG_GUIDE.md`, and add safe descriptive fields only when they do not break the parser. Material knobs include horizon length, scenario count, solver tolerances, time limits, PWL segment counts, neural-network sizes, learning rates, batch/rollout sizes, seed counts, baseline toggles, fallback triggers, output paths, and acceptance thresholds.
- Treat the deployed codebase as a user delivery project. Include all agreed method code, scripts, configuration, result collection, structured run records, and minimal documentation needed to run and inspect the project without relying on chat history.
- Keep command-line output concise and useful, but not opaque. Each entrypoint should print current phase, iteration/epoch/timestep or case id, elapsed time, primary metric, feasibility or violation diagnostics when relevant, current best metric, and output directory. For long solver, training, simulation, or benchmark jobs, the normal terminal path must also print completed work units, total work units, percent complete, ETA, observed throughput, and the current method/case/seed/path so an operator can tell where the run is and how long it is likely to take. Avoid verbose raw traces in the normal terminal path.
- Handle solver or training failure states explicitly.
- Save logs or status summaries when useful.
- Preserve the method class chosen in the Method Selection Report. If the implementation plan changes method class, such as from dynamic MILP or MAPPO to heuristic random search, stop and regenerate the Method Selection or Deployment Confirmation Report before coding.
- When using any asset under `assets/`, keep the output layout compatible with that asset's `run_records/` templates: `run_config.json`, `status.json`, `progress.csv` or `progress.jsonl`, `artifact_manifest.json`, terminal progress output, method-specific model or solution artifacts, evaluation summaries, and benchmark outputs.
- Record process metrics during nontrivial runs, especially training, solver jobs, simulation optimization, or benchmarks expected to run longer than 3 minutes. For every long run, record `progress_index`, `total_progress_units`, `progress_pct`, `elapsed_seconds`, `eta_seconds`, and `throughput_per_min` in addition to method-specific metrics. For training, record cost or reward over time, evaluation cost, feasibility violations, projection or repair magnitude, losses where available, elapsed time, and current best policy or objective. For solvers, record incumbent objective, bound, gap, feasibility, nodes or iterations, elapsed time, and solver status.
- Keep run artifacts tidy and operator-readable. Prefer a small set of canonical files with clear schemas over many scattered ad hoc logs. Aggregate repeated metrics into one `progress.csv` or `progress.jsonl` per run or per clearly separated experiment group.
- Use deterministic seeds for randomized heuristics or training when possible.
- Define the acceptance criteria in code or run configuration before large runs: primary metric, feasibility threshold, baselines to beat, target improvement, maximum acceptable gap to a lower bound or strong baseline, and what counts as a failed pilot.
- Implement baselines as fair comparators. Each baseline configuration should include material tunable parameters, a tuning budget or fixed-parameter rationale, the tuning data/scenario split, and the final selected settings. Tune heuristic thresholds, base-stock levels, myopic lookahead lengths, dispatching-rule weights, simulation-search budgets, or solver time limits when those choices materially affect the result and the runtime budget permits. Do not leave a baseline at an arbitrary weak default simply to make the primary method look better.
- For training-based methods, define the fallback method in code or run configuration before large runs: fallback id, role, implementation route, dependencies, trigger condition, evaluation metric, acceptance threshold, and whether it can be packaged as the selected policy if training remains unstable.
- For training-based methods, define the fallback guarantee in code or run configuration before large runs: guarantee type, guarantee statement, guarantee scope, evidence or certificate path, and whether the fallback is deployable, hybrid-only, interim, or diagnostic-only.
- Define every baseline separately in code or run configuration. Each baseline must have a unique id, method description, data/features used, fixed parameters or tuning settings, implementability or hindsight status, and reason for inclusion. Do not configure an aggregate baseline shortcut without saving individual baseline definitions and results.
- Do not use arbitrary tiny defaults for serious learned or numerical methods. Set hyperparameters from problem scale, library guidance, prior pilot evidence, or a documented tuning plan. Save the chosen values and rationale.
- When the user permits meaningful runtime, use a staged approach: smoke test for code health, pilot tuning for quality signal, then write a user-facing `run` command or `.sh` script for the best configuration. The `run` job should be started by the user in the foreground. If the user can run a larger job locally, prepare larger neural networks, larger batches, more timesteps/scenarios, multiple seeds, or a small hyperparameter search when they are likely to improve quality.
- For GPU-capable training or numerical workloads, add an explicit device setting such as `device: auto`, `cuda`, `mps`, or `cpu` when supported by the stack. Default to `auto`; select the GPU when it is visible to the chosen framework and expected to improve throughput; print and record the selected device in `run_config.json`, `status.json`, and terminal output. If GPU support is absent or incompatible, fall back to CPU only after recording the reason and the expected runtime impact.
- If a pilot is weak and approved runtime remains, iterate a few times before delivery. Prefer targeted changes to the most likely cause of failure: feature leakage, baseline construction, objective scaling, reward normalization, feasibility repair, action encoding, model capacity, batch/rollout size, scenario count, solver tolerance, warm starts, seed count, or training budget. When a very similar peer deployment candidate is likely to dominate the selected configuration, test that peer candidate as a serious alternative rather than packaging a known-weak pilot.
- If all targeted training redesign attempts are inconclusive or failed, activate the configured fallback rule. Package the fallback only if it satisfies its acceptance threshold; otherwise label the project result as preliminary or failed and identify the next method-ceiling step.
- For learned or black-box policies, save model artifacts, hyperparameters, training curves, random seeds, evaluation seeds, and action-projection or feasibility-repair logic so the result is reproducible and auditable.
- For any training-based method, instrument convergence explicitly. Save raw training logs, evaluation logs, learning curves, validation or rollout curves, relevant loss curves, constraint-violation curves, seed-level summaries, stopping criteria, and a convergence status label such as `acceptable`, `inconclusive`, or `failed`.
- For any neural, RL, actor-critic, supervised, fitted-value, forecasting, or surrogate model, implement best-checkpoint selection. Evaluate at fixed intervals on held-out seeds, trajectories, validation splits, or scenarios; append each evaluation to structured progress records; save a best checkpoint whenever the selected validation/evaluation metric improves; update `status.json` with `best_metric`, `best_checkpoint`, and `best_step`; and run final evaluation from `best_checkpoint` by default. The last checkpoint may be retained for diagnostics, but it must not silently replace the best checkpoint.
- For any neural, RL, actor-critic, supervised, fitted-value, forecasting, or surrogate model, implement a fallback selection record. `run_config.json` should name the fallback candidate and trigger; `status.json` should record whether fallback was activated; final result files should state whether the selected artifact is the trained model, hybrid model, or fallback method.
- For PPO, actor-critic, or related RL methods, capture metrics such as episodic reward/cost, evaluation cost, policy loss, value loss, entropy, approximate KL, clip fraction, explained variance, learning rate, feasibility violations, projection/repair magnitude, elapsed time, and timesteps. Use the metrics available from the selected library rather than fabricating unavailable diagnostics.
- If a run is only a smoke test or short pilot, label convergence as `inconclusive` and state that the run validates plumbing rather than policy quality.
- Include clear instructions for rerunning the code, including the exact smoke command you verified internally when useful for debugging and the exact `run` command the user can execute.
- After implementation, smoke verification, pilot validation, and cleanup, generate a static HTML Project Delivery And Run Manual using `references/response_style.md`. Regenerate it whenever later iterations materially change files, commands, outputs, acceptance-status interpretation, dependency status, or pilot evidence.
- Before returning the Project Delivery And Run Manual, run a pre-delivery cleanup pass and record it in the manual or artifact manifest. The pass must verify that no nonexistent-data references, orphaned example folders, smoke outputs, pilot outputs, pilot-only configs, temporary debug files, cache directories, useless empty folders, or irrelevant asset-template files remain in the delivered project tree.

## Delivery Project Requirements

The deployment project should be directly usable by the user after delivery. Prefer this concise structure unless the selected asset or problem requires a different simple layout:

```text
project_root/
  configs/
  data/ or data_refs/
  src/
  scripts/
  runs/
  docs/ or README.md
  requirements.txt
```

Required project properties:

- Clear entrypoints for the user-facing `run`, evaluation, and result collection when those phases apply. Smoke and pilot commands may exist during development, but remove or hide them before delivery unless the user explicitly asks to keep debug commands.
- A small number of user-editable configuration files with inline comments for material settings. Prefer YAML/TOML over JSON for new configs so comments can live in the file. If JSON must be retained, keep a commented YAML/TOML template or concise config guide next to it and make the user-facing instructions point to that commented source.
- A concise `requirements.txt` or environment note, including solver/license requirements when relevant.
- Structured run records under `runs/` or the selected asset's run folder, using `run_config.json`, `status.json`, `progress.csv` or `progress.jsonl`, `artifact_manifest.json`, and compact summaries.
- Scripts that can be run from the project root without relying on hidden notebook state or chat-only instructions.
- Operator-facing docs or README-style notes in the user's target language, while preserving code identifiers and metric keys in English.
- No unnecessary notebooks, duplicate scripts, deeply nested framework layers, or scattered one-off result files unless justified by the method.
- No stray example data, fake placeholder datasets, copied template outputs, cache folders, smoke/pilot outputs, pilot-only configs, or failed-trial leftovers. Any retained minimal test dataset must be small, documented, and explicitly needed for tests or demos that do not pretend to be real results.

## Project Delivery Manual

After smoke verifies the code path, pilot checks select the best feasible configuration, and cleanup removes smoke/pilot outputs, create a static read-only HTML Project Delivery And Run Manual. It must be detailed enough for the user or another engineer to run and inspect the project without reading the conversation.

Include:

- Project purpose and selected method.
- Confirmed input data or data references.
- Environment and dependency summary.
- Project tree with every important file or folder explained.
- Code-readability guide: identify the main modules/classes/functions a user is most likely to modify, the comments/docstrings that explain mathematical or solver/training logic, and the configuration files or README sections that explain safe parameter changes.
- Entrypoints and exact commands for the user-facing `run`, evaluation, and result collection when applicable. Mention smoke and pilot only as completed internal validation steps, not as commands the clean delivered project expects the user to run.
- Expected command-line output, including the meaning of printed metrics.
- Smoke status, detailed pilot evidence before cleanup, runtime estimate, and acceptance status.
- A `Pilot Experiments And Baseline Results` section that preserves the substantive pilot evidence even after pilot run folders are cleaned. For every pilot experiment condition that materially affected selection, report the experiment id, method configuration, data split or scenario set, seed(s), runtime budget, primary method metrics, every baseline or peer comparator's metrics in its own row, feasibility/convergence status, solver/training status, and the selection decision. Include weak, failed, timed-out, or superseded pilot conditions if they influenced tuning or method choice.
- A short interpretation of each pilot experiment that states which visible baseline row or peer row was strongest on each key metric, why the final configuration was selected, and whether the evidence is acceptable, inconclusive, or failed. Do not replace the pilot matrix with a narrative such as "the pilot looked good."
- A `Fallback Readiness And Selection` section for training-based deployments. It must state the fallback method, whether it was implemented and evaluated, its metric relative to the primary and strong baselines, the trigger for activation, whether activation occurred, and why the selected delivered method is primary, fallback, or preliminary.
- Acceptance criteria and baseline/bound comparison plan.
- Runtime estimate and foreground `run` command for jobs over 3 minutes.
- Run-record dictionary: `run_config.json`, `status.json`, `progress.csv` or `progress.jsonl`, `artifact_manifest.json`, result summaries, checkpoints/models, plots, and raw logs if present.
- How to monitor progress and how to tell whether a run is healthy, inconclusive, failed, or ready for analysis.
- What files or folder the user should point you to after `run` finishes.
- Known limitations, dependency risks, and the next iteration protocol.
- Delivery cleanup note: smoke/pilot outputs, pilot-only configs, and useless empty folders removed; minimal test datasets or placeholder directories intentionally retained if any; workspace-level reports location; and confirmation that run records reference existing files only.

## Run Logs And Output Files

For every serious run, design the file layout before starting it. The goal is that an operations analyst can inspect progress and understand the main outputs without opening source code or sorting through dozens of near-duplicate files.

Use a concise run folder such as:

```text
run_<timestamp>/
  run_config.json
  artifact_manifest.json
  status.json
  progress.csv or progress.jsonl
  stdout.log
  stderr.log
  results/
  models/ or checkpoints/
  plots/
```

Required process records:

- `run_config.json`: method, data, seeds, hyperparameters, acceptance criteria, baselines, runtime budget, environment assumptions, and run or rerun command.
- `artifact_manifest.json`: the purpose, schema, units, update frequency, and downstream use of each main generated file.
- `status.json`: current phase, start/end time, completion status, current case or iteration, last update time, and last error if any.
- `progress.csv` or `progress.jsonl`: a tidy longitudinal record. Include columns such as `timestamp`, `elapsed_seconds`, `progress_index`, `total_progress_units`, `progress_pct`, `eta_seconds`, `throughput_per_min`, `iteration` or `timestep`, `case_id`, `seed`, `train_cost` or `objective`, `eval_cost`, `best_cost`, `reward`, `loss`, `gap`, `feasibility_violation`, `projection_loss`, and relevant solver/RL diagnostics when available.
- `stdout.log` and `stderr.log`: raw process output only. Do not rely on them as the primary structured progress record.
- `results/`: final metrics and benchmark tables, preferably aggregated into a small number of CSV/JSON files.
- `models/` or `checkpoints/`: saved policies, model weights, solver warm starts, or checkpoint files.
- `plots/`: only the key diagnostic plots needed for review; avoid generating a plot for every minor metric unless it is requested or necessary.

Output-file rules:

- Avoid producing many per-step files. Append to a structured progress file instead.
- Avoid duplicated metric files with different names. If both CSV and JSON are useful, explain why in `artifact_manifest.json`.
- Use subfolders only for genuinely independent units such as cases, instances, seeds, or methods. Otherwise aggregate.
- Keep raw verbose traces optional and place them under `raw/` only when they are needed for debugging or reproducibility.
- Collect analysis data into as few canonical files as practical: one `progress.csv` or `progress.jsonl`, one `status.json`, one `run_config.json`, one `artifact_manifest.json`, and one compact `results/summary.json` or `results/summary.csv` unless the method genuinely needs separate per-case outputs.
- Ensure final reports include an output-file dictionary explaining the main files and what an operator should inspect first.
- Store baseline comparison results in a long or otherwise explicit table with one row per baseline method, split/scenario/trajectory/seed group, metric, and status when practical. Do not store only an aggregate baseline result; any interpretation of which baseline performed better must point back to the individual baseline rows.
- Before user delivery, delete temporary smoke/pilot scratch folders, stale failed-run outputs, ad hoc debug dumps, copied example datasets, and generated junk files that are not listed in `artifact_manifest.json`. If a file is kept, it must either be source code/config, a documented data reference, a minimal test dataset, a canonical run record, a model/checkpoint needed for reproducibility, or a final report.

## Run Protocol

Use this protocol for any training, solver, simulation, benchmark, or experiment expected to run longer than 3 minutes.

1. Run a reduced smoke-test configuration first. Keep the same code path as the user-facing `run`, but reduce timesteps, scenarios, epochs, horizon, seeds, or instance count enough to finish quickly.
2. During the smoke test, verify:
   - Code starts and exits normally.
   - Data loading, model/environment construction, solver/trainer setup, evaluation hooks, logging, checkpointing, and artifact writing all work.
   - Loss, reward, objective, cost, or optimality gap moves in a plausible direction when that can be assessed.
   - Hard constraints, feasibility repair, numerical values, and memory use are sane.
3. If solution quality depends on training or numerical tuning, run a pilot configuration with an explicit acceptance check before recommending the user-facing `run`. The pilot may still be smaller than `run`, but it must be large enough to compare against meaningful baselines and detect bad design choices. It should report early learning or objective improvement, feasibility, benchmark gaps, and at least one material hyperparameter or architecture sanity check when feasible. Save or summarize the pilot results in a structured comparison table with one row for the primary method and one row for every baseline/peer method under the same experiment condition.
4. If the pilot loses badly to a strong simple baseline, fails to improve beyond a do-nothing baseline, violates hard constraints, or shows unstable/non-learning diagnostics, do not provide `run` instructions unchanged. Diagnose and revise the likely cause: model capacity, batch size, rollout length, learning rate, reward/objective scaling, normalization, action encoding, feasibility projection penalty, seed count, scenario count, solver tolerances, or benchmark implementation. Iterate a few times when the runtime budget allows, and test a very similar peer deployment candidate when it is the most plausible way to get a good pilot.
5. If the targeted revisions still fail or the approved budget is exhausted, evaluate and select the pre-declared fallback when it satisfies its fallback acceptance threshold. If neither primary nor fallback is acceptable, report a failed or preliminary deployment rather than handing off an unstable trained model as production-ready.
   The fallback selection record must include the fallback guarantee type, evidence/certificate file, and any scope limitations.
6. Estimate `run` runtime from the smoke and pilot runs using a documented scaling rule, such as seconds per timestep, scenario, epoch, rollout, branch-and-bound node, or optimization iteration. Save this estimate in the run configuration or workspace-level report.
7. Write a concise `run` script when useful, preferably a `.sh` script with explicit arguments such as `--phase run`, output directory, seed, budget, and config path. The script must run in the foreground and print meaningful progress to the terminal.
8. Ensure the `run` code writes a small number of durable files that are easy to inspect later:
   - `run_config.json`
   - `artifact_manifest.json`
   - `status.json`
   - `progress.csv` or `progress.jsonl`
   - one compact result summary under `results/`
   - models or checkpoints only when needed
   - optional raw logs only under `raw/`
9. After smoke and pilot runs, clean the project tree before delivery: remove scratch directories, temporary debug dumps, unused copied examples, fake/demo datasets, smoke outputs, pilot outputs, pilot-only configs, temporary pilot models/checkpoints, stale failed-run files, and useless empty folders. Keep only source/config files needed for `run`, real data references, explicitly requested minimal test datasets, documented placeholder directories, and final delivery metadata that references existing files.
10. Make command-line output operator-friendly because the user will run the command themselves. Training code should print epoch/step, elapsed time, train loss, validation or rollout metric, current best metric, fallback status when relevant, feasibility or constraint violation where relevant, and output paths. Solver code should print status, incumbent objective, bound, gap, nodes or iterations, elapsed time, and output paths. Simulation code should print candidate id, replications, mean objective, uncertainty, baseline gap, and current best.
    For any job expected to exceed 3 minutes, terminal progress output must additionally include:
   - `progress`: completed work units / total work units and percent complete. Define the work unit explicitly, such as solver window, epoch, rollout batch, simulation candidate, benchmark trajectory, seed, or instance.
   - `eta`: remaining runtime estimated from observed throughput, plus elapsed time and throughput per minute. During the first few updates, label ETA as warm-up or unstable rather than implying precision.
   - `where`: method, phase, network/instance/case id, seed, path/scenario, period/window/epoch/iteration, and output directory.
   - `quality`: current objective/cost/reward/loss, current best metric, solver bound/gap/status, or training validation metric as applicable.
   - `health`: feasibility violation, backlog/shortage, hard-constraint violation, repair magnitude, fallback/emergency activation, timeout, or infeasibility warnings when relevant.
   The terminal should refresh at least once per meaningful decision unit and at least every 30-60 seconds for slow iterations. Raw solver traces may be saved separately, but the normal terminal path must remain readable without requiring the user to open a log file.
11. Return concise `run` instructions in chat and in the Project Delivery And Run Manual. Include smoke status, detailed pilot comparison evidence before cleanup, fallback readiness and activation status when training is involved, estimated runtime, exact `run` command, expected terminal output, progress/status/result file paths, what metrics the user should watch, and a note that after the run finishes the user can ask you to analyze the saved results.
12. When the user later asks for final analysis, read the saved progress, status, convergence artifacts, fallback-selection records, models/checkpoints, evaluation outputs, and benchmark files. Then produce the final results or technical report from those saved artifacts.

## Hyperparameter And Design Tuning

For any method where technical settings can materially change the result, tune or justify them before final deployment.

- PPO / actor-critic: consider policy/value network width and depth, activation, `n_steps`, batch size, epochs, learning rate, entropy coefficient, clip range, reward scaling, observation normalization, action scaling, feasibility projection penalty, total timesteps, evaluation episodes, and seed count.
- Tree or fitted-value methods: consider sample count, scenario generation, target construction, tree depth, ensemble size, regularization, validation split, and policy extraction from value estimates.
- Simulation optimization: consider policy parameterization, search ranges, scenario count, common random numbers, ranking-and-selection rules, and stopping criteria.
- Solver-based methods: consider relaxation strength, discretization granularity, solver tolerances, warm starts, scenario tree size, decomposition, and time limits.

If the selected or fallback method uses random search or differential evolution, state whether it is:

- a baseline,
- a warm start for a learned or solver method,
- a tuning subroutine inside a broader high-ceiling method,
- or an explicitly accepted low-ceiling interim deliverable.

Only the last case may be reported as the final primary method, and only after the user has accepted that tradeoff.

If a chosen configuration is small because of environment limits, state that explicitly and label the result as limited. If budget remains and the pilot is weak, run a stronger configuration instead of writing a final report around a poor policy.

## Deployment Review And Tuning Loop

Use this loop when a pilot is feasible within the user's runtime budget.

1. Baseline first: implement and evaluate strong baselines before or alongside the learned/optimized method. Include do-nothing only as a diagnostic baseline.
2. Smoke test: run the smallest configuration that exercises code, logging, feasibility, and checkpoints.
3. Pilot tier: run at least one credible configuration sized for quality, such as a larger neural network, larger batch/rollout, more scenarios, more solver time, or stronger search budget. If the method has material hyperparameters, compare at least two plausible settings when runtime allows. Training pilots must use periodic validation/evaluation and best-checkpoint saving; final pilot metrics should be computed from the best checkpoint unless the report explicitly compares best versus last.
4. Quality decision: compare pilot results to each approved baseline and feasibility threshold. Use confidence intervals or repeated seeds when stochastic noise could change the conclusion. Preserve the comparison as a pilot experiment matrix in the delivery manual: one row per method/baseline/peer per experiment condition, with status and metric columns aligned across rows.
5. Iterate if weak: if the policy only beats do-nothing or loses to a strong simple baseline, revise before preparing `run`. Make a small number of targeted iterations when budget allows rather than giving up after the first pilot. Typical revisions include evaluation interval and best-checkpoint selection, reward scaling, observation normalization, larger model, larger batch/rollout, longer training, warm start from the baseline, residual policy learning, action-space redesign, stronger optimizer settings, corrected feature construction, or corrected baseline logic. Stop only when the approved tuning budget is exhausted, a stronger peer method clearly dominates, or the user accepts the lower-ceiling result.
6. Test a peer deployment when appropriate. If a very similar model family or solver setup is likely to dominate the current pilot without changing the approved problem formulation, run it as a peer candidate and select the better pilot-supported configuration.
7. Select or activate fallback when appropriate. If the primary learned method remains unstable or underperforms after the planned iterations, compare it against the pre-declared fallback using the same metric and feasibility checks. Select the fallback for delivery only if it satisfies the fallback acceptance threshold; otherwise recommend a higher-ceiling next step instead of hiding the failure.
8. Escalate method ceiling if narrow policy search saturates. If a handcrafted parameter search improves a baseline but still has obvious structural limits, consider moving to residual RL/ADP, a richer policy class, rolling-horizon MILP/MPC, or PWL solver benchmarks before presenting it as final.
9. `run` package: prepare the best defensible `run` configuration, foreground command, `.sh` script when useful, progress logging, best-checkpoint evaluation, fallback-selection records, and concise result collection files, with the technical rationale saved in `run_config.json`.
10. Final report after results from the user's `run`: if the final policy still fails the acceptance criteria, label it as failed or preliminary and identify the next design step. Do not present it as a useful deployed policy.

## Environment Survey Examples

Tailor the survey to the method. Examples:

- Python environment discovery: report the active Python first, then list relevant conda/mamba environments discovered. If another environment already contains the needed solver, RL framework, GPU stack, workbook reader, or modeling package, prefer that environment or ask whether to use it before requesting installation into the default environment.
- PPO or deep RL: Python executable/version; `numpy`, `torch`, `gymnasium` or equivalent environment API, PPO framework such as `stable_baselines3` when planned; GPU/CUDA availability and GPU model if available; whether CPU-only training is acceptable.
- Supervised forecasting, regression, or classification: Python executable/version; `numpy`, `pandas`, `scikit-learn`, planned tree libraries such as `xgboost`, `lightgbm`, or `catboost`, planned deep-learning libraries such as `torch`, and data readers such as `pyarrow` when required; GPU/CUDA availability when deep models are material.
- Tree or fitted value methods: Python executable/version; `numpy`, `scikit-learn` or planned custom implementation; memory/runtime implication for trajectory datasets.
- MILP or MINLP: Python executable/version; modeling packages such as `pyomo`, `pulp`, `ortools`, or `cvxpy`; installed solvers such as CBC, GLPK, HiGHS, SCIP, Gurobi, CPLEX, Xpress, or Mosek; license assumptions; direct API, command-line, and modeling-framework invocation route; tiny LP/MILP solve-probe status; and whether any failure was caused by sandbox, network, token/license service, executable path, or missing package.
- Decomposition or stochastic programming: base modeling package and solver readiness plus parallel execution package when planned, scenario data reader availability, and whether commercial solvers are needed for master or subproblems.
- Simulation optimization: simulator dependencies such as `simpy` when planned, search/tuning packages such as `optuna` or `nevergrad` when planned, parallel execution readiness, and output storage for trajectory logs.
- Constraint programming: `ortools`, MiniZinc, or CPMPy availability; CP-SAT worker/thread settings; and whether the model needs solver features such as interval variables, no-overlap, cumulative, or search hints.
- Spreadsheet/data-heavy workflows: workbook reader availability, file access, output paths, and any conversion dependency.

## Evaluation Benchmarks

When reporting final cost or reward results, include a benchmark for every evaluation trajectory whenever this is possible without changing the problem meaning.

- For deterministic realized trajectories, compute the ex-post optimal cost with full hindsight when the finite-horizon or scenario-specific optimization is tractable.
- Treat the ex-post optimum as a clairvoyant lower bound for minimization problems or upper bound for maximization problems. Clearly state that it is not an implementable online policy.
- Report, for each trajectory: method cost, ex-post optimal or lower-bound cost, absolute gap, relative gap, horizon length, seed or scenario id, and any infeasibility or boundary warnings.
- Report aggregate statistics across trajectories: mean, median, best, worst, and standard deviation of cost and gap.
- If exact hindsight optimization is too large, nonconvex, or solver-limited, document why and use a valid benchmark with its own visible result row, such as a linear relaxation, deterministic equivalent relaxation, perfect-information relaxation, rolling-horizon oracle, or clearly defined comparator.
- Keep benchmark assumptions synchronized with the deployed model: same costs, capacities, feasibility rules, initial state, terminal convention, and discounting or averaging convention.
- Never compare an online method to a benchmark that uses different cost units or excludes penalties without labeling the difference.

Baseline reporting integrity:

- Report every baseline and comparator separately. If there are five baseline methods, the result files and reports must show five baseline rows, not one aggregate comparator row.
- For each baseline, record method logic, role category, information timing, data/features used, tuning budget or fixed settings, runtime status, and all primary metrics.
- If one baseline outperforms the others on a metric, identify it by name in the interpretation while keeping all weaker, failed, infeasible, timed-out, or non-run baselines visible in the table.
- If multiple metrics have different winning baselines, state that explicitly instead of implying a single baseline dominated on all metrics.

## Run and Debug Loop

1. Write the initial Python implementation.
2. Run it on the provided data or a minimal representative sample.
3. Fix syntax, data parsing, dependency, solver, or training issues.
4. Confirm that the run completes.
5. Run a quality pilot when method quality is uncertain. Compare to strong baselines and inspect whether the selected technical settings are plausibly strong enough.
6. If the pilot is weak and runtime budget remains, revise the design and rerun the pilot before scaling.
7. If the user-facing `run` is expected to exceed 3 minutes, execute the Run Protocol: smoke test, pilot acceptance check, targeted pilot iterations when needed, runtime estimate, foreground `run` script or command, durable progress/result files, and clear `run` instructions. Do not start the final `run` yourself.
8. For training methods, inspect convergence diagnostics before interpreting final performance: learning curves, validation/evaluation curves, losses, feasibility violations, seed variability, best-versus-last checkpoint behavior, and stopping criteria.
9. Run evaluation trajectories and any required ex-post benchmark or documented fallback benchmark.
10. Inspect whether outputs are reasonable relative to the problem, convergence evidence, and benchmark gaps.
11. If outputs are unreasonable, diagnose whether the issue is data, model assumptions, implementation, solver settings, benchmark construction, reward scaling, state/action design, exploration, optimizer settings, convergence failure, model capacity, batch size, or training budget.
12. Clean the project after smoke/pilot validation: delete smoke outputs, pilot outputs, pilot-only configs, temporary pilot models/checkpoints, scratch logs, failed-trial leftovers, and useless empty folders. Keep only the files needed for the user-facing `run`, documented placeholder directories, plus concise pilot evidence in the workspace-level report.
13. Generate or update the static HTML Project Delivery And Run Manual under the workspace-level `reports/` folder after the code runs, detailed pilot comparison evidence is summarized, and cleanup is complete.
14. Iterate with the user until the code project, run commands, outputs, and manual are stable enough for delivery, or until the report clearly states that the approved budget was insufficient and identifies the best next technical step.

## User Feedback

After implementation, report through the Project Delivery And Run Manual and a concise chat delivery note:

- What method was implemented
- What data was used
- Run status
- For jobs expected to run longer than 3 minutes, smoke status, detailed pilot experiment comparison before cleanup, runtime estimate, exact `run` command, expected terminal progress output, progress/status/checkpoint paths, and what files to send back for analysis
- Run logs and output files: which structured progress file records cost/objective over time, which file records status, and which manifest explains generated files
- Key results
- Baseline-by-baseline results: every baseline method, its definition/status, and its own metrics. Do not summarize baselines as a single aggregate row.
- Convergence status and supporting diagnostics for any training-based method, including whether the run is a smoke test, pilot, or sufficiently trained result
- Per-trajectory benchmark gap summary when evaluation trajectories exist
- Warnings or limitations
- Suggested next improvement if the result is not satisfactory

During later iterations, update the code, rerun the relevant short check, and regenerate the delivery manual whenever commands, files, dependencies, acceptance criteria, or output schemas change.
