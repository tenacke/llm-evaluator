import os
import sys
import pandas as pd

datasets_path = os.path.join(os.path.dirname(__file__), "datasets")

if not os.path.exists(datasets_path):
    os.makedirs(datasets_path)

if  len(sys.argv) != 3:
    print(
        "Usage: python dataset.py <datafile-name> <outputfile-name>"
    )
    sys.exit(1)

if sys.argv[1] == "--help":
    print(
        "Usage: python dataset.py <datafile-name> <outputfile-name>"
    )
    sys.exit()

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

try:
    input_df = pd.read_csv(os.path.join(datasets_path, f"{input_file_name}.csv"))
except FileNotFoundError:
    print(f"File {input_file_name}.csv not found in {datasets_path}")
    sys.exit(1)

# Check if the CSV file is empty
if input_df.empty:
    print(f"The CSV file {input_file_name}.csv is empty.")
    sys.exit(1)

# Remove all the data without "tr-en" or "en-tr" in the "lp" column
input_df = input_df[
    # input_df["lp"].str.contains("tr-en|en-tr", na=False)
    input_df["lp"].str.contains("en-tr", na=False)
]

# Create a new csv file with the filtered data
output_file_path = os.path.join(datasets_path, f"{output_file_name}.csv")
input_df.to_csv(output_file_path, index=False)
print(f"Filtered data saved to {output_file_path}")