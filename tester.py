import os
import sys
import ollama
import pandas as pd

prompt = """
You are given a Natural Language Inference (NLI) task output to evaluate. You will receive:

- A premise: the original statement
- A hypothesis: a statement that may or may not logically follow from the premise
- An answer: the model's predicted relationship between the premise and the hypothesis ("entailment", "contradiction", or "neutral")

Your task is to evaluate whether the answer is correct or not, and explain your reasoning.

Return your output in the following format:

Answer: [True/False]  
Reason: [Your explanation why the answer is correct or incorrect, based strictly on the logical relationship between the premise and hypothesis]

Here is the data:
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

if len(sys.argv) != 5:
    print(
        "Usage: python tester.py <model_name> <nli-model> <path> <number_of_repetitions>"
    )
    sys.exit(1)

if sys.argv[1] == "--help":
    print(
        "Usage: python tester.py <model_name> <nli-model> <path> <number_of_repetitions>"
    )
    sys.exit()

model_name = sys.argv[1]
if ":" not in model_name:
    print(
        "Invalid model name format. Please provide a valid model name. Example: evallm:v3"
    )
    sys.exit()

if model_name not in get_models():
    print(
        "Invalid model name. Please provide a valid model name."
    )
    sys.exit()

nli_model = sys.argv[2]

path = sys.argv[3]

path = os.path.join(os.path.dirname(__file__), path)
if not os.path.exists(path):
    print(f"Path {path} does not exist")
    sys.exit(1)

number_of_repetitions = int(sys.argv[4])

csv_dir_path = os.path.join(os.path.dirname(__file__), "csv")
datasets_path = os.path.join(os.path.dirname(__file__), "datasets")

try:
    model_answers_df = pd.read_csv(os.path.join(path, f"{nli_model}_nli_model_answers.csv"))
except FileNotFoundError:
    print(f"File {nli_model}_nli_results.csv not found in {path}")
    sys.exit(1)

client = ollama.Client()

exception_count = 0
log_file_name = f"{model_name}_nli_tester_logs.csv"
log_file = open(os.path.join(logs_path, log_file_name), "w")

treshold = number_of_repetitions / 2
results = pd.DataFrame(columns=["result"])

print(f'Evaluating with prompt:\n{prompt}', flush=True)

for index, row in model_answers_df.iterrows():
    print(f"Evaluating index {index+1}...", flush=True)
    
    query = f'{prompt}\nPremise: {row["sentence1"]}\nHypothesis: {row["sentence2"]}\nAnswer of model: {row["result"]}'
    repetition_results = {"result": ''}
    # answers = []
    true_count = 0
    for i in range(number_of_repetitions):
        print(f"Repetition {i+1}...", flush=True, end=" ")
        exception_ = False
        response = client.generate(model_name, query).response

        try:
            if "</think>" in response:
                response = response.split("</think>")[1]
            answer = response.split("Answer: ")[1].split('\n')[0].strip().lower()
            print(f"Answer: {answer}", flush=True)
            if "true" in answer:
                true_count += 1
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

    print(f"True count: {true_count}", flush=True)
    if true_count > treshold:
        results.loc[index] = 'true'
    else:
        results.loc[index] = 'false'

results.to_csv(
    os.path.join(
        output_path,
        f"{model_name}_{nli_model}_nli_results.csv",
    )
)
print(f"Results saved to {output_path}/{model_name}_{nli_model}_nli_results.csv.", flush=True)