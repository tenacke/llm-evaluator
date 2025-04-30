from ..connection.base import BaseConnection

from abc import ABC, abstractmethod


class BaseTask(ABC):
    """
    Base class for all task evaluators.
    """

    def __init__(
        self,
        *,
        connection: BaseConnection,
        repetition: int,
        timeout: int,
        **kwargs,
    ):
        # TODO : Add error handling for connection issues
        # Initialize the connection to the LLM
        self.connection = connection
        self.repetition = repetition
        self.timeout = timeout

    @abstractmethod
    def perform(self, *args, **kwargs):
        """
        Perform the task with the given details.
        """
        pass
