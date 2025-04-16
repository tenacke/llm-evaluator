import os
import sys

import pandas as pd

if len(sys.argv) != 5:
    print(
        "Usage: python correlation.py <model_name> <datafile-name> <base_data_path> <test_data_path>"
    )
    sys.exit(1)

model_name = sys.argv[1]
datafile_name = sys.argv[2]
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
    os.path.join(base_path, f"{datafile_name}.csv"),
    # usecols=["gold_label", "result"],
)

test_df = pd.read_csv(
    os.path.join(test_path, f"{model_name}_{datafile_name}_pw.csv"),
    # usecols=["result"],
)

one_one = 0
one_two = 0
two_two = 0
two_one = 0
no_answer = 0
for i in range(len(base_df)):
    if str(base_df.iloc[i]["winner"]).strip().lower() == "model_a":
        if test_df.iloc[i]["result"] == 1:
            one_one += 1
        elif test_df.iloc[i]["result"] == 2:
            one_two += 1
        else:
            no_answer += 1
    else:
        if test_df.iloc[i]["result"] == 2:
            two_two += 1
        elif test_df.iloc[i]["result"] == 1:
            two_one += 1
        else:
            no_answer += 1
true_count = one_one + two_two
false_count = one_two + two_one

# # Calculate precision, recall, and F-score
# precision = (
#     true_positive / (true_positive + false_positive)
#     if (true_positive + false_positive) > 0
#     else 0
# )
# recall = (
#     true_positive / (true_positive + false_negative)
#     if (true_positive + false_negative) > 0
#     else 0
# )
# f_score = (
#     2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
# )

# print(f"Evaluation of {nli_model_name} using {model_name}")
# print("\nConfusion Matrix:")
# print("-" * 41)
# print("|" + " " * 17 + "|     Predicted       |")
# print("|" + " " * 17 + "| Positive | Negative |")
# print("|" + "-" * 39 + "|")
# print(f"| Actual Positive | {true_positive:8} | {false_negative:8} |")
# print(f"| Actual Negative | {false_positive:8} | {true_negative:8} |")
# print("-" * 41)
# print(f"\nPrecision: {precision:.4f}")
# print(f"Recall: {recall:.4f}")
# print(f"F-score: {f_score:.4f}")

print(f"1: {one_one + one_two}")
print(f"2: {two_one + two_two}")
print(f"1-2: {one_two}")
print(f"2-1: {two_one}")
print(f"1-1: {one_one}")
print(f"2-2: {two_two}")
print(f"no_answer: {no_answer}")
print(f"Accuracy: {true_count / len(base_df) * 100:.2f}%")