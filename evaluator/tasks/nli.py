from .base import BaseTask
from .prompts import NLI_PROMPT
from ..exceptions import BaseConnectionError, InternalModelTiredError

from dataclasses import dataclass
from beartype.typing import Any, List, Union


@dataclass
class NLIOutput:
    """
    Output for the NLI task.
    """

    # The passed or failed status of the evaluation
    status: bool

    # The explanation of the evaluation
    explanation: Union[str, None] = None


class NLI(BaseTask):
    """
    A class to perform Natural Language Inference (NLI) tasks using a language model.
    """

    def perform(
        self,
        *,
        premise: str,
        hypothesis: str,
        label: str,
        explain: bool = True,
        **kwargs,
    ) -> NLIOutput:
        """
        Perform NLI task with the model and given input.
        """
        # TODO : Add error handling for evaluation issues

        prompt = NLI_PROMPT.format(
            premise=premise,
            hypothesis=hypothesis,
            label=label,
        )
        true_count = 0
        status = False
        for _ in range(self.repetition):
            output = self._perform(
                prompt=prompt,
                explain=explain,
                **kwargs,
            )
            if output.status:
                true_count += 1

        if true_count > self.repetition / 2:
            # If more than half of the responses are true, consider it a pass
            status = True

        return NLIOutput(
            explanation=output.explanation,
            status=status,
        )

    def _perform(
        self,
        *,
        prompt: str,
        explain: bool = True,
        **kwargs,
    ) -> NLIOutput:
        timeout = self.timeout
        while True:
            try:
                response = self.connection.send(
                    query=prompt,
                    **kwargs,
                )
                answer = (
                    "true"
                    in response.split("Answer: ")[1].split("\n")[0].strip().lower()
                )
                if explain:
                    explanation = response.split("Explanation: ")[1].strip()

            except IndexError:
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

        return NLIOutput(
            explanation=explanation if explain else None,
            status=answer,
        )
