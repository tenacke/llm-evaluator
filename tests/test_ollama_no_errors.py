from evaluator import LLMEvaluator
from evaluator.tasks import PairwiseOutput, NLIOutput, SummarizationOutput
import logging

logger = logging.getLogger(__name__)


def test_pairwise():
    evaluator = LLMEvaluator(
        connection="ollama", model="llama3.1:8b", task="pairwise", repetition=1
    )

    example_question = "Answer the following questions as best you can. You have access to the following tools:\n\nPython REPL: A Python shell. Use this to execute python commands. Input should be a valid python command. If you want to see the output of a value, you should print it out with `print(...)`.\n\nUse the following format:\n\nQuestion: the input question you must answer\nThought: you should always think about what to do\nAction: the action to take, should be one of [Python REPL]\nAction Input: the input to the action\nObservation: the result of the action\n... (this Thought/Action/Action Input/Observation can repeat N times)\nThought: I now know the final answer\nFinal Answer: the final answer to the original input question\n\nBegin!\n\nQuestion: whats 258 * 5987"
    example_answer1 = "Thought: I need to perform a mathematical calculation using Python.\nAction: Python REPL\nAction Input: `print(258 * 5987)`\nObservation: The result of the calculation is 166,659.\nThought: I should document the calculation for future reference.\nFinal Answer: The result of the calculation is 166,659."
    example_answer2 = "Thought: To calculate the product of 258 and 5987, we need to perform the following steps: 1. Multiply 258 by 5987 using a calculator or by hand. 2. Print the result with the command 'print(...)'. Python REPL: ```python 258 * 5987 # π * √e ```"
    logger.info("Starting pairwise evaluation...")
    logger.info(f"Question: {example_question}")
    logger.info(f"Answer 1: {example_answer1}")
    logger.info(f"Answer 2: {example_answer2}")
    logger.info("Expecting the evaluator to choose the best answer as answer 1...")
    logger.info("Evaluating...")

    result = evaluator.evaluate(
        question=example_question,
        output1=example_answer1,
        output2=example_answer2,
        explain=True,
    )

    logger.info(f"Pairwise Result: {result.choice}")
    logger.info(f"Pairwise Explanation: {result.explanation}")

    assert result is not None
    assert isinstance(result, PairwiseOutput)
    assert result.choice == 1 or result.choice == 2
    assert isinstance(result.explanation, str)

    logger.info("Pairwise evaluation completed successfully.")


def test_nli():
    evaluator = LLMEvaluator(
        connection="ollama", model="llama3.1:8b", task="nli", repetition=1
    )

    example_premise = "The cat sat on the mat."
    example_hypothesis = "The mat is under the cat."
    example_label = "entailment"

    logger.info("Starting NLI evaluation...")
    logger.info(f"Premise: {example_premise}")
    logger.info(f"Hypothesis: {example_hypothesis}")
    logger.info(f"Label: {example_label}")

    logger.info("Expecting the evaluator to grade the relationship as passed...")
    logger.info("Evaluating...")

    result = evaluator.evaluate(
        premise=example_premise,
        hypothesis=example_hypothesis,
        label=example_label,
        explain=True,
    )

    logger.info(f"NLI Result: {result.status}")
    logger.info(f"NLI Explanation: {result.explanation}")

    assert result is not None
    assert isinstance(result, NLIOutput)
    assert isinstance(result.status, bool)
    assert isinstance(result.explanation, str)

    logger.info("NLI evaluation completed successfully.")


def test_summarization():
    evaluator = LLMEvaluator(
        connection="ollama", model="llama3.1:8b", task="summarization", repetition=1
    )

    example_text = """
    Paul Merson has restarted his row with Andros Townsend after the Tottenham midfielder was brought on with only seven minutes remaining in his team's 0-0 draw with Burnley on Sunday.
    'Just been watching the game, did you miss the coach? #RubberDub #7minutes,' Merson put on Twitter.
    Merson initially angered Townsend for writing in his Sky Sports column that 'if Andros Townsend can get in (the England team) then it opens it up to anybody.'
    Paul Merson had another dig at Andros Townsend after his appearance for Tottenham against Burnley
    Townsend was brought on in the 83rd minute for Tottenham as they drew 0-0 against Burnley
    Andros Townsend scores England's equaliser in their 1-1 friendly draw with Italy in Turin on Tuesday night
    The former Arsenal man was proven wrong when Townsend hit a stunning equaliser for England against Italy and he duly admitted his mistake.
    'It's not as though I was watching hoping he wouldn't score for England, I'm genuinely pleased for him and fair play to him – it was a great goal,' Merson said. 'It's just a matter of opinion, and my opinion was that he got pulled off after half an hour at Manchester United in front of Roy Hodgson, so he shouldn't have been in the squad.
    'When I'm wrong, I hold my hands up. I don't have a problem with doing that - I'll always be the first to admit when I'm wrong.'
    Townsend hit back at Merson on Twitter after scoring for England against Italy
    Sky Sports pundit  Merson (centre) criticised Townsend's call-up to the England squad last week
    Townsend hit back at Merson after netting for England in Turin on Wednesday, saying 'Not bad for a player that should be 'nowhere near the squad' ay @PaulMerse?'
    Any bad feeling between the pair seemed to have passed but Merson was unable to resist having another dig at Townsend after Tottenham drew at Turf Moor.
    @highlight
    Andros Townsend an 83rd minute sub in Tottenham's draw with Burnley
    @highlight
    He was unable to find a winner as the game ended without a goal
    @highlight
    Townsend had clashed with Paul Merson last week over England call-up 
    """
    example_summary = "paul merson has restarted his row with andros townsend after the tottenham midfielder was brought on with only seven minutes remaining in his team 's 0-0 draw with burnley on sunday . townsend was brought on in the 83rd minute for tottenham as they drew 0-0 against burnley . townsend hit back at merson on twitter after scoring for england against italy ."
    example_metric = "all"

    logger.info("Starting summarization evaluation...")
    logger.info(f"Text: {example_text}")
    logger.info(f"Summary: {example_summary}")
    logger.info(f"Metric: {example_metric}")

    logger.info(
        "Expecting the evaluator to grade the summary with a score from 1 to 5..."
    )
    logger.info("Evaluating...")

    result = evaluator.evaluate(
        text=example_text,
        summary=example_summary,
        metric=example_metric,
        explain=True,
    )

    assert result is not None
    assert isinstance(result, list)

    for r in result:
        assert isinstance(r, SummarizationOutput)
        logger.info(f"Summarization Metric: {r.metric}")
        logger.info(f"Summarization Score: {r.score}")
        logger.info(f"Summarization Explanation: {r.explanation}")
        assert r.metric in ["coherence", "fluency", "relevance", "consistency"]
        assert isinstance(r.score, float)
        assert isinstance(r.explanation, str)

    logger.info("Summarization evaluation completed successfully.")
