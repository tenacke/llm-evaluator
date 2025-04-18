import os
import sys
import ollama
import pandas as pd
# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")


prompt = """
You are given a Natural Language Inference (NLI) task output to evaluate. You will receive:

- A premise: the original statement
- A hypothesis: a statement that may or may not logically follow from the premise
- An answer: the model's predicted relationship between the premise and the hypothesis ("entailment", "contradiction", or "neutral")

Below you can see the definitions and examples for each one of the possible answers

Entailment: The Hypothesis is a logical consequence of the Premise. The information in the Hypothesis must be true if the Premise is true. (E.g., specific to general, part to whole, synonyms, paraphrasing)
Contradiction: The Hypothesis directly conflicts with the Premise. If the Premise is true, the Hypothesis cannot be true. (E.g., opposite meanings, factual disagreements, mutually exclusive statements)
Neutral: The Hypothesis is plausible but not guaranteed by the Premise. The Premise provides insufficient information to determine the truth of the Hypothesis. (E.g., additional details, unrelated content, implications that are not certain)

Your task is to evaluate the model's answer and return "True" if the answer is correct and "False" if the answer is incorrect. You should also provide an explanation of why the answer is correct or incorrect, based strictly on the logical relationship between the premise and hypothesis.

Example 1:

Premise: "A woman is running a marathon."
Hypothesis: "A woman is engaging in a physical activity."
Answer: Entailment
Explanation: The hypothesis is a logical consequence of the premise. Running a marathon is a form of physical activity. The broader category of "physical activity" includes activities such as running, so the hypothesis follows logically. Therefore, you should return "True" if the answer is "entailment" and "False" if any other answer is given.

Example 2:

Premise: "A cat is sleeping on the sofa."
Hypothesis: "A cat is chasing a mouse."
Answer: Contradiction
Explanation: The hypothesis describes an activity that directly contradicts the premise. Sleeping and chasing are mutually exclusive actions; a cat cannot be doing both simultaneously. Therefore, you should return "True" if the answer is "contradiction" and "False" if any other answer is given.

Example 3:

Premise: "A man is playing the piano at a concert."
Hypothesis: "The man is famous."
Answer: Neutral
Explanation: The premise provides no information about the man's fame. Playing the piano at a concert does not necessarily imply fame; it could be a local or amateur performance. Therefore, the hypothesis is neither entailed nor contradicted by the premise. So, you should return "True" if the answer is "neutral" and "False" if any other answer is given.

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

if len(sys.argv) != 4:
    print(
        "Usage: python tester.py <model_name> <nli-model> <number_of_repetitions>"
    )
    sys.exit(1)

if sys.argv[1] == "--help":
    print(
        "Usage: python tester.py <model_name> <nli-model> <number_of_repetitions>"
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

# path = sys.argv[3]

# path = os.path.join(os.path.dirname(__file__), path)
# if not os.path.exists(path):
#     print(f"Path {path} does not exist")
#     sys.exit(1)

number_of_repetitions = int(sys.argv[3])

try:
    model_answers_df = pd.read_csv(os.path.join(csv_files_path, f"{nli_model}_nli_model_answers.csv"))
except FileNotFoundError:
    print(f"File {nli_model}_nli_model_answers.csv not found in {csv_files_path}")
    sys.exit(1)

client = ollama.Client()

log_file_name = f"{model_name}_nli_tester_logs.csv"
log_file = open(os.path.join(logs_path, log_file_name), "w")

results = pd.DataFrame(columns=["result"])

print(f'Evaluating with prompt:\n{prompt}', flush=True)

for index, row in model_answers_df.iterrows():
    print(f"Evaluating index {index+1}...", flush=True)
    
    query = f'{prompt}\nPremise: {row["sentence1"]}\nHypothesis: {row["sentence2"]}\nAnswer of model: {row["result"]}'
    repetition_results = {"result": ''}
    exception_count = 0
    true_count = 0
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
            exception_count += 1

    if exception_count < number_of_repetitions:
        print(f"Successfully evaluated index {index+1}", flush=True)

    print(f"True count: {true_count}", flush=True)
    threshold = (number_of_repetitions - exception_count) / 2
    if true_count >= threshold:  # favors true
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