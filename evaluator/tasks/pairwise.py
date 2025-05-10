from .base import BaseTask
from .prompts import PAIRWISE_PROMPT
from ..exceptions import BaseConnectionError, InternalModelTiredError

from dataclasses import dataclass
from beartype.typing import Any, List, Union


@dataclass
class PairwiseOutput:
    """
    Output class for pairwise tasks.
    """

    # The choice made by the evaluator
    choice: int  # 1 or 2 (0 if both are equal)

    # The explanation of the evaluation
    explanation: Union[str, None] = None


class Pairwise(BaseTask):
    """
    Evaluates the performance of a model by comparing two outputs and determining which one is better.
    """

    def perform(
        self,
        *,
        question: str,
        output1: str,
        output2: str,
        explain: bool = True,
        **kwargs,
    ) -> PairwiseOutput:
        """
        Perform the pairwise evaluation model with the given input.
        """
        # TODO : Add error handling for evaluation issues

        prompt = PAIRWISE_PROMPT.format(
            question=question,
            answer_1=output1,
            answer_2=output2,
        )

        counts = [0, 0]
        for _ in range(self.repetition):
            output = self._perform(
                prompt=prompt,
                explain=explain,
                **kwargs,
            )
            counts[output.choice - 1] += 1

        return PairwiseOutput(
            explanation=output.explanation,
            choice=(1 if counts[0] > counts[1] else 2 if counts[1] > counts[0] else 0),
        )

    def _perform(
        self,
        *,
        prompt: str,
        explain: bool = True,
        **kwargs,
    ) -> PairwiseOutput:
        """
        Perform the pairwise evaluation model with the given input.
        """
        # TODO : Add error handling for evaluation issues

        # Call the connection to get the output
        timeout = self.timeout
        while True:
            try:
                response = self.connection.send(
                    query=prompt,
                    **kwargs,
                )
                better_answer = (
                    response.split("Better Answer: ")[1].split("\n")[0].strip().lower()
                )
                if "1" in better_answer:
                    choice = 1
                elif "2" in better_answer:
                    choice = 2
                else:
                    raise ValueError(
                        f"Invalid choice in response: {response}. Expected '1' or '2'."
                    )
                if explain:
                    explanation = response.split("Explanation: ")[1].strip()
            except IndexError or ValueError:
                timeout -= 1
                # if timeout == 0:
                #     raise InternalModelTiredError(
                #         f"Timeout while waiting for the correct response. Please check the model and the connection."
                #     )
                continue
            except BaseConnectionError as e:
                # TODO : Add error handling for connection issues
                raise e
            else:
                break

        return PairwiseOutput(
            explanation=explanation,
            choice=choice,
        )
