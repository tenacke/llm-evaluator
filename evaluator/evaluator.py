from __future__ import annotations

from .connection.base import BaseConnection
from .connection.ollama import OllamaConnection
from .connection.openai import OpenAIConnection

from .tasks.base import BaseTask
from .tasks.summarization import Summarization
from .tasks.nli import NLI
from .tasks.pairwise import Pairwise

from .exceptions import BaseConnectionError, InvalidTaskError, ConnectionTypeError

from typing import Any

CONNECTION_MAP = {
    "ollama": OllamaConnection,
    "openai": OpenAIConnection,
}

TASK_MAP = {
    "summarization": Summarization,
    "nli": NLI,
    "pairwise": Pairwise,
}


class LLMEvaluator:
    """
    Main class for the LLM Evaluator.
    """

    def __init__(
        self,
        *,
        connection: str,
        task: str,
        repetition: int = 1,
        tireness: int = 5,
        **kwargs,
    ):
        if connection not in CONNECTION_MAP:
            raise ConnectionTypeError(f"Invalid connection type: {connection}.")
        if task not in TASK_MAP:
            raise InvalidTaskError(f"Invalid task type: {task}.")

        # Initialize the connection to the LLM
        # TODO : Add error handling for connection issues
        try:
            self.connection: BaseConnection = CONNECTION_MAP[connection](**kwargs)
        except BaseConnectionError as e:
            raise e

        # Initialize the evaluator for the specified task
        # TODO : Add error handling for task issues
        try:
            self.evaluator: BaseTask = TASK_MAP[task](
                connection=self.connection,
                repetition=repetition,
                timeout=tireness,
                **kwargs,
            )
        except Exception as e:
            raise e

    def evaluate(
        self,
        *args,
        **kwargs,
    ) -> Any:
        """
        Evaluate the model with the given prompt.
        """
        # Evaluate the model with the given prompt
        # TODO : Add error handling for evaluation issues
        try:
            result = self.evaluator.perform(*args, **kwargs)

            # Check if the result is a list of scores or a single score
            ## TODO WONT WORK FOR ALL TASKS CHANGE IT
            return result
            # if isinstance(result, list):
            #     print([r.explanation for r in result])
            #     return [r.score for r in result], [r.metric for r in result]
            # print(result.explanation)
            # return result.score, result.metric

        except Exception as e:
            raise e


if __name__ == "__main__":
    # Example usage
    evaluator = LLMEvaluator(
        connection="ollama",
        task="pairwise",
    )

    if True:
        example_question = "Answer the following questions as best you can. You have access to the following tools:\n\nPython REPL: A Python shell. Use this to execute python commands. Input should be a valid python command. If you want to see the output of a value, you should print it out with `print(...)`.\n\nUse the following format:\n\nQuestion: the input question you must answer\nThought: you should always think about what to do\nAction: the action to take, should be one of [Python REPL]\nAction Input: the input to the action\nObservation: the result of the action\n... (this Thought/Action/Action Input/Observation can repeat N times)\nThought: I now know the final answer\nFinal Answer: the final answer to the original input question\n\nBegin!\n\nQuestion: whats 258 * 5987"
        example_answer1 = "Thought: I need to perform a mathematical calculation using Python.\nAction: Python REPL\nAction Input: `print(258 * 5987)`\nObservation: The result of the calculation is 166,659.\nThought: I should document the calculation for future reference.\nFinal Answer: The result of the calculation is 166,659."
        example_answer2 = "Thought: To calculate the product of 258 and 5987, we need to perform the following steps: 1. Multiply 258 by 5987 using a calculator or by hand. 2. Print the result with the command 'print(...)'. Python REPL: ```python 258 * 5987 # π * √e ```"
        # winner 1

        result = evaluator.evaluate(
            question=example_question,
            output1=example_answer1,
            output2=example_answer2,
            explain=True,
        )
        print("Result:", result)

    if False:
        example_premise = "The cat sat on the mat."
        example_hypothesis = "The mat is under the cat."
        example_label = "entailment"

        result = evaluator.evaluate(
            premise=example_premise,
            hypothesis=example_hypothesis,
            label=example_label,
            explain=False,
        )
        print("Result:", result)

    if False:
        import os

        example_text = ""
        with open(
            os.path.join(
                "../..",
                "datasets",
                "cnndm/dailymail/stories/8764fb95bfad8ee849274873a92fb8d6b400eee2.story",
            ),
            "r",
        ) as f:
            example_text = f.read()
        example_summary = "paul merson has restarted his row with andros townsend after the tottenham midfielder was brought on with only seven minutes remaining in his team 's 0-0 draw with burnley on sunday . townsend was brought on in the 83rd minute for tottenham as they drew 0-0 against burnley . townsend hit back at merson on twitter after scoring for england against italy ."
        example_metric = input(
            "Enter the metric to evaluate (coherence, relevance, fluency, consistency, all): "
        )

        result = evaluator.evaluate(
            text=example_text,
            summary=example_summary,
            metric=example_metric,
            explain=True,
        )
        print("Result:", result)
