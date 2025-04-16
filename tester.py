import os
import sys
import ollama
import pandas as pd
# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")


prompt = """
You are given a question and two different answers provided by two separate AI models. Your task is to carefully compare both answers and decide which one is better.
You should consider the following criteria in your evaluation:

Relevance: How well does the answer address the question?
Correctness: Is the answer factually and logically accurate?
Clarity: Is the answer clear, well-structured, and easy to understand?
Depth: Does the answer show reasoning or deeper insight when appropriate?
Please return your judgment in the following format:

Better Answer: [Answer 1 / Answer 2]
Reason: [A detailed explanation of why you chose that answer, referring to the criteria above]
Here is the input:
"""

def get_models():
    return [model.model for model in ollama.list().models]

# Get the path to the datasets folder
datasets_arena_path = os.path.join(os.path.dirname(__file__), "datasets", "arena")
csv_files_path = os.path.join(os.path.dirname(__file__), "csv")
logs_path = os.path.join(os.path.dirname(__file__), "logs")
output_path = os.path.join(os.path.dirname(__file__), "output")
if not os.path.exists(csv_files_path):
    os.makedirs(csv_files_path)
if not os.path.exists(logs_path):
    os.makedirs(logs_path)
if not os.path.exists(output_path):
    os.makedirs(output_path)

if len(sys.argv) != 4:
    print(
        "Usage: python tester.py <model_name> <datafile-name> <number_of_repetitions>"
    )
    sys.exit(1)

if sys.argv[1] == "--help":
    print(
        "Usage: python tester.py <model_name> <datafile-name> <number_of_repetitions>"
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

datafile_name = sys.argv[2]

try:
    number_of_repetitions = int(sys.argv[3])
except:
    print(
        "Number of repetitions should be an integer"
    )
    sys.exit()

try:
    input_df = pd.read_csv(os.path.join(datasets_arena_path, f"{datafile_name}.csv"))
except FileNotFoundError:
    print(f"File {datafile_name}.csv not found in {datasets_arena_path}")
    sys.exit(1)

client = ollama.Client()

log_file_name = f"{model_name}_{datafile_name}_logs.csv"
log_file = open(os.path.join(logs_path, log_file_name), "w")

results = pd.DataFrame(columns=["result"])

print(f'Evaluating with prompt:\n{prompt}', flush=True)

for index, row in input_df.iterrows():
    print(f"Evaluating index {index+1}...", flush=True)
    
    query = f'{prompt}\nQuestion: {row["question"]}\nAnswer 1: {row["answer_a"]}\nAnswer 2: {row["answer_b"]}'
    repetition_results = {"result": 0}
    one_count = 0
    exception_count = 0
    for i in range(number_of_repetitions):
        print(f"Repetition {i+1}...", flush=True, end=" ")

        # response = openai.ChatCompletion.create(
        #             model="gpt-4o",
        #             messages=[
        #                 {"role": "user", "content": query}
        #             ],
        #             temperature=0.0
        #         )["choices"][0]["message"]["content"]

        response = client.generate(model_name, query).response

        try:
            if "</think>" in response:
                response = response.split("</think>")[1]
            answer = response.split("Better Answer: ")[1].split('\n')[0].strip().lower()
            if "1" in answer:
                one_count += 1
        except:
            print(
                f"Error parsing response index {index+1} repetition {i}",
                flush=True,
            )
            log_file.write(f'{index},{i},"{response.replace(",", ";")}"\n')
            log_file.flush()
            exception_count += 1

    if exception_count < number_of_repetitions:
        print(f"Successfully evaluated index {index+1}", flush=True)
    else:
        print(f"Failed to evaluate index {index+1}", flush=True)
        results.loc[index] = 0
        continue
    
    threshold = (number_of_repetitions - exception_count) / 2
    
    if one_count > threshold: # favor answer 2 in case of tie
        results.loc[index] = 1
    else:
        results.loc[index] = 2

results.to_csv(
    os.path.join(
        output_path,
        f"{model_name}_{datafile_name}_pw.csv",
    )
)
print(f"Results saved to {output_path}/{model_name}_{datafile_name}_pw.csv.", flush=True)