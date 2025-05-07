import os
import sys
import ollama
import pandas as pd
# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")


# prompt_100 = """
# You are a professional translation evaluator. You will be given 2 sentences:

# - Source sentence (English): The original English sentence.
# - Translated sentence (Turkish): A sentence that is claimed to be its translation.
# Your task is to give a score from 0 to 100 as 100 being the highest, based on how good the Turkish translation is. Focus on the following:

# Does the translation accurately convey the meaning?
# - Is it fluent and natural in Turkish?
# - Are there any mistakes, unnatural phrases, or missing parts?
# - Do not just translate back into English — judge the Turkish sentence as a native Turkish speaker would.

# Use your expert judgment. A perfect or near-perfect translation would get close to 100, while incorrect, broken, or misleading translations would get a much lower score.

# Return your output in this format:
# Score: [number between 0 and 100]
# Reason: [Brief explanation of your decision]
# """

prompt_5 = """
You are a professional translation evaluator. You will be given 2 sentences:

- Source sentence (English): The original English sentence.
- Translated sentence (Turkish): A sentence that is claimed to be its translation.
Your task is to give a score from 1 to 5 as 5 being the highest, based on how good the Turkish translation is. Focus on the following:

Does the translation accurately convey the meaning?
- Is it fluent and natural in Turkish?
- Are there any mistakes, unnatural phrases, or missing parts?
- Do not just translate back into English — judge the Turkish sentence as a native Turkish speaker would.

Use your expert judgment. A perfect or near-perfect translation would get close to 5, while incorrect, broken, or misleading translations would get a lower score.

Return your output in this format:
Score: [number between 1 and 5]
Reason: [Brief explanation of your decision]
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
    input_df = pd.read_csv(os.path.join(datasets_path, f"{datafile_name}.csv"))
except FileNotFoundError:
    print(f"File {datafile_name}.csv not found in {datasets_path}")
    sys.exit(1)

client = ollama.Client()

log_file_name = f"{model_name}_logs.csv"
log_file = open(os.path.join(logs_path, log_file_name), "w")

results = pd.DataFrame(columns=["result_100", "result_5"])

print(f'Evaluating with prompt:\n{prompt_5}', flush=True)

for index, row in input_df.iterrows():
    print(f"Evaluating index {index+1}...", flush=True)
    if index == 500:
        print("Reached 1000 iterations, stopping...", flush=True)
        break
    # for i in range(2):
    #     if i == 0:
    #         query = prompt_100 + f"\nSource sentence (English): {row['src']}\n" + f"Translated sentence (Turkish): {row['mt']}\n"
    #     else:
    query = prompt_5 + f"\nSource sentence (English): {row['src']}\n" + f"Translated sentence (Turkish): {row['mt']}\n"
    repetition_results = {"result_100": 0, "result_5": 0}
    count = 0
    exception_ = False
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
            score = response.split("Score: ")[1][0]
            print(f"Score: {score}", flush=True)
            repetition_results["result_100"] = 0
            repetition_results["result_5"] += int(score)
            count += 1
        except:
            print(
                f"Error parsing response index {index+1} repetition {i}",
                flush=True,
            )
            log_file.write(f'{index},{i},"{response.replace(",", ";")}"\n')
            log_file.flush()
            exception_ = True

        if not exception_:
            print(f"Successfully evaluated index {index+1}", flush=True)

        # repetition_results["result_100"] /= count
        repetition_results["result_5"] /= count

        results.loc[index] = repetition_results

results.to_csv(
    os.path.join(
        output_path,
        f"{model_name}_translation.csv",
    )
)
print(f"Results saved to {output_path}/{model_name}_translation.csv.", flush=True)