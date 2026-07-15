"""Evaluation loop contract."""

EVALUATION_STEPS = [
    "load selected best policy checkpoint by default",
    "load fallback policy or method when evaluating fallback readiness or activation",
    "freeze stochastic policy or define deterministic evaluation mode",
    "run fixed evaluation seeds or trajectories",
    "compare against strong baselines and lower bounds when available",
    "record cost/reward components and constraint diagnostics",
    "report aggregate statistics and seed variability",
    "report fallback metric and selected method when fallback activation is possible",
    "export per-trajectory or per-episode results",
]


REQUIRED_EVAL_FIELDS = [
    "case_id",
    "seed",
    "episode",
    "policy_name",
    "total_reward_or_cost",
    "baseline_reward_or_cost",
    "gap_abs",
    "gap_pct",
    "feasibility_violation",
    "termination_status",
    "checkpoint_path",
    "checkpoint_selection_reason",
    "fallback_method_id",
    "fallback_activation_reason",
    "selected_method_for_handoff",
]
