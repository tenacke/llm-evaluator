import os
import sys
import pandas as pd

import ollama


def get_models():
    return [model.model for model in ollama.list().models]


# Get the path to the datasets folder
datasets_path = os.path.join(os.path.dirname(__file__), "datasets")
csv_files_path = os.path.join(os.path.dirname(__file__), "csv")

# Check if command line arguments are provided
if len(sys.argv) < 4:
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
if model_name not in get_models():
    print("Invalid model name. Please provide a valid model name.")
    sys.exit()


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
exception_file = open(
    f"{model_name.split(':')[1]}_{evaluation_type}_exceptions.txt", "w"
)

# Evaluate the model
results = pd.DataFrame(columns=["coherence", "fluency", "relevance", "consistency"])
for index, row in test_data.iterrows():
    print(f"Evaluating index {index+1}...")

    text_file = row["filepath"]
    with open(os.path.join(datasets_path, text_file), "r") as f:
        text = f.read()

    query = "Summary\n" + row["decoded"] + "\n\nText\n" + text

    repetition_results = {
        "coherence": 0,
        "fluency": 0,
        "relevance": 0,
        "consistency": 0,
    }
    count = 0
    for i in range(number_of_repetitions):
        print(f"Repetition {i+1}...")
        response = client.generate(model_name, query).response

        try:
            coherence = response.split("Coherence: ")[1][0]
            fluency = response.split("Fluency: ")[1][0]
            relevance = response.split("Relevance: ")[1][0]
            consistency = response.split("Consistency: ")[1][0]

            repetition_results["coherence"] += int(coherence)
            repetition_results["fluency"] += int(fluency)
            repetition_results["relevance"] += int(relevance)
            repetition_results["consistency"] += int(consistency)

            count += 1
        except:
            print(f"Error parsing response index {index} repetition {i}")
            exception_file.write(f'{index},{i},"{response.replace(",", ";")}"\n')
            exception_count += 1
            exception_file.flush()

    if count == 3:
        print(f"Successfully evaluated index {index+1}")

    for key in repetition_results:
        repetition_results[key] /= count

    results.loc[index] = repetition_results

results.to_csv(
    os.path.join(
        csv_files_path, f"{model_name.split(':')[1]}_{evaluation_type}_results.csv"
    )
)
print("Results saved to csv file.")
