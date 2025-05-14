from .base import BaseTask
from .prompts import (
    SUMMARIZATION_TEMPLATE,
    COHERENCE_CRITERIA,
    RELEVANCE_CRITERIA,
    FLUENCY_CRITERIA,
    CONSISTENCY_CRITERIA,
)
from ..exceptions import (
    BaseConnectionError,
    MetricNotFoundError,
    InternalModelTiredError,
)

from dataclasses import dataclass
from beartype.typing import List, Union, Literal

METRICS = [
    "coherence",
    "relevance",
    "fluency",
    "consistency",
]

PROMPT_MAPPER = {
    "coherence": COHERENCE_CRITERIA,
    "relevance": RELEVANCE_CRITERIA,
    "fluency": FLUENCY_CRITERIA,
    "consistency": CONSISTENCY_CRITERIA,
}


@dataclass
class SummarizationOutput:
    """
    Output class for summarization tasks.
    """

    # The score of the generated summary
    score: Union[int, float]

    metric: Union[str, None] = None

    # The explanation of the evaluation
    explanation: Union[str, None] = None


class Summarization(BaseTask):
    """
    A class to perform summarization tasks using a language model.
    """

    def _get_prompt(
        self,
        metric: str,
    ) -> str:
        """
        Get the prompt for the specified metric.
        """
        if metric not in PROMPT_MAPPER:
            raise MetricNotFoundError(
                f"Metric '{metric}' not found. Available metrics are: {', '.join(METRICS)}"
            )
        return PROMPT_MAPPER[metric]

    def perform(
        self,
        *,
        text: str,
        summary: str,
        metric: Literal[
            "coherence", "relevance", "fluency", "consistency", "all"
        ] = "all",
        explain: bool = True,
        custom_prompt: str | None = None,
        **kwargs,
    ) -> Union[SummarizationOutput, List[SummarizationOutput]]:
        """
        Evaluate the model with the given prompt.
        """

        if metric == "all":
            # If 'all' is specified, evaluate all metrics
            metrics = METRICS
            total_output = []
            for metric in metrics:
                output = self._perform(
                    text=text,
                    summary=summary,
                    metric=metric,
                    explain=explain,
                    custom_prompt=custom_prompt,
                    **kwargs,
                )
                total_output.append(output)
            return total_output
        else:
            return self._perform(
                text=text,
                summary=summary,
                metric=metric,
                explain=explain,
                custom_prompt=custom_prompt,
                **kwargs,
            )

    def _perform(
        self,
        *,
        text: str,
        summary: str,
        metric: str,
        explain: bool = True,
        custom_prompt: str | None = None,
        **kwargs,
    ) -> SummarizationOutput:
        """
        Perform the summarization task with the given input.
        """
        output = self._run_repetitions(
            text=text,
            summary=summary,
            prompt=(
                self._get_prompt(metric=metric)
                if custom_prompt is None
                else custom_prompt
            ),
            explain=explain,
            **kwargs,
        )
        output.metric = metric
        return output

    def _run_repetitions(
        self,
        *,
        text: str,
        summary: str,
        prompt: str,
        explain: bool,
        **kwargs,
    ) -> SummarizationOutput:
        """
        Run the prompt with multiple repetitions.
        """
        total_score = 0
        for _ in range(self.repetition):
            response = self._run_prompt(
                text=text,
                summary=summary,
                prompt=prompt,
                explain=explain,
                **kwargs,
            )
            total_score += response.score

        return SummarizationOutput(
            explanation=response.explanation if explain else None,
            score=total_score / self.repetition,
        )

    def _run_prompt(
        self,
        *,
        text: str,
        summary: str,
        prompt: str,
        explain: bool,
        **kwargs,
    ) -> SummarizationOutput:
        """
        Run the prompt with single input.
        """
        timeout = self.timeout
        while True:
            try:
                response = self.connection.send(
                    query=SUMMARIZATION_TEMPLATE.format(
                        criteria=prompt,
                        text=text,
                        summary=summary,
                    ),
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
        return SummarizationOutput(
            explanation=explanation if explain else None,
            score=score,
        )
