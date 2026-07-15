# Workflow

Creator and maintainer: Xiaotian Liu · xiaotianliu01@gmail.com

## User-Facing Response Style

Before returning any major stage output to the user, apply `references/response_style.md`. Major report information must be written to a detailed, polished, static read-only HTML report, not pasted as a long chat answer. The report must be self-contained and suitable for expert OR or operations review: include modeling scope, data and assumptions, notation, model or method logic, risks, and the technical meaning of the next decision. Avoid generic reader guides, standalone operator-explanation sections, and broad tutorial recaps after the technical material. Use compact tables for non-formula information, recommendation blocks, risk/limitation blocks, indented mathematical definitions, standalone rendered LaTeX equations, and stable review anchors. Do not put input boxes, buttons, forms, clickable choice boxes, comment panels, localStorage state, or other interactive controls in the HTML. User confirmation and choices happen in chat after the HTML report link.

All report section labels, option text, chat prompts, and implementation notes in this workflow must follow the language contract in `references/response_style.md`. Treat the Chinese option labels in examples below as examples only; translate them fully when the user's primary language is not Chinese.

## Formulator Stage

Start by reading `references/formulator.md`. Convert the user request and verified data into a rigorous formulation brief. Include:

- Problem statement in one paragraph
- Data artifacts and formats
- Data loadability and actual observed fields, dimensions, schemas, samples, or metadata
- Multimodal data interpretation and whether each artifact is structured model input or high-dimensional feature input
- Decision variables
- Objective function candidate
- Constraints and business rules
- Known parameters and uncertain parameters
- Assumptions that are safe to make
- Missing required data or missing rules for generating synthetic data
- Missing information that blocks modeling
- Contradictions, infeasible requirements, or trivial cases

Use `scripts/data_probe.py` when raw files or directories need preloading. Do not rely only on user-described file contents when files are available to inspect.

If critical data cannot be loaded, if required data are absent, if the data contradicts the prompt, or if essential modeling information is missing, ask focused questions before running the three branches.

If the task requires generated or simulated data but the user has not specified the generating process, ask for the missing process before modeling. Common blockers include demand distributions, arrival processes, service-time distributions, lead-time distributions, network disruption probabilities, transition dynamics, reward definitions, noise models, scenario probabilities, and correlations among random variables.

Only proceed with assumptions when they are non-critical, clearly labeled, and do not determine the main method choice or feasibility of the model.

## Formulation Confirmation Gate

After the formulator stage, generate a static HTML Formulation Confirmation Report and stop. Do not start analyzer, optimizer, or trainer exploration until the user confirms in chat that the problem interpretation, data analysis, and mathematical model are correct.

The HTML report must use this polished structure, applying `references/response_style.md`:

```text
Formulation Confirmation Report

Executive Summary
...

Problem Understanding
| Item | Interpretation |
|---|---|
| Operational decision | ... |
| Horizon and timing | ... |
| Objective | ... |
| Business rules | ... |

Data Inventory
| Artifact / Source | Status | Observed structure | Model role |
|---|---|---|---|
| ... | Confirmed / Missing / Assumed | ... | ... |

Mathematical Model

Sets and indices:
  - ...

Parameters:
  - ...

Decision variables:
  - ...

Objective:

$$
...
$$

Constraints and state transitions:

$$
\begin{aligned}
...
\end{aligned}
$$

Use indentation for notation and explanations. Do not use a Markdown table for mathematical model design, cost formulas, objectives, constraints, or state transitions.

Assumptions And Gaps
| Type | Item | Consequence |
|---|---|---|
| Confirmed | ... | ... |
| Assumed | ... | ... |
| Missing | ... | ... |

Decision Needed
List the available text replies only; do not include any form controls or clickable choice boxes.

Options:
- Option A: Confirm the formulation
- Option B: Revise the formulation
- Other: add data / pause
```

After creating the HTML report, return only a compact chat message like:

```text
**Decision Needed**
Formulation Confirmation Report generated: <path-to-html>
- Option A: Confirm the formulation; I will proceed to analytics / optimization / training method exploration.
- Option B: Revise the formulation; I will update the brief and return a revised report.
- Other: add data or pause; I will wait for your input.
```

If the user provides corrections, update the formulation and return the revised static HTML Formulation Confirmation Report. Repeat until the formulation is confirmed.

