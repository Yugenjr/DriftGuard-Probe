"""Investigation lifecycle state enumeration."""
from enum import Enum


class InvestigationStatus(str, Enum):
    """Exhaustive lifecycle enumeration for investigation progression.
    
    Every domain workflow and specialized agent transitions through these concrete stages,
    guaranteeing complete visibility, replayability, and OpenTelemetry trace tagging.
    """
    CREATED = "Created"
    COLLECTING_EVIDENCE = "CollectingEvidence"
    RESEARCHING = "Researching"
    GENERATING_HYPOTHESIS = "GeneratingHypothesis"
    PLANNING_EXPERIMENTS = "PlanningExperiments"
    EVALUATING = "Evaluating"
    REPORTING = "Reporting"
    COMPLETED = "Completed"
    FAILED = "Failed"
