from typing import Any, Dict, Mapping


SIMULATION_OPTIMIZATION_STAGES = [
    "load config and simulator inputs",
    "build baseline policies",
    "initialize candidate policy class",
    "run smoke simulation",
    "run pilot search with controlled replications",
    "apply acceptance criteria against baselines",
    "run the user-facing search if pilot is credible",
    "evaluate selected candidates on fresh seeds",
    "write progress, status, results, trajectories, and artifact manifest",
]


class SimulationOptimizationLoopContract:
    def run_smoke(self, config: Dict[str, Any]) -> Mapping[str, Any]:
        raise NotImplementedError

    def run_pilot(self, config: Dict[str, Any]) -> Mapping[str, Any]:
        raise NotImplementedError

    def run(self, config: Dict[str, Any]) -> Mapping[str, Any]:
        raise NotImplementedError