## Parallel Branching

Only after the user confirms the formulation, run method exploration. When multi-agent or subagent tools are available, run three independent agents in parallel:

- `analyzer`: explores analytical, theoretical, and heuristic methods.
- `optimizer`: explores solver-based mathematical optimization.
- `trainer`: explores data-driven, ML, neural network, simulation, and reinforcement learning methods.

Pass the same formulator output to all three agents. Include only branch-specific reference instructions:

- For analyzer, attach or instruct reading `references/analyzer.md`.
- For optimizer, attach or instruct reading `references/optimizer.md`.
- For trainer, attach or instruct reading `references/trainer.md`.

Do not share branch results among the three agents before reviewer synthesis. This preserves independent reasoning.

If parallel execution is unavailable, run the three branches sequentially and label outputs clearly as independent branch results.

Do not constrain the method exploration to simplified policies just because they are easy to implement. If the confirmed formulation is an MDP, stochastic dynamic program, simulator-backed sequential decision problem, or complex nonconvex stochastic control problem, require the training branch to examine strong learned policy/value methods such as PPO, actor-critic, fitted value iteration, tree/regression-based policies, or other parametric approximators unless the user explicitly forbids black-box models. Hand-designed policy forms must be justified by mathematical structure, known OR theory, or planned empirical rejection tests; otherwise they are weak baselines, not primary recommendations.

Method exploration must be solution-quality-first. Every branch should identify what would count as a good practitioner-facing result: strong baselines or bounds, target improvement or gap, feasibility requirements, runtime budget, and failure conditions. Do not treat a method as recommended merely because it can produce output. Baselines must be fair, competent comparators rather than deliberately weak hurdles: if a heuristic, rule, simulation-search policy, myopic optimizer, or simple model has material parameters, plan a reasonable tuning procedure under the same information timing and a comparable or explicitly capped budget. For training or simulation methods, require a credible tuning and model-size plan, a pilot acceptance check, and a pre-declared fallback method before any large run. Any branch that proposes smoke tests, pilots, or training runs must also plan pre-delivery cleanup: temporary scratch outputs, copied example data, fake/demo datasets, failed-run leftovers, irrelevant template files, and useless empty folders must be removed or converted into documented minimal test datasets before the project is given to the user.

For any fallback attached to a training-based method, require a guarantee statement. The statement must identify the strongest support available: solver certificate or optimality gap, feasibility by construction, valid bound relation, approximation or dominance property, incumbent-safe switching rule, or statistically validated performance interval. If the fallback is empirical only, the branch must say why no stronger guaranteed fallback fits the confirmed formulation and what evidence would make the empirical fallback acceptable.

## Benchmark Taxonomy And Promotion Rule

During method selection, keep the comparison roles explicit:

- Primary candidates: methods that could reasonably be recommended as the main deployable solution under the confirmed formulation.
- Fallback candidates: deployable methods that may be selected when the primary is blocked by dependencies, runtime, licenses, interpretability requirements, or pilot evidence.
- Classical baselines: literature-standard, current-practice, simple-rule, naive, myopic, seasonal, base-stock, dispatching, rolling-average, sample-average, lower-bound, relaxation, or hindsight benchmarks whose purpose is to calibrate difficulty and prevent weak recommendations.
- Warm starts or tuning components: methods that initialize, guide, or tune a stronger method, but are not being evaluated as standalone deployable policies unless explicitly promoted.

A method may be called a baseline only when it is materially simpler or methodologically different from the primary candidate, or when it is a recognized benchmark in the relevant literature or industry practice. Do not hide a sophisticated method in the baseline set merely because it is convenient for scoring. If a "baseline" uses nearly the same feature set, comparable model capacity, the same policy class or learning paradigm, or is expected to outperform the proposed primary method, reclassify it as a primary candidate, fallback candidate, or peer challenger. The Method Selection Report must state this reclassification and compare it in the main candidate table. If the user explicitly asks to benchmark against a strong production model, label it as "incumbent / peer benchmark" rather than a simple baseline.

When a report contains benchmark or result values, baseline reporting must be explicit rather than aggregated. List each baseline method separately with its definition, data/features, settings, status, and metrics. Do not use the top result among many baseline methods as a single baseline number. Do not add an aggregate baseline row; explain which visible baseline row performed better when interpreting a metric.

