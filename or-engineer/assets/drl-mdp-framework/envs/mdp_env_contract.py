"""General MDP environment contract.

Replace this scaffold with a task-specific implementation. It may wrap
Gymnasium, a custom simulator, a discrete-event simulator, or a mathematical
transition function.
"""

from typing import Any, Dict, Protocol, Tuple


class MDPEnv(Protocol):
    observation_space: Any
    action_space: Any

    def reset(self, *, seed: int | None = None, options: Dict[str, Any] | None = None) -> Tuple[Any, Dict[str, Any]]:
        """Return initial observation and info."""
        ...

    def step(self, action: Any) -> Tuple[Any, float, bool, bool, Dict[str, Any]]:
        """Return observation, reward, terminated, truncated, and info."""
        ...

    def render(self) -> Any:
        ...

    def close(self) -> None:
        ...


REQUIRED_ENV_NOTES = [
    "state variables and Markov sufficiency",
    "observation variables and partial observability",
    "action variables, bounds, discreteness, and feasibility repair",
    "transition timing and stochastic process",
    "reward or cost sign convention and scaling",
    "termination and truncation",
    "hard constraints and violation diagnostics",
    "baseline policy hooks",
]

