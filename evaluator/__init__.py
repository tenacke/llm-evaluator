from __future__ import annotations
from beartype.claw import beartype_this_package

beartype_this_package()

from .evaluator import LLMEvaluator
from .exceptions import (
    EvaluatorError,
    InvalidTaskError,
    ConnectionTypeError,
    BaseConnectionError,
    OllamaError,
    OllamaConnectionError,
    OllamaModelError,
    OllamaResponseError,
    OllamaTimeoutError,
    BaseTaskError,
    SummarizationError,
    MetricNotFoundError,
    NLIError,
    PairwiseError,
    InternalError,
    InternalModelTiredError,
)

__version__ = "0.1.1"

__all__ = [
    "LLMEvaluator",
    "EvaluatorError",
    "InvalidTaskError",
    "ConnectionTypeError",
    "BaseConnectionError",
    "OllamaError",
    "OllamaConnectionError",
    "OllamaModelError",
    "OllamaResponseError",
    "OllamaTimeoutError",
    "BaseTaskError",
    "SummarizationError",
    "MetricNotFoundError",
    "NLIError",
    "PairwiseError",
    "InternalError",
    "InternalModelTiredError",
]
