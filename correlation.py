import os
import sys

import pandas as pd

if len(sys.argv) != 4:
    print("Usage: python correlation.py <model_name> <base_data_path> <test_data_path>")
    sys.exit(1)

model_name = sys.argv[1]
base_path = sys.argv[2]
test_path = sys.argv[3]

base_path = os.path.join(os.path.dirname(__file__), base_path)
if not os.path.exists(base_path):
    print(f"Path {base_path} does not exist")
    sys.exit(1)

test_path = os.path.join(os.path.dirname(__file__), test_path)
if not os.path.exists(test_path):
    print(f"Path {test_path} does not exist")
    sys.exit(1)

csv_dir_path = os.path.join(os.path.dirname(__file__), "csv")
datasets_path = os.path.join(os.path.dirname(__file__), "datasets")

base_df = pd.read_csv(
    os.path.join(base_path, f"{model_name}_nli_model_answers.csv"),
    usecols=['gold_label', 'result']
    )

# new column: true if other two columns are the same, false otherwise
base_df['tf'] = base_df.apply(
    lambda row: str(row["gold_label"]).strip().lower() == str(row["result"]).strip().lower(),
    axis=1
)

test_df = pd.read_csv(
    os.path.join(test_path, f"{model_name}_nli_results.csv"),
    usecols=['result']
    )

true_count = 0
for i in range(len(base_df)):
    if str(base_df.iloc[i]["tf"]).strip().lower() == str(test_df.iloc[i]["result"]).strip().lower():
        true_count += 1

print(f"Correctly guessed {true_count} out of {len(base_df)} answers")
print(
    f"Accuracy: {true_count / len(base_df) * 100:.2f}%"
)