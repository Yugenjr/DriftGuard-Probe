"""Core Supervisor routing engine orchestrating investigation workflows."""
import logging
from typing import Dict, Any
from .state import InvestigationState
from .lifecycle import InvestigationStatus
from ..models.incident import Incident
from .di import Container, get_container

logger = logging.getLogger(__name__)


class CoreSupervisor:
    """Orchestrates investigation lifecycle transitions via domain workflows.
    
    Instead of manually calling individual agents in sequence, the supervisor routes
    incidents to dedicated workflows (e.g. Drift, Bias, Latency, Security).
    """
    def __init__(self, container: Container = None):
        self.container = container or get_container()

    async def initiate_investigation(self, incident: Incident) -> InvestigationState:
        """Create initial runtime execution state and begin workflow evaluation."""
        state = InvestigationState(
            investigation_id=f"inv-{incident.incident_id}",
            incident=incident,
            status=InvestigationStatus.CREATED,
        )
        state.transition_to(InvestigationStatus.COLLECTING_EVIDENCE, "Investigation initialized via webhook.")
        logger.info("Initiated investigation %s for model %s", state.investigation_id, incident.model_id)

        # TODO: Implementation pending for async workflow registry routing and state persistence
        return state
