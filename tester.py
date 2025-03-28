import os
import sys
import pandas as pd

import ollama

coherence_prompt = """
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

First find correct method to evaluate the coherence of the summary.
Then rate the summary based on coherence and provide your scores and explanations in the response box.
Please use the following format for your response:
Score: point
Explanation: explanation
"""

consistency_prompt = """
You will be given one summary written for a news article.
Your task is to rate the summary on one metric.
Please make sure you read and understand these instructions carefully.

Evaluation Criteria:
Consistency: It measures the quality of the summary in terms of how well it maintains the same tone and
style throughout the text.
Score 5: Entirely consistent, with the same tone and style maintained throughout the text.
Score 4: Only containing some minor inconsistent parts that basically do not affect overall consistency.
Score 3: Consistent in general, with some obvious conflicting tone and style problems.
Score 2: There are major inconsistent tone and style, but at least the related topic.
Score 1: Not consistent at all, full of self-contradictory or unrelated tone and style.

First find correct method to evaluate the coherence of the summary.
Then rate the summary based on consistency and provide your scores and explanations in the response box.
Please use the following format for your response:
Score: point
Explanation: explanation
"""

fluency_prompt = """
You will be given one summary written for a news article.
Your task is to rate the summary on one metric.
Please make sure you read and understand these instructions carefully.

Evaluation Criteria:
Fluency: It measures the quality of individual sentences, are they grammatically correct, non-repetitive,
and in accord with common English usage, with clear meanings.
Score 5: Entirely fluent, grammatically correct, and well-written.
Score 4: Only containing some minor non-fluent parts or grammatical errors that basically have no effect
on fluency.
Score 3: Fluent in general, with some obvious grammatical errors and unfamiliar phrases.
Score 2: There are major grammatical errors, duplication, unfamiliar phrases and syntactic structures,
and missing components, but some fluent segments.
Score 1: Not fluent at all, full of meaningless fragments and unclear contents.

First find correct method to evaluate the coherence of the summary.
Then rate the summary based on fluency and provide your scores and explanations in the response box.
Please use the following format for your response:
Score: point
Explanation: explanation
"""

relevance_prompt = """
You will be given one summary written for a news article.
Your task is to rate the summary on one metric.
Please make sure you read and understand these instructions carefully.

Evaluation Criteria:
Relevance: It measures the quality of the summary in terms of how well it covers the main topic and key
points of the news article.
Score 5: Entirely relevant, covering all the main topics and key points of the news article.
Score 4: Only containing some minor irrelevant parts that basically do not affect overall relevance.
Score 3: Relevant in general, with some obvious conflicting logical or inconsistent problems.
Score 2: There are major irrelevant parts, but at least the related topic.
Score 1: Not relevant at all, full of self-contradictory or unrelated content.

First find correct method to evaluate the coherence of the summary.
Then rate the summary based on relevance and provide your scores and explanations in the response box.
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
output_path = os.path.join(os.path.dirname(__file__), "outputs")
if not os.path.exists(csv_files_path):
    os.makedirs(csv_files_path)
if not os.path.exists(logs_path):
    os.makedirs(logs_path)
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Check if command line arguments are provided
if len(sys.argv) < 5:
    print(
        "Usage: python tester.py <model_name> [powerful|poor|average] <number_of_repetitions>"
    )
    sys.exit()

if sys.argv[1] == "--help":
    print(
        "Usage: python tester.py <model_name> [powerful|poor|average] <number_of_repetitions>"
    )
    sys.exit()

# Get the model name from the command line arguments
model_name = sys.argv[1]
if ":" not in model_name:
    print(
        "Invalid model name format. Please provide a valid model name. Example: evallm:v3"
    )
    sys.exit()
# model_base_name = model_name.split(":")[0]
# model_version = model_name.split(":")[1]

# Get the evaluation type from the command line arguments
evaluation_type = sys.argv[2]
if evaluation_type not in ["powerful", "poor", "average"]:
    print(
        "Invalid evaluation type. Please provide one of the following: powerful, poor, average"
    )
    sys.exit()

if not sys.argv[3].isdigit():
    print("Invalid number of repetitions. Please provide a valid number.")
    sys.exit()

metric = sys.argv[4]
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

number_of_repetitions = int(sys.argv[3])

try:
    # Load the test data
    test_data_file = evaluation_type + "_model.csv"
    test_data = pd.read_csv(os.path.join(csv_files_path, test_data_file))
except:
    print("Error loading the test data.")
    sys.exit()

client = ollama.Client()

exception_count = 0
log_file_name = f"{model_name}_{metric}_{evaluation_type}_logs.csv"
log_file = open(os.path.join(logs_path, log_file_name), "w")

if metric == "coherence":
    prompt = coherence_prompt
elif metric == "consistency":
    prompt = consistency_prompt
elif metric == "fluency":
    prompt = fluency_prompt
elif metric == "relevance":
    prompt = relevance_prompt

# Evaluate the model
results = pd.DataFrame(columns=["result"])
for index, row in test_data.iterrows():
    print(f"Evaluating index {index+1}...", flush=True)

    text_file = row["filepath"]
    with open(os.path.join(datasets_path, text_file), "r") as f:
        text = f.read()

    if "@highlight" in text:
        text = text.split("@highlight")[0]

    query = (
        prompt
        + "Summary\n"
        + row["decoded"]
        # + "\n\nReference"
        # + row["reference"]
        + "\n\nText\n"
        + text
    )

    repetition_results = {"result": 0}
    count = 0
    for i in range(number_of_repetitions):
        print(f"Repetition {i+1}...", flush=True)
        exception_ = False
        response = client.generate(model_name, query).response
        try:
            if "</think>" in response:
                response = response.split("</think>")[1]
            score = response.split("Score: ")[1][0]
            repetition_results["result"] += int(score)
            count += 1
        except:
            print(
                f"Error parsing response index {index} repetition {i}",
                flush=True,
            )
            log_file.write(f'{index},{i},"{response.replace(",", ";")}"\n')
            log_file.flush()
            exception_ = True

    if not exception_:
        print(f"Successfully evaluated index {index+1}", flush=True)

    repetition_results["result"] /= count

    results.loc[index] = repetition_results

results.to_csv(
    os.path.join(
        output_path,
        f"{model_name}_{metric}_{evaluation_type}_results.csv",
    )
)
print("Results saved to csv file.", flush=True)
