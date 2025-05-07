from abc import ABC, abstractmethod


class BaseConnection(ABC):
    """
    Base class for all connection types.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the connection.
        """
        pass

    @abstractmethod
    def send(
        self,
        *,
        query: str,
        **kwargs,
    ) -> str:
        """
        Send a request to the provider and return the response.
        """
        pass
