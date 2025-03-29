#!/bin/bash
#SBATCH --job-name=powerful-test
#SBATCH --container-image ghcr.io\#tenacke/llm-evaluator:latest-container
#SBATCH --container-mounts=/users/bilge.guneyli/llm-evaluator/output:/opt/llm-evaluator/output,/users/bilge.guneyli/llm-evaluator/logs:/opt/llm-evaluator/logs
#SBATCH --time=08:00:00
#SBATCH --cpus-per-task=8
#SBATCH --mem=4G

source /opt/llm-evaluator/venv/bin/activate
git fetch --all && \
git add entrypoint.sh && \
git commit -m "Update entrypoint.sh" && \
git checkout kaan-container && \
git pull origin kaan-container

python3 models/v3/model_test.py && \
python3 tester.py llama3.1:70b powerful 3 coherence && \
python3 tester.py llama3.1:70b powerful 3 fluency && \
python3 tester.py llama3.1:70b powerful 3 relevance && \
python3 tester.py llama3.1:70b powerful 3 consistency 



