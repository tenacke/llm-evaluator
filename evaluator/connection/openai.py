from .base import BaseConnection
from ..exceptions import OpenAIResponseError, OpenAIConnectionError

from openai import OpenAI
import os


class OpenAIConnection(BaseConnection):
    """
    Connection to the OpenAI LLM.
    """

    def __init__(
        self,
        *,
        api_key: str | None = None,
        model: str = "gpt-4o-mini",
        **kwargs,
    ):
        self.model = model
        # Initialize the OpenAI client
        try:
            if api_key is None and "OPENAI_API_KEY" in os.environ:
                api_key = os.environ["OPENAI_API_KEY"]
            elif api_key is None:
                raise OpenAIConnectionError(
                    "API key is required for OpenAI connection."
                )
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
                self.client.responses.create(
                    model=self.model,
                    input=query,
                    **kwargs,
                ).output_text
                # self.client.chat.completions.create(
                #     model=self.config.model,
                #     messages=[{"role": "user", "content": query}],
                # )
                # .choices[0]
                # .message.content
            )
        except Exception as e:
            raise OpenAIResponseError(
                f"Error while sending request to OpenAI: {e}"
            ) from e

        return response