## Performance-Ceiling Frontier

Before recommending a method, build a method frontier that compares expected performance ceiling against implementation effort and deployment risk. This is mandatory for complex OR tasks where a simple heuristic can run quickly but has a low ceiling.

The frontier must include:

- At least one high-ceiling solver or mathematical programming candidate when the formulation contains hard constraints, nonlinear production, clearing functions, scenario recourse, or finite-horizon dynamics. Examples include dynamic MILP, rolling-horizon MILP/MPC, PWL linearization of nonlinear clearing functions, stochastic programming, decomposition, and valid lower-bound or hindsight models.
- At least one high-ceiling learned or approximate dynamic programming candidate when the formulation is an MDP, stochastic dynamic program, simulator-backed sequential decision process, or repeated production-control problem. Examples include PPO, actor-critic, MAPPO/RMAPPO, fitted value iteration, fitted Q iteration, residual RL around a strong baseline, and neural or tree value approximation.
- Any supplied codebase evidence that raises feasibility, such as existing environment wrappers, training scripts, pretrained models, solver baselines, PWL linearization utilities, or benchmark outputs. Treat these artifacts as important method evidence and cite the relevant files in the internal reasoning and report.
- Candidate reusable assets discovered from `assets/asset_registry.md` and every `assets/*/asset_manifest.json`, including user-added custom assets. Treat a custom asset as feasibility evidence when its manifest and guide fit the confirmed formulation and enforce industrial acceptance criteria.
- The best simple heuristic, current rule, base-stock policy, or random/search-tuned policy as a baseline or warm start. Do not let it become primary without a written reason that the higher-ceiling methods are infeasible, unnecessary for the user's acceptance target, or dominated under pilot evidence.
- Any strong peer benchmark or incumbent model that is not materially simpler than the primary candidate. Label it as a peer candidate or incumbent benchmark, not as a simple baseline, and allow it to become the recommended method when its expected quality, robustness, and deployability dominate.

For each frontier candidate, state:

- Performance ceiling: optimality, approximation power, adaptivity, ability to exploit nonlinear dynamics, or ability to close a benchmark gap.
- Implementation effort: data engineering, solver/training complexity, dependency and license burden, debugging risk, and required runtime.
- Evidence available now: existing files, known algorithms, formulation structure, pilot results, solver availability, or missing dependencies.
- Asset support: selected built-in or custom asset path, contracts it contributes, and acceptance criteria it enforces.
- What would make the candidate fail: infeasibility, scaling, non-convergence, license denial, poor pilot quality, or inability to beat strong baselines.
- For training-based candidates, which fallback method would be selected or recommended if training is unstable, seed-sensitive, dependency-blocked, or still below target after the allowed redesign attempts.
- For training-based candidates, the fallback guarantee level, scope, certificate/evidence, and trigger for selecting the fallback instead of the learned model.

Random search, differential evolution over a few policy parameters, or ad hoc heuristic tuning can be a useful diagnostic, baseline, warm start, or subroutine. It should be labeled low-ceiling when it does not materially expand the policy class. It is not a sufficient final strategy for a production-scale sequential OR problem unless the report explicitly justifies why a higher-ceiling method is not worth pursuing.

## Specialist Agent Prompt Template

Use this structure for each branch:

