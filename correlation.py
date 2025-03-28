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

metrics = ["coherence", "relevance", "fluency", "consistency"]
models = ["average", "poor", "powerful"]

csv_dir_path = os.path.join(os.path.dirname(__file__), "csv")

expert_pearson_correlations = []
expert_spearman_correlations = []

turker_pearson_correlations = []
turker_spearman_correlations = []

for model in models:
    scores_df = pd.read_csv(os.path.join(csv_dir_path, f"{model}_model.csv"))
    scores_df.drop(
        columns=[
            "Unnamed: 0",
            "filepath",
            "decoded",
            "model_id",
            "reference",
        ],
        inplace=True,
    )

    for metric in metrics:
        results_df_path = os.path.join(
            path, f"{model_name}_{metric}_{model}_results.csv"
        )
        if not os.path.exists(results_df_path):
            print(f"File {results_df_path} does not exist")
            expert_pearson_correlations.append([model, metric, None])
            expert_spearman_correlations.append([model, metric, None])
            turker_pearson_correlations.append([model, metric, None])
            turker_spearman_correlations.append([model, metric, None])
            continue
        results_df = pd.read_csv(results_df_path)
        results_df.drop(columns=["Unnamed: 0"], inplace=True)
        result = results_df["result"]

        expert_scores = scores_df[f"expert_{metric}_score"]
        turker_scores = scores_df[f"turker_{metric}_score"]

        pearson_expert = expert_scores.corr(result, method="pearson")
        pearson_turker = turker_scores.corr(result, method="pearson")

        spearman_expert = expert_scores.corr(result, method="spearman")
        spearman_turker = turker_scores.corr(result, method="spearman")

        expert_pearson_correlations.append([model, metric, pearson_expert])
        expert_spearman_correlations.append([model, metric, spearman_expert])

        turker_pearson_correlations.append([model, metric, pearson_turker])
        turker_spearman_correlations.append([model, metric, spearman_turker])

expert_pearson_correlations_df = pd.DataFrame(
    expert_pearson_correlations, columns=["model", "metric", "pearson"]
)

expert_spearman_correlations_df = pd.DataFrame(
    expert_spearman_correlations, columns=["model", "metric", "spearman"]
)

turker_pearson_correlations_df = pd.DataFrame(
    turker_pearson_correlations, columns=["model", "metric", "pearson"]
)

turker_spearman_correlations_df = pd.DataFrame(
    turker_spearman_correlations, columns=["model", "metric", "spearman"]
)

print("Expert Pearson Correlations")
print(expert_pearson_correlations_df)

print("Expert Spearman Correlations")
print(expert_spearman_correlations_df)

print("Turker Pearson Correlations")
print(turker_pearson_correlations_df)

print("Turker Spearman Correlations")
print(turker_spearman_correlations_df)
