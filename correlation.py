import os
import sys

import pandas as pd

if len(sys.argv) < 3:
    print("Usage: python correlation.py <model_name> <path>")
    sys.exit(1)

model_name = sys.argv[1]
path = sys.argv[2]

path = os.path.join(os.path.dirname(__file__), path)
if not os.path.exists(path):
    print(f"Path {path} does not exist")
    sys.exit(1)


csv_dir_path = os.path.join(os.path.dirname(__file__), "csv")
datasets_path = os.path.join(os.path.dirname(__file__), "datasets")

model_answers_df = pd.read_csv(os.path.join(path, f"{model_name}_nli_results.csv"))
number_of_rows = len(model_answers_df)

read_columns = ['annotator_labels', 'sentence1', 'sentence2']
real_answers_df = pd.read_json(
        os.path.join(datasets_path, "snli", "snli_1.0", "snli_1.0_train.jsonl"), 
        lines=True,
        nrows=number_of_rows
    )

true_count = 0
for i in range(len(model_answers_df)):
    print(f'{real_answers_df.iloc[i]["sentence1"]} vs. {real_answers_df.iloc[i]["sentence2"]}')
    print(f'{i}: {model_answers_df.iloc[i]["result"]} vs. {real_answers_df.iloc[i]["annotator_labels"][0].strip().lower()}' )
    if model_answers_df.iloc[i]["result"] == real_answers_df.iloc[i]["annotator_labels"][0].strip().lower():
        true_count += 1

print(f"Correctly gueesed {true_count} out of {number_of_rows} answers")
print(
    f"Accuracy: {true_count / number_of_rows * 100:.2f}%"
)