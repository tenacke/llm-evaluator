# from beartype.claw import beartype_this_package
# from beartype import BeartypeConf

# Beartype the package
# beartype_this_package()

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
