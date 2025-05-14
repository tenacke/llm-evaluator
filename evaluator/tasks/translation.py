from .base import BaseTask
from .prompts import TRANSLATION_TEMPLATE, TRANSLATION_CRITERIA
from ..exceptions import BaseConnectionError, InternalModelTiredError

from dataclasses import dataclass
from beartype.typing import Any, List, Union


@dataclass
class TranslationOutput:
    """
    Output for the Translation task.
    """

    # The passed or failed status of the evaluation
    score: Union[int, float]

    # The explanation of the evaluation
    explanation: Union[str, None] = None


class Translation(BaseTask):
    """
    A class to perform Machine Translation tasks using a language model.
    """

    def perform(
        self,
        *,
        source: str,
        translation: str,
        explain: bool = True,
        custom_prompt: str | None = None,
        **kwargs,
    ) -> TranslationOutput:
        """
        Perform NLI task with the model and given input.
        """
        # TODO : Add error handling for evaluation issues

        prompt = TRANSLATION_TEMPLATE.format(
            criteria=custom_prompt or TRANSLATION_CRITERIA,
            source=source,
            translation=translation,
        )
        total_score = 0
        for _ in range(self.repetition):
            response = self._perform(
                prompt=prompt,
                explain=explain,
                **kwargs,
            )
            total_score += response.score

        return TranslationOutput(
            explanation=response.explanation,
            score=total_score / self.repetition,
        )

    def _perform(
        self,
        *,
        prompt: str,
        explain: bool = True,
        **kwargs,
    ) -> TranslationOutput:
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
        return TranslationOutput(
            explanation=explanation if explain else None,
            score=score,
        )
