from abc import ABC, abstractmethod

from pydantic import BaseModel, Field


class EvaluateConfig(BaseModel):
    """
    Configuration for the evaluation.
    """

    # The prompt to evaluate
    prompt: str = Field(
        default="",
        description="The prompt to evaluate.",
    )


class BaseEvaluator(ABC):
    """
    Base class for all evaluators.
    """

    def __init__(self):
        pass

    @abstractmethod
    def evaluate(self, config: EvaluateConfig) -> str:
        """
        Evaluate the model with the given prompt.
        """
        pass
