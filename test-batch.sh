#!/bin/bash
#SBATCH --job-name=test-nli
#SBATCH --container-image ghcr.io\#tenacke/llm-evaluator:latest-container
#SBATCH --container-mounts=/users/bilge.guneyli/llm-evaluator/output:/opt/llm-evaluator/output,/users/bilge.guneyli/llm-evaluator/logs:/opt/llm-evaluator/logs
#SBATCH --time=08:00:00
#SBATCH --cpus-per-task=8
#SBATCH --mem=4G

source /opt/llm-evaluator/venv/bin/activate
git fetch --all && \
git add entrypoint.sh && \
git commit -m "Update entrypoint.sh" && \
git checkout kaan-nli && \
git pull origin kaan-nli

python3 tester.py deepseek-r1:32b roberta output 3 
python3 tester.py deepseek-r1:32b deberta output 3 
python3 tester.py deepseek-r1:32b random output 3 



