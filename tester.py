import os
import sys
import pandas as pd

import ollama


def get_models():
    return [model.model for model in ollama.list().models]


# Get the path to the datasets folder
datasets_path = os.path.join(os.path.dirname(__file__), "datasets")
csv_files_path = os.path.join(os.path.dirname(__file__), "csv")
logs_path = os.path.join(os.path.dirname(__file__), "logs")
if not os.path.exists(csv_files_path):
    os.makedirs(csv_files_path)
if not os.path.exists(logs_path):
    os.makedirs(logs_path)

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
model_base_name = model_name.split(":")[0]
model_version = model_name.split(":")[1]

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

model_name = f"{model_base_name}-{metric}:{model_version}"
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
log_file_name = f"{model_version}_{metric}_{evaluation_type}_logs.csv"
log_file = open(os.path.join(logs_path, log_file_name), "w")

# Evaluate the model
results = pd.DataFrame(columns=["result"])
for index, row in test_data.iterrows():
    print(f"Evaluating index {index+1}...", flush=True)

    text_file = row["filepath"]
    with open(os.path.join(datasets_path, text_file), "r") as f:
        text = f.read()

    query = "Summary\n" + row["decoded"] + "\n\nText\n" + text

    repetition_results = {"result": 0}
    count = 0
    for i in range(number_of_repetitions):
        print(f"Repetition {i+1}...", flush=True)
        exception_ = False
        response = client.generate(model_name, query).response
        log_file.write(f'{index},{i},"{response.replace(",", ";")}"\n')
        log_file.flush()
        try:
            if "</think>" in response:
                response = response.split("</think>")[1]
            coherence = response.split("Score: ")[1][0]
            repetition_results["result"] += int(coherence)
            count += 1
        except:
            print(
                f"Error parsing response index {index} repetition {i}",
                flush=True,
            )
            exception_ = True

    if not exception_:
        print(f"Successfully evaluated index {index+1}", flush=True)

    repetition_results["result"] /= count

    results.loc[index] = repetition_results

results.to_csv(
    os.path.join(
        csv_files_path,
        f"{model_version}_{metric}_{evaluation_type}_results.csv",
    )
)
print("Results saved to csv file.", flush=True)
