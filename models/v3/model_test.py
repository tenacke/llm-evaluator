import ollama
import os


example_text = ""
with open(
    os.path.join(
        "datasets",
        "cnndm/dailymail/stories/8764fb95bfad8ee849274873a92fb8d6b400eee2.story",
    ),
    "r",
) as f:
    example_text = f.read()

example_summary = "paul merson has restarted his row with andros townsend after the tottenham midfielder was brought on with only seven minutes remaining in his team 's 0-0 draw with burnley on sunday . townsend was brought on in the 83rd minute for tottenham as they drew 0-0 against burnley . townsend hit back at merson on twitter after scoring for england against italy ."

query = (
    """
You will be given one summary written for a news article.
Your task is to rate the summary on one metric.
Please make sure you read and understand these instructions carefully.

Evaluation Criteria:
Coherence: It measures the quality of all sentences collectively, do they make sense as a whole, with the
context organized and connected logically.
Score 5: Entirely coherent, with good context-relatedness among all the sentences.
Score 4: Only containing some minor illogical parts that basically do not affect overall coherency.
Score 3: Coherent in general, with some obvious conflicting logical or inconsistent problems.
Score 2: There are major unreasonable logic and semantic inconsistencies, but at least the related topic.
Score 1: Not coherent at all, full of self-contradictory or unrelated content.

Evaluation Steps:
1. Read the news article carefully and identify the main topic and key points.
2. Read the summary and compare it to the news article. Check if the summary covers the main topic and key
points of the news article, and if it presents them in a clear and logical order.
3. Assign a score for the metric on a scale of 1 to 5, where 1 is the lowest and 5 is the highest based on the
Evaluation Criteria.
4. Provide the scores for coherence in the response box.
5. Provide a brief explanation for each score in the response box.

Please rate the summary based on the above metrics and provide your scores and explanations in the response box.
Please use the following format for your response:
Score: point
Explanation: explanation
"""
    + "summary\n"
    + example_summary
    + "\ntext\n"
    + example_text
    + "\n"
)

model_name = "llama3.1:70b"

for part in ollama.generate(model_name, query, stream=True):
    print(part["response"], end="", flush=True)
