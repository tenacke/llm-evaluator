from openai import OpenAI
from pydantic import BaseModel, Field

from .base import BaseConnection, SendInputConfig


class OpenAIConfig(BaseModel):
    """Configuration for the OpenAI LLM."""

    # The API key for OpenAI
    api_key: str = Field(
        default="",
        description="The API key for OpenAI.",
    )

    # The model to use
    model: str = Field(
        default="gpt-3.5-turbo",
        description="The LLM model to use.",
    )


class OpenAIConnection(BaseConnection):
    """
    Connection to the OpenAI LLM.
    """

    def __init__(self, config: OpenAIConfig):
        self.config = config
        # TODO : Add error handling for connection issues
        # Initialize the OpenAI client
        try:
            self.client = OpenAI(api_key=config.api_key)
        except Exception as e:
            pass

    def send(self, message: SendInputConfig) -> str:
        """
        Send a request to the OpenAI LLM and return the response.
        """
        # TODO : Add error handling for request issues
        # Send the request to the LLM
        try:
            response = (
                self.client.chat.completions.create(
                    model=self.config.model,
                    messages=[{"role": "user", "content": message.query}],
                )
                .choices[0]
                .message.content
            )
        except Exception as e:
            pass

        return response