```text
You are the {analyzer|optimizer|trainer} specialist for an OR/math modeling task.
Use the formulator output below and your branch reference instructions.
Return a rigorous candidate solution, not final user-facing advice.

Formulator output:
{brief}

Required output:
1. Problem assumptions
2. Candidate methods or policies within this branch
3. Method summary for each suitable candidate
4. Mathematical formulation or method principle
5. Pros and cons for each suitable candidate
6. Data requirements
7. Dependencies and license risks
8. Implementation route
9. Complexity and scalability notes
10. Failure modes and risks
11. Suitable and unsuitable scenarios
12. Rigor check: what justifies the policy/model class, and what would make it invalid
13. Performance-ceiling versus implementation-effort assessment, including whether the method is high-ceiling, medium-ceiling, or baseline-only for the confirmed formulation
14. Higher-ceiling alternatives in this branch that were considered and why they are selected, deferred, or rejected
15. Benchmark taxonomy: which comparators are classical baselines, lower bounds, incumbent / peer benchmarks, fallbacks, warm starts, or primary candidates; explain any promotion of a strong "baseline" into a candidate method
16. Quality target: strong baselines, desired improvement or optimality gap, feasibility threshold, runtime budget, failure criteria, and fallback trigger
17. For training-based methods, tuning and model-size plan: architecture or policy class, batch/rollout/sample/scenario settings, tuning budget, and why settings are not arbitrary small defaults
18. For training-based methods, convergence diagnostics plan: monitored metrics, stopping rule, plots/tables to produce, seed variability, and non-convergence warning signs
19. For training-based methods, fallback plan: fallback method, why it is reliable, implementation readiness, dependencies, evaluation protocol, acceptance threshold, and selection rule
20. For training-based methods, fallback guarantee: guarantee type, guarantee scope, proof/certificate/evidence, and whether the fallback is deployable as the selected method or only usable as a diagnostic comparator
21. Pilot acceptance check: the reduced run evidence required before recommending the user-facing `run`, what targeted revisions or peer-candidate tests should occur if the pilot is weak, and how many iterations are reasonable under the runtime budget
22. Run logs and output files: structured progress metrics, cost/objective over time, status files, model/checkpoint files, fallback-selection records, result summaries, and artifact manifest
23. Pre-delivery cleanup plan: delete smoke/pilot outputs, pilot-only configs, scratch files, failed-run leftovers, copied examples, cache files, and useless empty folders before delivery; keep only files needed for `run`, documented placeholder directories, and any explicitly requested minimal test dataset
24. Relevant built-in or custom assets considered: asset path, why it fits or does not fit, contracts reused, and acceptance criteria required
```

## Review and User Choice

After all branches return, read `references/reviewer.md`. The reviewer compares all candidates, identifies invalid or weak assumptions, and recommends one or more methods. The main thread must then study the reviewer synthesis carefully and respect it when generating the user-facing Method Selection Report.

Before returning the report, run a consistency audit:

- The highest score in the cross-method table must match the branch described as highest-ranked unless an override rationale is written in the report.
- The branch conclusion callouts, recommendation block, and recommended-method technical-details section must name the same primary method.
- Fallback methods must be clearly secondary and must not be described as the selected method.
- For training-based recommendations, the fallback method and fallback trigger must be visible and technically credible; a do-nothing diagnostic baseline is not enough when stronger feasible fallbacks exist.
- For training-based recommendations, the fallback guarantee statement, scope, and evidence must be visible. A fallback with no feasibility, bound, incumbent-safety, or statistical guarantee must be labeled empirical-only.
- If the main thread changes or challenges the reviewer recommendation, the report must explicitly state why; do not silently blur or rewrite the reviewer conclusion.
- The primary method must be selected for expected solution quality under the confirmed model, not merely for ease of implementation. If a simpler heuristic is selected over PPO, actor-critic, fitted value iteration, or another stronger learned/optimization method, the report must justify why the simpler method is sufficient or why the stronger method is infeasible.
- Any pre-specified heuristic or parametric policy form must include a rigor check. If there is no proof, structural argument, approximation argument, or empirical validation plan, label it as a baseline rather than a recommended primary method.
- The report must audit whether each "baseline" is truly a classical/simple/literature benchmark. If a comparator is feature-rich, highly tuned, comparable in complexity to the primary method, or likely to dominate the primary method, promote it to the main method comparison and consider recommending it.
- If the report includes any result values, it must list every baseline result separately. It must not report only an aggregate baseline value when multiple baselines were evaluated or configured.
- If random search or parameter tuning is part of the recommendation, the report must state whether it is only a baseline/warm-start/tuning component or the primary algorithm. If it is primary, the report must include the explicit rejection evidence for higher-ceiling dynamic programming, solver, RL, ADP, or hybrid methods.
- If the report proposes training, solver, simulation, or pilot runs, it must include a pre-delivery cleanup expectation: delete unused example data, fake/demo datasets, stale scratch outputs, failed-run leftovers, cache files, duplicate logs, copied template outputs, and useless empty folders unless they are explicitly documented minimal test datasets, placeholder directories, or canonical run records.

Generate a static HTML Method Selection Report and stop. Do not prepare or run deployment until the user selects a method, confirms the recommendation, or resolves objections in chat.

