from .base import BaseEvaluator

from pydantic import BaseModel, Field


class PairwiseEvaluator(BaseEvaluator):
    """
    Evaluates the performance of a model by comparing two outputs and determining which one is better.
    """

    pass
