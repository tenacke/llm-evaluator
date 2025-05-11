from .base import BaseConnection
from ..exceptions import OpenAIResponseError, OpenAIConnectionError

from openai import OpenAI


class OpenAIConnection(BaseConnection):
    """
    Connection to the OpenAI LLM.
    """

    def __init__(
        self,
        *,
        api_key: str,
        model: str = "gpt-3.5-turbo",
        **kwargs,
    ):
        self.model = model
        # Initialize the OpenAI client
        try:
            self.client = OpenAI(api_key=api_key)
        except Exception as e:
            raise OpenAIConnectionError(
                f"Failed to connect to the OpenAI server. Error: {str(e)}"
            ) from e

    def send(
        self,
        *,
        query: str,
        **kwargs,
    ) -> str:
        """
        Send a request to the OpenAI LLM and return the response.
        """
        # Send the request to the LLM
        try:
            response = (
                self.client.chat.completions.create(
                    model=self.config.model,
                    messages=[{"role": "user", "content": query}],
                )
                .choices[0]
                .message.content
            )
        except Exception as e:
            raise OpenAIResponseError(
                f"Error while sending request to OpenAI: {e}"
            ) from e

        return response
