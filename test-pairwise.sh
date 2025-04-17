#!/bin/bash
#SBATCH --job-name=pairwise
#SBATCH --container-image ghcr.io\#tenacke/llm-evaluator:latest-container
#SBATCH --container-mounts=/users/bilge.guneyli/llm-evaluator/output:/opt/llm-evaluator/output,/users/bilge.guneyli/llm-evaluator/logs:/opt/llm-evaluator/logs
#SBATCH --time=24:00:00
#SBATCH --cpus-per-task=8
#SBATCH --mem=4G

source /opt/llm-evaluator/venv/bin/activate
git fetch --all && \
git checkout pairwise-emre && \
git pull origin pairwise-emre

python3 tester.py llama3.1:70b random_200 3 && \
python3 tester.py llama3.1:70b vicukoala_100 3 && \
python3 tester.py llama3.1:70b vicukoala_100_swapped 3



