"""Runtime investigation state tracking."""
from datetime import datetime, timezone
from typing import Dict, List, Optional
from pydantic import BaseModel, Field
from .lifecycle import InvestigationStatus
from ..models.incident import Incident
from ..models.evidence import EvidenceItem
from ..models.hypothesis import Hypothesis
from ..models.experiment import Experiment
from ..models.recommendation import Recommendation
from ..models.report import InvestigationReport


class InvestigationState(BaseModel):
    """Runtime execution state representing the active investigation session.
    
    This model is passed across workflow transitions and persisted via StorageProvider,
    separating dynamic runtime state from persistent business entities.
    """
    investigation_id: str = Field(..., description="Unique runtime session UUID")
    status: InvestigationStatus = Field(default=InvestigationStatus.CREATED)
    incident: Incident
    active_workflow_name: Optional[str] = Field(default=None, description="Selected routing workflow")
    evidence_items: List[EvidenceItem] = Field(default_factory=list)
    hypotheses: List[Hypothesis] = Field(default_factory=list)
    experiments: List[Experiment] = Field(default_factory=list)
    recommendation: Optional[Recommendation] = None
    report: Optional[InvestigationReport] = None
    started_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    completed_at: Optional[datetime] = None
    execution_history: List[str] = Field(default_factory=list, description="Chronological trace of agent actions")

    def transition_to(self, new_status: InvestigationStatus, log_entry: Optional[str] = None) -> None:
        """Advance the investigation lifecycle and log state transitions."""
        self.status = new_status
        self.updated_at = datetime.now(timezone.utc)
        if log_entry:
            self.execution_history.append(f"[{self.updated_at.isoformat()}] [{new_status.value}] {log_entry}")
        if new_status in (InvestigationStatus.COMPLETED, InvestigationStatus.FAILED):
            self.completed_at = self.updated_at
            
    # TODO: Implementation pending for async immutable snapshots and rollback checkpoints
