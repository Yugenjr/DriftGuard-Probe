"""Incident domain model."""
from enum import Enum
from datetime import datetime, timezone
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field


class IncidentSeverity(str, Enum):
    """Severity classification of production model anomaly."""
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class IncidentStatus(str, Enum):
    """Current triage status of an incident."""
    NEW = "NEW"
    INVESTIGATING = "INVESTIGATING"
    RESOLVED = "RESOLVED"
    FALSE_POSITIVE = "FALSE_POSITIVE"


class Incident(BaseModel):
    """Represents an MLOps production anomaly triggering an automated investigation."""
    incident_id: str = Field(..., description="Unique globally assigned incident identifier")
    model_id: str = Field(..., description="Target model deployment identifier")
    model_version: str = Field(..., description="Model version tag experiencing drift/anomaly")
    detected_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    severity: IncidentSeverity = Field(default=IncidentSeverity.MEDIUM)
    status: IncidentStatus = Field(default=IncidentStatus.NEW)
    trigger_type: str = Field(..., description="Anomaly classification e.g. 'drift_detected' or 'latency_spike'")
    raw_payload: Dict[str, Any] = Field(default_factory=dict, description="Original alerting platform webhook payload")

    # TODO: Implementation pending for validation methods and statistical confidence calculation
