from abc import ABC

BaseConnectionError = ConnectionError
BaseTaskError = RuntimeError
InternalError = (
    RuntimeError  # TODO : Add error handling for internal issues if happens a lot
)
EvaluatorError = RuntimeError


class ConnectionTypeError(EvaluatorError):
    """Exception raised when the connection type is not supported."""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class InvalidTaskError(EvaluatorError):
    """Exception raised when the task is not supported."""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class InternalModelTiredError(InternalError):
    """Exception raised when the model tired out waiting a correct response."""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class SummarizationError(BaseTaskError):
    """Exception raised for errors in the summarization task. Do not use this class directly."""

    pass


class MetricNotFoundError(SummarizationError):
    """Exception raised when a metric is not found."""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class NLIError(BaseTaskError):
    """Exception raised for errors in the NLI task. Do not use this class directly."""

    pass


class PairwiseError(BaseTaskError):
    """Exception raised for errors in the pairwise task. Do not use this class directly."""

    pass


class OllamaError(BaseConnectionError, ABC):
    """Base class for all exceptions raised by the Ollama package. Do not use this class directly."""

    pass


class OllamaConnectionError(OllamaError):
    """Exception raised for connection errors."""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class OllamaModelError(OllamaError):
    """Exception raised for model errors."""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class OllamaResponseError(OllamaError):
    """Exception raised for response errors."""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class OllamaTimeoutError(OllamaError):
    """Exception raised for timeout errors."""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
