from .base import BaseConnection
from ..exceptions import OllamaConnectionError, OllamaModelError, OllamaResponseError

from ollama import Client


class OllamaConnection(BaseConnection):
    """
    Connection to the Ollama LLM.
    """

    def __init__(
        self,
        *,
        url: str = "http://localhost:11434",
        model: str = "llama3.1:8b",
        **kwargs,
    ):
        """
        Initialize the Ollama connection.
        """

        self.url = url
        self.model = model
        # TODO : Add error handling for connection issues
        # Initialize the Ollama client
        # Check if the URL is valid
        # Check if the server is running
        # Check if the model is available
        try:
            self.client = Client(host=self.url)
        except Exception as e:
            raise OllamaConnectionError(
                f"Failed to connect to the Ollama server at {self.url}. Error: {str(e)}"
            )

        try:
            self.client.pull(model=self.model)
        except Exception as e:
            raise OllamaModelError(
                f"Failed to pull the model {self.model} from the Ollama server. Error: {str(e)}"
            )

    def send(
        self,
        *,
        query: str,
        **kwargs,
    ) -> str:
        """
        Send a request to the Ollama LLM and return the response.
        """
        # TODO : Add error handling for timeout issues
        # Send the request to the LLM
        try:
            response = self.client.generate(
                model=self.model,
                prompt=query,
            ).response
        except Exception as e:
            raise OllamaResponseError(
                f"Failed to get a response from the Ollama server. Error: {str(e)}"
            )
        if "</think>" in response:
            response = response.split("</think>")[1]
        # Check if the response is valid
        if not response:
            raise OllamaResponseError(
                "Received an empty response from the Ollama server."
            )
        return response
