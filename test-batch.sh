#!/bin/bash
#SBATCH --job-name=nli
#SBATCH --container-image ghcr.io\#tenacke/llm-evaluator:latest-container
#SBATCH --container-mounts=/users/bilge.guneyli/llm-evaluator/output:/opt/llm-evaluator/output,/users/bilge.guneyli/llm-evaluator/logs:/opt/llm-evaluator/logs
#SBATCH --time=24:00:00
#SBATCH --cpus-per-task=8
#SBATCH --mem=4G

source /opt/llm-evaluator/venv/bin/activate
git fetch --all && \
git add entrypoint.sh && \
git commit -m "Update entrypoint.sh" && \
git checkout kaan-nli && \
git pull origin kaan-nli

python3 tester.py llama3.1:70b llama3.1:70b 3 #&& \
# python3 tester.py llama3.1:70b roberta 3 && \
# python3 tester.py llama3.1:70b deberta 3 && \
# python3 tester.py llama3.1:70b random 3 



