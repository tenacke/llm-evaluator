from abc import ABC, abstractmethod
from pydantic import BaseModel, Field


class SendInputConfig(BaseModel):
    """
    Input for the send method.
    """

    # The query to send to the LLM
    query: str = Field(
        default="",
        description="The query to send to the LLM.",
    )


class BaseConnection(ABC):
    """
    Base class for all connection types.
    """

    @abstractmethod
    def send(self, message: SendInputConfig) -> str:
        """
        Send a request to the provider and return the response.
        """
        pass
