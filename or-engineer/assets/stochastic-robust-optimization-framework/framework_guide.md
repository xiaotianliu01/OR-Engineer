# Stochastic And Robust Optimization Framework Guide

Creator and maintainer: Xiaotian Liu · xiaotianliu01@gmail.com

This asset is a general scaffold for optimization under uncertainty. It is intentionally not runnable until task-specific uncertainty models, scenarios, robust sets, recourse structure, and evaluation logic are implemented.

## Industrial Implementation Contract

Do not use this asset to create a tiny in-sample scenario toy or a deterministic model with uncertainty labels. A serious deployment must document uncertainty sources, information timing, dependence, scenario probabilities or ambiguity sets, in-sample versus out-of-sample separation, common-random-number comparison when useful, service/risk metrics, sensitivity to scenario count or risk settings, and feasibility under held-out scenarios. Final claims must be based on out-of-sample evaluation.

Use it for:

- sample average approximation,
- two-stage or multistage stochastic programming,
- scenario trees,
- chance constraints,
- robust optimization,
- distributionally robust optimization,
- CVaR and risk-aware objectives,
- service-level constrained optimization,
- out-of-sample policy or solution evaluation.

Adaptation flow:

1. Identify uncertain parameters, timing, observation process, and decision stages.
2. Choose stochastic, robust, or DRO model family.
3. Implement uncertainty model and scenario generation in `uncertainty/` and `scenarios/`.
4. Implement deterministic equivalent or robust counterpart in `models/`.
5. Implement risk and service-level metrics in `risk/`.
6. Evaluate in-sample and out-of-sample performance in `evaluation/`.
7. Save scenario manifests, solution files, sample metrics, and benchmark gaps under `run_records/`.

Minimum acceptance criteria:

- Separate training or optimization scenarios from out-of-sample evaluation scenarios.
- Report feasibility, objective, service level, and risk metrics out of sample.
- Use common random numbers for fair stochastic comparison when possible.
- Report sensitivity to scenario count, ambiguity radius, chance level, or risk weight when those settings drive decisions.