The HTML report must use this polished structure, applying `references/response_style.md`:

```text
Method Selection Report

Confirmed Formulation Snapshot
| Item | Summary |
|---|---|
| Problem | ... |
| Data | ... |
| Objective and constraints | ... |
| Important assumptions | ... |

Analytics Methods
| Method | Principle | Pros | Cons | Fit |
|---|---|---|---|---|
| ... | ... | ... | ... | Suitable / Limited / Not recommended |

Analytics branch conclusion:
...

Optimization Methods
| Method | Model / solver route | Pros | Cons | Fit |
|---|---|---|---|---|
| ... | ... | ... | ... | Suitable / Limited / Not recommended |

Optimization branch conclusion:
...

Training / Simulation / Learning Methods
| Method | Target | Convergence diagnostics | Pros | Cons | Fit |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | Suitable / Limited / Not recommended |

Training branch conclusion:
...

Performance-Ceiling / Implementation-Effort Frontier
| Candidate | Branch | Expected ceiling | Implementation effort | Existing evidence | Primary / Fallback / Baseline / Reject |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |

Recommended Method Technical Details
Principle: ...
State representation: ...
Action representation: ...
Transition mechanics: ...
Update equation or objective:

$$
...
$$

Convergence or stopping criterion: ...
Convergence diagnostics to report: ...
Acceptance target and review rule: ...
Tuning and model-size plan: ...
Pilot acceptance check and redesign rule: ...
Run logs and output files: ...
Policy extraction: ...
Evaluation protocol: ...
Benchmark design: ...
Implementation complexity and validity limits: ...
Rigor check: ...

Cross-Method Comparison
| Criterion | Analytics | Optimization | Training |
|---|---|---|---|
| Correctness | ... | ... | ... |
| Data compatibility | ... | ... | ... |
| Implementation effort | ... | ... | ... |
| Performance ceiling | ... | ... | ... |
| Scalability | ... | ... | ... |
| Explainability | ... | ... | ... |
| Convergence observability | ... | ... | ... |
| Hyperparameter / design rigor | ... | ... | ... |
| Expected policy quality | ... | ... | ... |
| Run logs / output files | ... | ... | ... |
| Main risks | ... | ... | ... |

Recommendation
Primary: ...
Fallback: ...
Reason: ...

Decision Needed
List the available text replies only; do not include any form controls or clickable choice boxes.

Options:
- Option A: Use the recommended method
- Option B: Use the fallback method
- Other: revise / continue exploration
```

After creating the HTML report, return only a compact chat message like:

```text
**Decision Needed**
Method Selection Report generated: <path-to-html>
- Option A: Use the recommended method; I will proceed to deployment planning.
- Option B: Use the fallback method; I will design deployment around the fallback.
- Other: revise / continue exploration; I will update the method set from your feedback.
```

## Deployment and Feedback

After the user selects a method, read `references/deployment.md`. First inspect the relevant deployment environment for the selected method, create an implementation plan grounded in that observed environment, and run a pre-deployment reviewer check against the selected formulation, method, environment, and plan. Generate a static HTML Deployment Confirmation Report and stop. Do not write final deployment code, run solvers, generate training runs, or produce final results until the user confirms the implementation plan in chat.

The environment survey must be method-specific. Check the programming runtime, package availability and versions, solver availability, hardware or accelerator availability when relevant, writable paths, external-service/network needs, and license/install risks. If conda, mamba, or micromamba is available, enumerate user environments and inspect plausible non-default Python environments before declaring a dependency missing; another conda environment may already contain the required solver, modeling package, RL framework, GPU stack, or data reader. For example, an RL method should report Python and RL/training libraries plus GPU/CUDA readiness if relevant; an MILP method should report modeling packages and solver/license readiness; a spreadsheet method should report workbook-reading and output dependencies. Do not clutter the report with irrelevant machine details, but do report missing capabilities that affect deployment. Missing packages, solvers, licenses, or accelerators must not be used as a silent reason to discard a high-ceiling method; list them as install/license actions, ask the user whether to approve installation or license setup, and only move to a faithful fallback if the user declines or the approved setup fails.

The HTML report must use this polished structure, applying `references/response_style.md`:

