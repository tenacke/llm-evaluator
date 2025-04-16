import os
import sys

import pandas as pd

if len(sys.argv) != 5:
    print(
        "Usage: python correlation.py <model_name> <nli_model_name> <base_data_path> <test_data_path>"
    )
    sys.exit(1)

model_name = sys.argv[1]
nli_model_name = sys.argv[2]
base_path = sys.argv[3]
test_path = sys.argv[4]

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
    os.path.join(base_path, f"{nli_model_name}_nli_model_answers.csv"),
    usecols=["gold_label", "result"],
)

# new column: true if other two columns are the same, false otherwise
base_df["tf"] = base_df.apply(
    lambda row: str(row["gold_label"]).strip().lower()
    == str(row["result"]).strip().lower(),
    axis=1,
)

test_df = pd.read_csv(
    os.path.join(test_path, f"{model_name}_{nli_model_name}_nli_results.csv"),
    usecols=["result"],
)

true_positive = 0
true_negative = 0
false_positive = 0
false_negative = 0
for i in range(len(base_df)):
    if str(base_df.iloc[i]["tf"]).strip().lower() == "true":
        if str(test_df.iloc[i]["result"]).strip().lower() == "true":
            true_positive += 1
        else:
            false_negative += 1
    else:
        if str(test_df.iloc[i]["result"]).strip().lower() == "true":
            false_positive += 1
        else:
            true_negative += 1
true_count = true_positive + true_negative
false_count = false_positive + false_negative

# Calculate precision, recall, and F-score
precision = (
    true_positive / (true_positive + false_positive)
    if (true_positive + false_positive) > 0
    else 0
)
recall = (
    true_positive / (true_positive + false_negative)
    if (true_positive + false_negative) > 0
    else 0
)
f_score = (
    2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
)

print(f"Evaluation of {nli_model_name} using {model_name}")
print("\nConfusion Matrix:")
print("-" * 41)
print("|" + " " * 17 + "|     Predicted       |")
print("|" + " " * 17 + "| Positive | Negative |")
print("|" + "-" * 39 + "|")
print(f"| Actual Positive | {true_positive:8} | {false_negative:8} |")
print(f"| Actual Negative | {false_positive:8} | {true_negative:8} |")
print("-" * 41)
print(f"\nPrecision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F-score: {f_score:.4f}")

print(f"Accuracy: {true_count / len(base_df) * 100:.2f}%")
