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

base_file = os.path.join(base_path, f"{datafile_name}.csv")
print(f"Base file: {base_file}")
base_df = pd.read_csv(base_file)

test_file = os.path.join(test_path, f"{model_name}_{datafile_name}_pw.csv")
print(f"Test file: {test_file}")
test_df = pd.read_csv(test_file)

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

print(f"model chose 1: {two_one + one_one}")
print(f"model chose 2: {one_two + two_two}")
print(f"1-2: {one_two}")
print(f"2-1: {two_one}")
print(f"1-1: {one_one}")
print(f"2-2: {two_two}")
print(f"no_answer: {no_answer}")
print(f"Accuracy: {true_count / len(base_df) * 100:.2f}%")