```text
Deployment Confirmation Report

Selected Method
| Item | Description |
|---|---|
| Method | ... |
| Reason for selection | ... |
| Confirmed model scope | ... |

Implementation Plan
| Workstream | Plan | Output |
|---|---|---|
| Data loading / preprocessing | ... | ... |
| Core algorithm | ... | ... |
| Hyperparameter / design tuning | ... | ... |
| Acceptance criteria and baseline target | ... | ... |
| Run logs / output files | ... | ... |
| Test run and runtime estimate | ... | ... |
| Run instructions | ... | ... |
| Training convergence monitoring | ... | ... |
| Evaluation | ... | ... |
| Benchmarks | ... | ... |
| Output files | ... | ... |

Environment Survey
| Area | Observed status | Deployment implication |
|---|---|---|
| Runtime | ... | ... |
| Key packages / solvers | ... | ... |
| Hardware / accelerator | ... | ... |
| Filesystem / outputs | ... | ... |
| License / install risk | ... | ... |

Dependency Action Plan
| Missing capability | Why it matters | Proposed install / license action | User approval needed | Fallback if declined or failed |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

Reviewer Check
Status: Pass / Needs Revision
Reason: ...

| Check | Result | Notes |
|---|---|---|
| Match to formulation | ... | ... |
| Objective and constraints | ... | ... |
| Data compatibility | ... | ... |
| Environment readiness | ... | ... |
| Dependencies and license | ... | ... |
| Run readiness | ... | ... |
| Pilot acceptance check | ... | ... |
| Tuning and model-size rationale | ... | ... |
| Run logs and output files | ... | ... |
| Training convergence observability | ... | ... |
| Risks and mitigations | ... | ... |

Decision Needed
List the available text replies only; do not include any form controls or clickable choice boxes.

Options:
- Option A: Approve deployment
- Option B: Revise the plan
- Other: pause / add requirements
```

After creating the HTML report, return only a compact chat message like:

```text
**Decision Needed**
Deployment Confirmation Report generated: <path-to-html>
- Option A: Approve deployment; I will build the delivery-ready project, run smoke and pilot validation, clean the project, and generate the project delivery manual.
- Option B: Revise the plan; I will update the implementation plan and return a revised deployment brief.
- Other: pause or add requirements; I will stop before code or solver execution.
```

If the user requests changes, revise the implementation plan and repeat the static HTML Deployment Confirmation Report. After user confirmation, implement a delivery-ready code project rather than a loose script or one-off result. If the approved method requires missing dependencies and the user has approved installation or license setup, attempt that setup first through the normal execution-environment approval path; if it fails, report the failure and ask whether to retry, provide credentials/license, use an installed equivalent, or switch to the closest faithful fallback. The project must contain the agreed method code, concise configuration files, foreground `run` scripts, result-collection logic, structured run records, and readable module boundaries. Keep the folder layout easy for the user to understand, with a small number of obvious directories such as `configs/`, `data/`, `src/`, `scripts/`, `runs/`, and `docs/` when useful. Do not create a `reports/` folder inside the generated code project; deployment-generated HTML reports go under the workspace-level `reports/` folder.

Generated code must be maintainable by the user. Include module docstrings and block-level comments throughout the code, not only at file headers. Explain math, solver variables, constraint blocks, Big-M or bound choices, state/action/reward logic, scenario generation, unit conversions, baseline definitions, fallback triggers, feasibility repair, run-record schemas, and dependency/license branches. Comments should state why the block exists, what invariant it protects, and what a user can safely modify; avoid comments that merely restate assignments.

Generated configuration files must explain user-tunable parameters where the user edits them. Prefer YAML/TOML or another comment-capable format for new configs. If JSON is unavoidable, include a commented YAML/TOML template or concise config guide next to it, and point the user to that commented source.

Run smoke and pilot checks yourself before delivery. Smoke only verifies that the code path starts, writes output files, and handles dependencies. Pilot checks method quality against baselines and acceptance criteria. Pilot comparisons must evaluate competent baseline implementations: tune material baseline parameters when feasible, preserve the baseline tuning record, and keep baseline information timing consistent with the primary method. If the pilot is weak and approved runtime remains, iterate a few times on the most likely cause, such as feature leakage, baseline logic, hyperparameters, model capacity, reward/objective scaling, normalization, action representation, benchmark logic, solver settings, scenario count, seed count, or training budget. If a very similar peer deployment candidate is likely to dominate the current configuration, test it before packaging the project.

