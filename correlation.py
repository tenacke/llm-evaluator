import os
import sys
import pandas as pd

if len(sys.argv) < 4:
    print(
        "Usage: python correlation.py <model_name> <dataset_file> <output_file>"
    )
    sys.exit(1)

model_name = sys.argv[1]
dataset_file_name = sys.argv[2]
output_file_name = sys.argv[3]

datasets_path = os.path.join(os.path.dirname(__file__), "datasets")
output_path = os.path.join(os.path.dirname(__file__), "output")

data_file = os.path.join(datasets_path, f"{dataset_file_name}.csv")
if not os.path.exists(data_file):
    print(f"File {dataset_file_name}.csv not found in {datasets_path}")
    sys.exit(1)
data_df = pd.read_csv(data_file)


output_file = os.path.join(output_path, f"{model_name}_translation.csv")
if not os.path.exists(output_file):
    print(f"File {model_name}_translation.csv not found in {output_path}")
    sys.exit(1)
output_df = pd.read_csv(output_file)

pearson_correlations = []
spearman_correlations = []

output_scores = output_df["result"]
data_scores = pd.cut(
    data_df['raw'],
    bins=[0, 20, 40, 60, 80, 100],
    labels=[1, 2, 3, 4, 5],
    include_lowest=True
).astype(int)
  
pearson = data_scores.corr(output_scores, method="pearson")

spearman = data_scores.corr(output_scores, method="spearman")

print(f"Pearson correlation: {pearson}")
print(f"Spearman correlation: {spearman}")
# pearson_correlations_df = pd.DataFrame(
#     pearson_correlations, columns=["model", "pearson"]
# )

# spearman_correlations_df = pd.DataFrame(
#     spearman_correlations, columns=["model", "spearman"]
# )

# print("Spearman Correlations")
# print(spearman_correlations_df)

# print("Pearson Correlations")
# print(pearson_correlations_df)
