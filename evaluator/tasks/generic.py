from .base import BaseTask
from .prompts import GENERIC_TEMPLATE
from ..exceptions import BaseConnectionError, InternalModelTiredError

from dataclasses import dataclass
from beartype.typing import Any, List, Union


@dataclass
class GenericOutput:
    """
    Output for the GENERIC task.
    """

    # The passed or failed status of the evaluation
    score: Union[int, float]

    # The explanation of the evaluation
    explanation: Union[str, None] = None


class Generic(BaseTask):
    """
    A class to perform Machine Translation tasks using a language model.
    """

    def perform(
        self,
        *,
        input: str,
        output: str,
        custom_prompt: str,
        explain: bool = True,
        **kwargs,
    ) -> GenericOutput:
        """
        Perform NLI task with the model and given input.
        """
        # TODO : Add error handling for evaluation issues

        prompt = GENERIC_TEMPLATE.format(
            criteria=custom_prompt,
            input=input,
            output=output,
        )
        total_score = 0
        for _ in range(self.repetition):
            response = self._perform(
                prompt=prompt,
                explain=explain,
                **kwargs,
            )
            total_score += response.score

        return GenericOutput(
            explanation=response.explanation,
            score=total_score / self.repetition,
        )

    def _perform(
        self,
        *,
        prompt: str,
        explain: bool = True,
        **kwargs,
    ) -> GenericOutput:
        timeout = self.timeout
        while True:
            try:
                response = self.connection.send(
                    query=prompt,
                    **kwargs,
                )
                score = int(response.split("Score: ")[1][0])
                if explain:
                    explanation = response.split("Explanation: ")[1].strip()
            except IndexError or ValueError:
                # Retry if the response format is not as expected
                timeout -= 1
                if timeout == 0:
                    raise InternalModelTiredError(
                        f"Timeout while waiting for the correct response. Please check the model and the connection."
                    )
                continue
            except BaseConnectionError as e:
                # TODO Handle connection errors
                raise e
            else:
                break
        return GenericOutput(
            explanation=explanation if explain else None,
            score=score,
        )