For any method expected to exceed 3 minutes, do not start the final `run` yourself. Prepare a concise foreground `.sh` script or exact command for the user to run locally. The command-line output must be operator-friendly and concise: print phase, iteration/epoch/timestep, elapsed time, current objective/loss/reward/gap, feasibility or violation diagnostics, current best metric, best checkpoint/model path when training is involved, and output paths when relevant. Save durable progress/status/results in a small number of files. For training methods, the final evaluation must load the best validation/evaluation checkpoint or model by default, not the last checkpoint, unless the report explicitly justifies another choice. Stop after giving the user the smoke status, pilot evidence summary, estimated runtime, exact `run` command, output paths, and instructions to ask for analysis after `run` completes.

Before delivery, clean the generated project: delete smoke outputs, pilot outputs, pilot-only configs, temporary pilot models/checkpoints, scratch logs, failed-run leftovers, copied examples, fake/demo data, cache files, and useless empty folders. Keep only the source/config/scripts needed for the user-facing `run`, real data references, explicitly requested minimal test datasets, documented placeholder directories, and concise output templates.

After cleanup, generate a static read-only HTML Project Delivery And Run Manual under the workspace-level `reports/` folder and return its path in chat. This manual is the deployment deliverable, not a cosmetic note. It must explain the project structure, every important file and folder, each script/entrypoint, configuration knobs, dependencies, exact `run` command, expected terminal output, run records, result files, checkpoints/models, acceptance criteria, detailed pilot evidence before cleanup, known limitations, and the iteration protocol for user feedback or completed `run` results. The pilot evidence must use the required result-comparison format from `references/response_style.md`: for Chinese reports, columns are `实验设置 | 方法 | 结果 | 解释/讨论`. For every pilot condition that affected the final configuration, show the primary method and every baseline/peer method as separate rows with aligned metrics, feasibility/convergence status, runtime/budget, and the decision; include weak, failed, or superseded rows when they explain tuning. Continue iterating with the user after delivery: when they report errors or provide run outputs, inspect saved output files, fix code or configuration, rerun short checks when needed, regenerate the delivery manual when materially changed, and repeat until development is finalized.

For all substantial code runs, write tidy structured run logs: cost/objective or reward over time, evaluation cost, feasibility diagnostics, loss/gap where relevant, elapsed time, status, current best metric, selected best checkpoint/model path, and a concise manifest explaining the main files. For training-based methods, produce convergence logs and plots before interpreting performance: raw training logs, learning/evaluation curves, best-versus-last checkpoint/model behavior, relevant loss curves, feasibility-violation curves, seed variability, stopping criteria, and a convergence status label. When the user later requests final analysis after `run` completes, read the saved logs/models/results and produce a final results analysis or final technical document as requested. Reflect on whether results are reasonable; if not, revise the model or implementation and rerun short checks while budget remains.

When the task includes evaluation scenarios, samples, simulations, or historical trajectories, evaluate the selected method on each trajectory and, when computationally reasonable, compute a trajectory-level ex-post optimal benchmark. This benchmark should use the realized trajectory with future information and should be labeled as a clairvoyant lower bound or hindsight optimum, not as an implementable policy. Report absolute and relative gaps for each trajectory and aggregate summaries across trajectories. If the exact ex-post benchmark is not tractable, document the reason and use a valid relaxation, lower bound, or clearly defined benchmark with its own visible result row.

For every deployment, delivery, final results, or final technical report that discusses baselines, include baseline-by-baseline definitions and results. Use the required four-column result-comparison table for result-bearing comparisons. Interpret metric winners by pointing to the visible baseline rows; do not create a single aggregate baseline result.

## Archive

When the user asks for a final summary or final technical document, read `references/archive.md` and package code, data, results, requirements, trajectory benchmark outputs, prior finalized stage reports, the project delivery manual, and the final technical report in one folder. Default to a rendered PDF technical document unless the user requests another format. The report is part of the solution, not a cosmetic wrapper: it must combine the confirmed formulation, method-selection rationale, deployment plan, final project structure, results from the user's `run`, benchmark evidence, limitations, and reproducibility steps in enough detail for a manager or colleague to evaluate and reuse the work.
