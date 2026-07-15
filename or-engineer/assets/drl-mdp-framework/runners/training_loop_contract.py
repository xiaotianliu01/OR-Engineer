"""Training loop contract.

This scaffold describes what a task-specific training loop must do. It is not a
complete runner until algorithm, environment, networks, and data interfaces are
implemented.
"""

TRAINING_LOOP_STEPS = [
    "load frozen run_config",
    "set deterministic seeds where feasible",
    "construct environment and evaluation environment",
    "construct or load the declared fallback policy or fallback method",
    "construct algorithm and networks",
    "run smoke test through the same code path as `run` training",
    "collect rollouts or replay data",
    "run algorithm updates",
    "evaluate on fixed seeds or scenarios at intervals",
    "append progress metrics",
    "save periodic checkpoints and save/update best policy when evaluation metric improves",
    "load best checkpoint for final evaluation, not the last checkpoint unless it is best",
    "update status file",
    "if pilot is weak and budget remains, run targeted redesign attempts on high-impact settings",
    "if redesign attempts fail or learning remains unstable, evaluate and activate the declared fallback when it meets its acceptance threshold",
    "apply pilot acceptance check before recommending the user-facing run",
]


REQUIRED_TRAIN_METRICS = [
    "train_reward_or_cost",
    "eval_reward_or_cost",
    "best_eval_metric",
    "best_checkpoint_path",
    "selected_checkpoint_path",
    "fallback_method_id",
    "fallback_metric",
    "fallback_activated",
    "fallback_activation_reason",
    "selected_method_for_handoff",
    "feasibility_violation",
    "policy_loss",
    "value_or_q_loss",
    "entropy_or_exploration_metric",
    "learning_rate",
    "gradient_norm",
    "elapsed_seconds",
]
