import os
import sys
import pandas as pd
import ollama
from collections import Counter

prompt = """
You are given two sentences: a Premise and a Hypothesis. Your task is to determine the logical relationship between these two sentences and provide a well-reasoned explanation for your decision. The relationship can be one of the following:

Entailment: The Hypothesis is a logical consequence of the Premise. The information in the Hypothesis must be true if the Premise is true. (E.g., specific to general, part to whole, synonyms, paraphrasing)
Contradiction: The Hypothesis directly conflicts with the Premise. If the Premise is true, the Hypothesis cannot be true. (E.g., opposite meanings, factual disagreements, mutually exclusive statements)
Neutral: The Hypothesis is plausible but not guaranteed by the Premise. The Premise provides insufficient information to determine the truth of the Hypothesis. (E.g., additional details, unrelated content, implications that are not certain)
Response Format:
Answer: [entailment | contradiction | neutral]
Explanation: Explain your reasoning clearly, identifying any clues or keywords that helped you make the decision. Provide logical steps and reference any implicit knowledge or assumptions used.
Examples:
Example 1:

Premise: "A woman is running a marathon."
Hypothesis: "A woman is engaging in a physical activity."
Answer: Entailment
Explanation: The hypothesis is a logical consequence of the premise. Running a marathon is a form of physical activity. The broader category of "physical activity" includes activities such as running, so the hypothesis follows logically.
Example 2:

Premise: "A cat is sleeping on the sofa."
Hypothesis: "A cat is chasing a mouse."
Answer: Contradiction
Explanation: The hypothesis describes an activity that directly contradicts the premise. Sleeping and chasing are mutually exclusive actions; a cat cannot be doing both simultaneously.
Example 3:

Premise: "A man is playing the piano at a concert."
Hypothesis: "The man is famous."
Answer: Neutral
Explanation: The premise provides no information about the man's fame. Playing the piano at a concert does not necessarily imply fame; it could be a local or amateur performance. Therefore, the hypothesis is neither entailed nor contradicted by the premise.
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
        "Usage: python tester.py <model_name> <number_of_repetitions> <test_size>"
    )
    sys.exit()

if sys.argv[1] == "--help":
    print(
        "Usage: python tester.py <model_name> <number_of_repetitions> <test_size>"
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
    read_columns = ['sentence1', 'sentence2']
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
log_file_name = f"{model_name}_nli_logs.csv"
log_file = open(os.path.join(logs_path, log_file_name), "w")

# Evaluate the model
results = pd.DataFrame(columns=["result"])
print(f'Using the prompt: {prompt}', flush=True)
for index, row in test_data.iterrows():
    if index == number_of_rows:
        break
    print(f"Evaluating index {index+1}...", flush=True)

    query = f'{prompt} \nPremise: {row["sentence1"]} \nHypothesis: {row["sentence2"]}'
    print(f'Premise: {row["sentence1"]} Hypothesis: {row["sentence2"]}', flush=True)
    repetition_results = {"result": ''}

    for i in range(number_of_repetitions):
        print(f"Repetition {i+1}...", flush=True)
        exception_ = False
        response = client.generate(model_name, query).response
        answers = []
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

    results.loc[index] = repetition_results

results.to_csv(
    os.path.join(
        output_path,
        f"{model_name}_nli_results.csv",
    )
)
print("Results saved to csv file.", flush=True)