from ollama import Client
from pydantic import BaseModel, Field

from .base import BaseConnection, SendInputConfig


class OllamaConfig(BaseModel):
    """Configuration for the Ollama LLM."""

    # The URL of the Ollama server
    url: str = Field(
        default="http://localhost:11434",
        description="The URL of the Ollama server.",
    )

    # The model to use
    model: str = Field(
        default="llama3.1:8b",
        description="The LLM model to use.",
    )


class OllamaConnection(BaseConnection):
    """
    Connection to the Ollama LLM.
    """

    def __init__(self, config: OllamaConfig):
        self.config = config
        # TODO : Add error handling for connection issues
        # Initialize the Ollama client
        # Check if the URL is valid
        # Check if the model is available
        # Check if the server is running
        try:
            self.client = Client(host=config.url)
            self.client.pull(model=config.model)
        except Exception as e:
            pass

    def send(self, message: SendInputConfig) -> str:
        """
        Send a request to the Ollama LLM and return the response.
        """
        # TODO : Add error handling for request issues
        # Send the request to the LLM
        try:
            response = self.client.generate(
                model=self.config.model,
                prompt=message.query,
            ).response
        except Exception as e:
            pass

        return response
