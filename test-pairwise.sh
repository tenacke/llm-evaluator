#!/bin/bash
#SBATCH --job-name=average-test
#SBATCH --container-image ghcr.io\#tenacke/llm-evaluator:latest-container
#SBATCH --container-mounts=/users/emre.kilic/llm-evaluator/outputs:/opt/llm-evaluator/outputs,/users/emre.kilic/llm-evaluator/logs:/opt/llm-evaluator/logs
#SBATCH --time=08:00:00
#SBATCH --cpus-per-task=8
#SBATCH --mem=4G

source /opt/llm-evaluator/venv/bin/activate

python3 tester.py llama3.1:70b random_200 3 && \
python3 tester.py llama3.1:70b vicukoala_100 3 && \
python3 tester.py llama3.1:70b vicukoala_100_swapped 3



