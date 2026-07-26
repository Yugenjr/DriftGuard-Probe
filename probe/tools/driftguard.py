"""Platform monitoring tools wrapping PlatformProvider adapter methods."""
from typing import Any, Dict
from .base import BaseTool
from ..adapters.driftguard.client import DriftGuardRESTClient


class GetModelTool(BaseTool):
    """Tool extracting model architectural versioning and status details."""
    @property
    def name(self) -> str:
        return "get_model"

    @property
    def description(self) -> str:
        return "Fetch deployment status, version lineage, and structural metadata for a target model ID."

    @property
    def input_schema(self) -> Dict[str, Any]:
        return {"type": "object", "properties": {"model_id": {"type": "string"}}, "required": ["model_id"]}

    async def invoke(self, **kwargs: Any) -> Dict[str, Any]:
        provider = self.provider or DriftGuardRESTClient()
        return await provider.get_model(kwargs["model_id"])


class GetMetricsTool(BaseTool):
    """Tool extracting recent time-series telemetry distributions."""
    @property
    def name(self) -> str:
        return "get_metrics"

    @property
    def description(self) -> str:
        return "Retrieve historical latency, error rate, or precision operational telemetry curves."

    @property
    def input_schema(self) -> Dict[str, Any]:
        return {"type": "object", "properties": {"model_id": {"type": "string"}}, "required": ["model_id"]}

    async def invoke(self, **kwargs: Any) -> Dict[str, Any]:
        provider = self.provider or DriftGuardRESTClient()
        return {"metrics": await provider.get_drift_metrics(kwargs["model_id"])}


class GetDriftTool(BaseTool):
    """Tool obtaining feature drift statistics and distance scores."""
    @property
    def name(self) -> str:
        return "get_drift"

    @property
    def description(self) -> str:
        return "Retrieve calculated statistical feature drift indices (ADWIN, KS, Wasserstein)."

    @property
    def input_schema(self) -> Dict[str, Any]:
        return {"type": "object", "properties": {"model_id": {"type": "string"}}, "required": ["model_id"]}

    async def invoke(self, **kwargs: Any) -> Dict[str, Any]:
        provider = self.provider or DriftGuardRESTClient()
        return {"drift_records": await provider.get_drift_metrics(kwargs["model_id"])}


class GetValidationTool(BaseTool):
    """Tool checking automated validation test suite runs."""
    @property
    def name(self) -> str:
        return "get_validation"

    @property
    def description(self) -> str:
        return "Verify whether input schema data validation rules succeeded or failed."

    @property
    def input_schema(self) -> Dict[str, Any]:
        return {"type": "object", "properties": {"model_id": {"type": "string"}}, "required": ["model_id"]}

    async def invoke(self, **kwargs: Any) -> Dict[str, Any]:
        provider = self.provider or DriftGuardRESTClient()
        return {"validation_checks": await provider.get_validation_records(kwargs["model_id"])}


class GetAuditTool(BaseTool):
    """Tool gathering audit trail logs and historical engineer interventions."""
    @property
    def name(self) -> str:
        return "get_audit"

    @property
    def description(self) -> str:
        return "Extract chronological operational logs, threshold modifications, and deploy history."

    @property
    def input_schema(self) -> Dict[str, Any]:
        return {"type": "object", "properties": {"model_id": {"type": "string"}}, "required": ["model_id"]}

    async def invoke(self, **kwargs: Any) -> Dict[str, Any]:
        provider = self.provider or DriftGuardRESTClient()
        return {"audit_logs": await provider.get_audit_logs(kwargs["model_id"])}


class TriggerRetrainTool(BaseTool):
    """Tool dispatching model retraining jobs via platform adapter."""
    @property
    def name(self) -> str:
        return "trigger_retrain"

    @property
    def description(self) -> str:
        return "Initiate an automated training pipeline run on new validated target datasets."

    @property
    def input_schema(self) -> Dict[str, Any]:
        return {"type": "object", "properties": {"model_id": {"type": "string"}}, "required": ["model_id"]}

    async def invoke(self, **kwargs: Any) -> Dict[str, Any]:
        provider = self.provider or DriftGuardRESTClient()
        return await provider.trigger_retraining(kwargs["model_id"], kwargs.get("dataset_path"))
