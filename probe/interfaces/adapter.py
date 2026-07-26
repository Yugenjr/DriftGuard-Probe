"""Platform Adapter protocol abstractions."""
from typing import Any, Dict, List, Optional, Protocol, runtime_checkable


@runtime_checkable
class PlatformProvider(Protocol):
    """Abstract interface defining required capabilities for any MLOps monitoring adapter.
    
    Platforms like DriftGuard, Arize, WhyLabs, or dummy mocks implement this interface,
    insulating core agents from direct REST, MCP, or database networking calls.
    """

    async def get_model(self, model_id: str) -> Dict[str, Any]:
        """Fetch model telemetry metadata and version details."""
        ...

    async def get_drift_metrics(self, model_id: str, limit: int = 100) -> List[Dict[str, Any]]:
        """Retrieve statistical drift measurement distributions."""
        ...

    async def get_validation_records(self, model_id: str) -> List[Dict[str, Any]]:
        """Retrieve automated validation test executions."""
        ...

    async def get_audit_logs(self, model_id: str, limit: int = 50) -> List[Dict[str, Any]]:
        """Retrieve system operational logs and lifecycle events."""
        ...

    async def get_reports(self, model_id: str) -> List[Dict[str, Any]]:
        """Retrieve existing diagnostic or governance reports."""
        ...

    async def trigger_retraining(self, model_id: str, dataset_path: Optional[str] = None) -> Dict[str, Any]:
        """Dispatch a retraining pipeline execution request."""
        ...
