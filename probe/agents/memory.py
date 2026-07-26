"""Memory Agent orchestrating memory infrastructure facilities."""
import logging
from typing import Any, Dict, List, Optional
from .base import BaseAgent
from ..core.state import InvestigationState
from ..memory.retriever import KnowledgeRetriever
from ..memory.store import VectorStore

logger = logging.getLogger(__name__)


class MemoryAgent(BaseAgent):
    """Orchestrates underlying vector storage, summarizers, and retrieval infrastructure.
    
    Adhering to architectural best practice: Memory is infrastructure, not an autonomous reasoning loop.
    The MemoryAgent simply coordinates persistence and indexing across vector storage facilities.
    """
    def __init__(self, retriever: Optional[KnowledgeRetriever] = None, store: Optional[VectorStore] = None):
        super().__init__()
        self.retriever = retriever or KnowledgeRetriever()
        self.store = store or VectorStore()

    @property
    def role_name(self) -> str:
        return "Memory"

    async def execute(self, state: InvestigationState, **kwargs: Any) -> Dict[str, Any]:
        """Index completed investigation snapshots into semantic memory collections."""
        logger.info("Memory Agent archiving investigation %s into vector store.", state.investigation_id)
        content = state.report.markdown_content if state.report else f"Incident on {state.incident.model_id}"
        await self.store.store_document(
            collection="incidents",
            doc_id=state.investigation_id,
            content=content,
            metadata={"model_id": state.incident.model_id, "status": state.status.value},
        )
        # TODO: Implementation pending for automatic embedding compaction and consolidation
        return {"archived": True, "collection": "incidents", "id": state.investigation_id}
