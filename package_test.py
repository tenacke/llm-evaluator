from llm_evaluator import LLMEvaluator


def pairwise():
    evaluator = LLMEvaluator(
        connection="ollama",
        task="pairwise",
        repetition=1,
    )
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


def nli():
    evaluator = LLMEvaluator(
        connection="ollama",
        task="nli",
        repetition=1,
    )

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


def summarization():
    evaluator = LLMEvaluator(
        connection="ollama",
        task="summarization",
        repetition=1,
    )

    import os

    example_text = ""
    with open(
        os.path.join(
            # "../..",
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


while True:
    input_text = input("Enter the task to evaluate (or 'exit' to quit): ")
    if input_text.lower() == "exit":
        break

    if input_text == "pairwise":
        pairwise()

    elif input_text == "nli":
        nli()

    elif input_text == "summarization":
        summarization()

    else:
        print("Invalid task. Please enter 'pairwise', 'nli', or 'summarization'.")
