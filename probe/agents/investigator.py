"""Investigator Agent collecting diagnostic empirical evidence."""
import logging
from typing import Any, List
from .base import BaseAgent
from ..core.state import InvestigationState
from ..models.evidence import EvidenceItem, EvidenceType

logger = logging.getLogger(__name__)


class InvestigatorAgent(BaseAgent):
    """Specialized agent tasked exclusively with empirical evidence acquisition via Tools."""
    @property
    def role_name(self) -> str:
        return "Investigator"

    async def execute(self, state: InvestigationState, **kwargs: Any) -> List[EvidenceItem]:
        logger.info("Investigator Agent acquiring metrics for model %s", state.incident.model_id)
        # Simulate tool execution gathering statistical metrics
        item = EvidenceItem(
            evidence_id=f"ev-{len(state.evidence_items) + 1}",
            source_tool="get_drift",
            evidence_type=EvidenceType.DRIFT_STATS,
            summary="Feature adwin_drift_score breached baseline threshold of 0.10.",
            data_payload={"observed_drift": 0.12, "feature": "user_age"},
            relevance_score=0.95,
        )
        state.evidence_items.append(item)
        # TODO: Implementation pending for dynamic iteration over available assigned tools
        return [item]
