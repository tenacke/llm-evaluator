import os
import sys
import pandas as pd
import ollama
from collections import Counter

prompt = """
You are given a Premise and a Hypothesis. Your task is to determine the logical relationship between the two statements. Analyze whether the Hypothesis logically follows from, contradicts, or is unrelated to the Premise. Choose one of the following labels:

Entailment: The Hypothesis must be true if the Premise is true. It logically follows without needing any additional information. This includes paraphrasing, synonymous phrases, or generalizations that preserve truth.

Contradiction: The Hypothesis must be false if the Premise is true. The two statements contain conflicting information and cannot both be true at the same time.

Neutral: The Hypothesis could be true or false based on the Premise. The Premise does not provide enough information to determine the truth of the Hypothesis. This often includes new, unrelated, or speculative information.

Instructions:

Read both sentences carefully.
Determine whether the Hypothesis is a necessary consequence, a contradiction, or logically independent of the Premise.
Avoid making assumptions beyond the given information.
Output Format:
Answer: [entailment | contradiction | neutral]
Explanation: A clear justification for your choice, referring to specific parts of both sentences and any logical reasoning used.

Examples:
Premise: "A man is playing the guitar."
Hypothesis: "A man is performing music."
Answer: entailment
Explanation: Playing the guitar is a form of performing music, so the hypothesis logically follows from the premise.

Premise: "A man is playing the guitar."
Hypothesis: "A man is swimming."
Answer: contradiction
Explanation: The man cannot be playing the guitar and swimming at the same time, so the statements are logically incompatible.

Premise: "A man is playing the guitar."
Hypothesis: "A man is outdoors."
Answer: neutral
Explanation: The location is not specified in the premise. The man could be indoors or outdoors, so we can't determine if the hypothesis is true.
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
        "Usage: python nli-model.py <model_name> <number_of_repetitions> <test_size>"
    )
    sys.exit()

if sys.argv[1] == "--help":
    print(
        "Usage: python nli-model.py <model_name> <number_of_repetitions> <test_size>"
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

if model_name not in get_models():
    print("Invalid model name. Please provide a valid model name.")
    sys.exit()

number_of_repetitions = int(sys.argv[2])

try:
    number_of_rows = int(sys.argv[3])
except:
    number_of_rows = 500

if number_of_rows <= 0 or number_of_rows > 500:
    print("Invalid number of rows. Converting to 500.")
    number_of_rows = 500

try:
    # Load the test data
    read_columns = ['sentence1', 'sentence2', 'gold_label']
    test_data = pd.read_json(
        os.path.join(datasets_path, "snli", "snli_1.0", "snli_1.0_test_batch.jsonl"), 
        lines=True,
        nrows=number_of_rows
    )[read_columns]
except:
    print("Error loading the test data.")
    sys.exit()

client = ollama.Client()

exception_count = 0
log_file_name = f"{model_name}_nli_model_logs.csv"
log_file = open(os.path.join(logs_path, log_file_name), "w")

# Evaluate the model
results = pd.DataFrame(columns=["sentence1", "sentence2", "result", "gold_label"])
print(f'Using the prompt: {prompt}', flush=True)
for index, row in test_data.iterrows():
    if index == number_of_rows:
        break
    print(f"Evaluating index {index+1}...", flush=True)

    query = f'{prompt} \nPremise: {row["sentence1"]} \nHypothesis: {row["sentence2"]}'
    print(f'Premise: {row["sentence1"]} Hypothesis: {row["sentence2"]}', flush=True)
    repetition_results = {"result": ''}
    answers = []

    for i in range(number_of_repetitions):
        print(f"Repetition {i+1}...", flush=True)
        exception_ = False
        response = client.generate(model_name, query).response
        try:
            if "</think>" in response:
                response = response.split("</think>")[1]
            answer = response.split("Answer: ")[1].split('\n')[0].strip().lower()
            answers.append(answer)
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

    counter = Counter(answers)
    try:
        repetition_results["result"] = counter.most_common(1)[0][0]
    except:
        exception_count += 1
        repetition_results["result"] = "error"
        # log the error
        log_file.write(
            f"Error: {index} - {repetition_results['result']}\n"
        )
        log_file.flush()        

    results = pd.concat(
        [
            results,
            pd.DataFrame(
                {
                    "sentence1": [row["sentence1"]],
                    "sentence2": [row["sentence2"]],
                    "result": [repetition_results["result"]],
                    "gold_label": [row["gold_label"].strip().lower()],
                }
            ),
        ],
        ignore_index=True,
    )

results.to_csv(
    os.path.join(
        output_path,
        f"{model_name}_nli_model_answers.csv",
    )
)
print(f"Results saved to {output_path}/{model_name}_nli_model_answers.csv.", flush=True)