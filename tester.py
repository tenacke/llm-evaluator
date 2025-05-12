import os
import sys
import ollama
import pandas as pd
# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")

# You are a professional English-to-Turkish translation evaluator. You will be given two sentences:

# Source sentence (English): The original English sentence.
# Translated sentence (Turkish): A Turkish sentence that is claimed to be a faithful translation of the source.
# Your task is to assign an integer score from 1 to 5, based on the overall translation quality. You must evaluate the translation using the following three criteria, weighted equally:

# Evaluation Criteria:
# 1. Meaning Accuracy:
# - Does the Turkish sentence preserve all essential meaning of the English source sentence?
# - Are there any additions, omissions, or changes in meaning?
# 2. Fluency and Naturalness
# - Does the translation sound natural and idiomatic to a native Turkish speaker?
# - Is it contextually and stylistically appropriate?
# 3.Grammar, Syntax, and Spelling
# - Are there any grammatical errors, unnatural word order, or spelling mistakes?
# - Is the sentence structurally correct?

# Scoring Rubric (Only integer values allowed):
# 5 - Excellent: All meaning preserved. Fluent, natural, idiomatic Turkish. No grammar or spelling errors. Comparable to professional human translation.
# 4 - Good: Meaning preserved. Minor issues in fluency or grammar that do not significantly impact readability.
# 3 - Fair: Understandable, but there are clear issues with fluency, grammar, or partial meaning loss.
# 2 - Poor: Significant issues with accuracy, fluency, or grammar. Translation may be hard to follow.
# 1 - Unacceptable: Translation is misleading, incorrect, or incoherent. Does not preserve the original meaning.

# Common Error Types to Consider:
# - Meaning distortion due to incorrect translation
# - Missing or added information not present in the source
# - Word-for-word or literal phrasing that sounds unnatural
# - Grammar mistakes (e.g., verb tense, case, agreement)
# - Unidiomatic or awkward expressions
# - Spelling or punctuation errors


# You are a professional English-to-Turkish translation evaluator. You will be given two sentences:

# Source sentence (English): The original English sentence.
# Translated sentence (Turkish): A sentence that is claimed to be its correct translation.
# Your task is to evaluate how accurate, fluent, and grammatically correct the Turkish sentence is, using the following three equally important criteria:

# Evaluation Criteria:
# Meaning Preservation: Does the Turkish sentence convey the full and correct meaning of the English sentence?
# Fluency and Naturalness: Does the Turkish sentence sound natural and idiomatic to a native speaker?
# Grammar and Spelling: Is the sentence free from grammatical errors, awkward constructions, or spelling mistakes?
# Scoring (Only integers: 1 to 5):
# 5 (Excellent): Meaning is perfectly preserved; sentence is fluent and grammatically flawless. Professional-quality translation.
# 4 (Good): Small issues in word choice or fluency, but meaning is clear and no serious errors.
# 3 (Adequate): Understandable but has some meaning loss or unnatural phrasing. Noticeable grammatical or stylistic issues.
# 2 (Poor): Major meaning inaccuracies or awkward, incorrect language. Hard to read naturally.
# 1 (Very Poor): Completely incorrect, misleading, or incomprehensible translation.

# Return your output in this format:
# Score: [number between 1 and 5]
# Reason: [Brief explanation of your decision]
prompt = """
You are a professional English-to-Turkish translation evaluator. You will be given two sentences:

Source sentence (English): The original English sentence.
Translated sentence (Turkish): A sentence that is claimed to be its correct translation.
Your task is to evaluate how accurate, fluent, and grammatically correct the Turkish sentence is, using the following three equally important criteria:

Evaluation Criteria:

1. Meaning Preservation: 
- Does the Turkish sentence convey the full and correct meaning of the English sentence?
- Are there any additions, omissions, or changes in meaning?
2. Fluency and Naturalness:
- Does the Turkish sentence sound idiomatic, natural, and fluent to a native speaker?
- Would a Turkish reader find the sentence stylistically appropriate and contextually coherent?
3. Grammar and Spelling:
- Is the sentence free from grammar errors, unnatural constructions, incorrect word order, or spelling mistakes?
- Is the sentence structurally well-formed and professionally written?

Scoring (Only integers: 1 to 5):
5 (Excellent):
- Meaning is perfectly preserved.
- The sentence is fluent, idiomatic, and natural to a native speaker.
- No grammatical, stylistic, or spelling errors.
- All three criteria (meaning, fluency, grammar) are fully satisfied.
4 (Good):
- The meaning is accurately preserved.
- The sentence reads naturally overall, but there may be minor fluency or style issues.
- One minor grammar or phrasing issue may be present, but it does not affect understanding.
- Satisfies all three criteria, with only minor flaws.
3 (Adequate):
- The sentence is understandable, but some meaning may be lost or slightly distorted.
- Fluency may be uneven, and parts of the sentence may feel unnatural or awkward.
- Grammar or spelling issues are noticeable but do not render the sentence incomprehensible.
- At least one of the three criteria is weakly satisfied.
2 (Poor):
- Meaning is partially preserved but with significant loss, distortion, or ambiguity.
- The sentence reads unnaturally and may be difficult for a native speaker to process smoothly.
- Contains major grammatical issues or multiple minor ones that affect readability.
- At most one criterion is moderately satisfied.
1 (Very Poor):
- The translation is misleading, severely inaccurate, or mostly incomprehensible.
- Meaning is not preserved.
- The sentence is ungrammatical, unnatural, and difficult or impossible to understand.
- Fails to meet any of the three evaluation criteria.

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

        if not exception_:
            print(f"Successfully evaluated index {index+1}", flush=True)

        repetition_results["result"] /= count
        results.loc[index] = repetition_results

results.to_csv(
    os.path.join(
        output_path,
        f"{model_name}_translation.csv",
    )
)
print(f"Results saved to {output_path}/{model_name}_translation.csv.", flush=True)