import os
import sys
import ollama
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

prompt = """
You are a professional English-to-Turkish translation evaluator. You will be given two sentences:

Source sentence (English): The original English sentence.
Translated sentence (Turkish): A sentence that is claimed to be its correct translation.
Your task is to evaluate how accurate, fluent, and grammatically correct the Turkish sentence is, using the following three equally important criteria:

Evaluation Criteria:
Meaning Preservation: Does the Turkish sentence convey the full and correct meaning of the English sentence?
Fluency and Naturalness: Does the Turkish sentence sound natural and idiomatic to a native speaker?
Grammar and Spelling: Is the sentence free from grammatical errors, awkward constructions, or spelling mistakes?
Scoring (Only integers: 1 to 5):
5 (Excellent): Meaning is perfectly preserved; sentence is fluent and grammatically flawless. Professional-quality translation.
4 (Good): Small issues in word choice or fluency, but meaning is clear and no serious errors.
3 (Adequate): Understandable but has some meaning loss or unnatural phrasing. Noticeable grammatical or stylistic issues.
2 (Poor): Major meaning inaccuracies or awkward, incorrect language. Hard to read naturally.
1 (Very Poor): Completely incorrect, misleading, or incomprehensible translation.

Output Format (strictly follow this structure):
Score: [1-5]
Reason: [Clear and concise explanation citing strengths and weaknesses in terms of the three evaluation criteria]
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

if len(sys.argv) < 4:
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
# if ":" not in model_name:
#     print(
#         "Invalid model name format. Please provide a valid model name. Example: evallm:v3"
#     )
#     sys.exit()

if not (model_name in get_models() or model_name == "gpt-4o-mini"):
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

if model_name == "gpt-4o-mini":
    api_key = os.getenv("OPENAI_API_KEY")
    print(api_key)
    client = OpenAI(api_key=api_key)
else:
    client = ollama.Client()

log_file_name = f"{model_name}_logs.csv"
log_file = open(os.path.join(logs_path, log_file_name), "w")

results = pd.DataFrame(columns=["result"])

print(f'Evaluating with prompt:\n{prompt}', flush=True)

for index, row in input_df.iterrows():
    print(f"Evaluating index {index+1}...", flush=True)
    if index == 500:
        print("Reached 1000 iterations, stopping...", flush=True)
        break
    query = prompt + f"\nSource sentence (English): {row['src']}\n" + f"Translated sentence (Turkish): {row['mt']}\n"
    repetition_results = {"result": 0}
    count = 0
    exception_ = False
    for i in range(number_of_repetitions):
        print(f"Repetition {i+1}...", flush=True, end=" ")
        if model_name == "gpt-4o-mini":
            response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "user", "content": query}
                        ],
                    ).choices[0].message.content
        else:
            response = client.generate(model_name, query).response

        try:
            if "</think>" in response:
                response = response.split("</think>")[1]
            score = response.split("Score: ")[1][0]
            print(f"Score: {score}", flush=True)
            repetition_results["result"] += int(score)
            count += 1
        except:
            print(
                f"Error parsing response index {index+1} repetition {i}",
                flush=True,
            )
            log_file.write(f'{index},{i},"{response.replace(",", ";")}"\n')
            log_file.flush()
            exception_ = True

        print(f"{index+1} is completed", flush=True)

        repetition_results["result"] /= count
        results.loc[index] = repetition_results

results.to_csv(
    os.path.join(
        output_path,
        f"{model_name}_translation.csv",
    )
)
print(f"Results saved to {output_path}/{model_name}_translation.csv.", flush=True)