"""Specialized multi-agent system reasoning roster."""
from .base import BaseAgent
from .supervisor import SupervisorAgent
from .investigator import InvestigatorAgent
from .researcher import ResearcherAgent
from .hypothesis import HypothesisAgent
from .experimenter import ExperimenterAgent
from .evaluator import EvaluatorAgent
from .reporter import ReporterAgent
from .memory import MemoryAgent
from .planner import PlannerAgent
from .compliance import ComplianceAgent
from .critic import CriticAgent

__all__ = [
    "BaseAgent",
    "SupervisorAgent",
    "InvestigatorAgent",
    "ResearcherAgent",
    "HypothesisAgent",
    "ExperimenterAgent",
    "EvaluatorAgent",
    "ReporterAgent",
    "MemoryAgent",
    "PlannerAgent",
    "ComplianceAgent",
    "CriticAgent",
]
