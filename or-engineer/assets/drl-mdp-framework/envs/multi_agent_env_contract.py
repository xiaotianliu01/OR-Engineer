"""General multi-agent MDP environment contract."""

from typing import Any, Dict, Protocol, Tuple


class MultiAgentEnv(Protocol):
    agents: list[str]
    observation_spaces: Dict[str, Any]
    action_spaces: Dict[str, Any]
    state_space: Any | None

    def reset(self, *, seed: int | None = None, options: Dict[str, Any] | None = None) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """Return per-agent observations and info."""
        ...

    def step(
        self,
        actions: Dict[str, Any],
    ) -> Tuple[Dict[str, Any], Dict[str, float], Dict[str, bool], Dict[str, bool], Dict[str, Any]]:
        """Return obs, rewards, terminated flags, truncated flags, and info."""
        ...

    def global_state(self) -> Any:
        """Return centralized-training state when available."""
        ...


REQUIRED_MULTI_AGENT_NOTES = [
    "agent identities and symmetry",
    "shared or individual rewards",
    "centralized-training state",
    "decentralized-execution observations",
    "joint-action feasibility",
    "coordination or communication assumptions",
    "agent masks and unavailable actions",
]

