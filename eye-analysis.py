import os
import sys
import pandas as pd

import ollama

coherence_prompt = """
You will be given one summary written for a news article.
Your task is to rate the summary on one metric.
Please make sure you read and understand these instructions carefully.

Evaluation Criteria:
Coherence:  (1-5) - the collective quality of all sentences. 
We align this dimension with the DUC quality question of structure and coherence whereby "the summary should be well-structured and well-organized.
The summary should not just be a heap of related information, but should build from sentence to a coherent body of information about a topic."

Evaluation Steps:
1. Read the news article carefully and identify the main topic and key points.
2. Read the summary and compare it to the news article. Check if the summary covers the main topic and key points of the news article, and if it presents them in a clear and logical order.
3. Assign a score for coherence on a scale of 1 to 5, where 1 is the lowest and 5 is the highest based on the Evaluation Criteria.

Question:
How coherent is the summary? That is, how well do the sentences in the summary fit together? (On a scale of 1-5, with 1 being the lowest)

Please rate the summary based on the above metrics and provide your scores and explanations in the response box.
Please use the following format for your response:
Score: point
Explanation: explanation
"""

consistency_prompt = """
You will be given one summary written for a news article.
Your task is to rate the summary on one metric.
Please make sure you read and understand these instructions carefully.

Evaluation Criteria:
Consistency (1-5) - the factual alignment between the summary and the summarized source.
A factually consistent summary contains only statements that are entailed by the source document.
Annotators were also asked to penalize summaries that contained hallucinated facts.

Evaluation Steps:
1. Read the news article carefully and identify the main facts and details it presents.
2. Read the summary and compare it to the news article. Check if the summary contains any factual errors that are not supported by the article.
3. Assign a score for consistency based on the Evaluation Criteria.

Question:
How consistent is the summary with the source document in terms of the factual alignment? (On a scale of 1-5, with 1 being the lowest)

Please rate the summary based on the above metrics and provide your scores and explanations in the response box.
Please use the following format for your response:
Score: point
Explanation: explanation
"""

fluency_prompt = """
You will be given one summary written for a news article.
Your task is to rate the summary on one metric.
Please make sure you read and understand these instructions carefully.

Fluency (1-5): This rating measures the quality of individual sentences, are they well-written and grammatically correct.
Consider the quality of individual sentences.

Evaluation steps:
1. Read the given summary.
2. Evaluate the fluency of the summary on a scale of 1-5 based on the criteria provided.
3. Provide the rating.

Question:
Based on the evaluation criteria, how fluent is the summary? (On a scale of 1-5, with 1 being the lowest)

Please rate the summary based on the above metrics and provide your scores and explanations in the response box.
Please use the following format for your response:
Score: point
Explanation: explanation
"""

relevance_prompt = """
You will be given one summary written for a news article.
Your task is to rate the summary on one metric.
Please make sure you read and understand these instructions carefully.

Evaluation Criteria:
Relevance (1-5) - selection of important content from the source.
The summary should include only important information from the source document. 
Annotators were instructed to penalize summaries which contained redundancies and excess

Evaluation Steps:
1. Read the summary and the source
2. Compare the summary to the source document and identify the main points of the article.
3. Assess how well the summary covers the main points of the article, and how much irrelevant or redundant information it contains.
4. Assign a relevance score from 1 to 5.

Please rate the summary based on the above metrics and provide your scores and explanations in the response box.
Please use the following format for your response:
Score: point
Explanation: explanation
"""


def get_models():
    return [model.model for model in ollama.list().models]


# Get the path to the datasets folder
datasets_path = os.path.join(os.path.dirname(__file__), "datasets")
csv_files_path = os.path.join(os.path.dirname(__file__), "csv")
logs_path = os.path.join(os.path.dirname(__file__), "logs")
output_path = os.path.join(os.path.dirname(__file__), "output")
if not os.path.exists(csv_files_path):
    os.makedirs(csv_files_path)
if not os.path.exists(logs_path):
    os.makedirs(logs_path)
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Check if command line arguments are provided
if len(sys.argv) < 3:
    print(
        "Usage: python eye-analysis.py <model_name> <metric>"
    )
    sys.exit()

if sys.argv[1] == "--help":
    print(
        "Usage: python eye-analysis.py <model_name> <metric>"
    )
    sys.exit()

# Get the model name from the command line arguments
model_name = sys.argv[1]
if ":" not in model_name:
    print(
        "Invalid model name format. Please provide a valid model name. Example: evallm:v3"
    )
    sys.exit()


metric = sys.argv[2]
if metric not in ["coherence", "fluency", "relevance", "consistency"]:
    print(
        "Invalid metric. Please provide one of the following: coherence, fluency, relevance, consistency"
    )
    sys.exit()

# model_name = f"{model_base_name}-{metric}:{model_version}"
if model_name not in get_models():
    # if model_name not in get_models():
    print("Invalid model name. Please provide a valid model name.")
    sys.exit()

client = ollama.Client()

exception_count = 0

if metric == "coherence":
    prompt = coherence_prompt
elif metric == "consistency":
    prompt = consistency_prompt
elif metric == "fluency":
    prompt = fluency_prompt
elif metric == "relevance":
    prompt = relevance_prompt

type_rows = {"poor": 380, "average": 1481, "powerful": 1156}    # HARDCODE THIS ONE

for key, val in type_rows.items():
    df = pd.read_csv(
        os.path.join(csv_files_path, f"{key}_model.csv"),
    )
    row = df[df["id"] == val]
    text_file = row["filepath"].values[0]

    with open(os.path.join(datasets_path, text_file), "r") as f:
        text = f.read()

    query = prompt + "Summary\n" + row["decoded"].values[0] + "\n\nText\n" + text

    print(f"Model: {model_name} power: {key}, index: {val}")
    print(f'Query:\n{query}')
    

    response = client.generate(model_name, query).response
    print(f"Response:\n{response}\n\n")
