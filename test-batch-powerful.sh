#!/bin/bash
#SBATCH --job-name=powerful-test
#SBATCH --container-image ghcr.io\#tenacke/lastest-container
#SBATCH --container-mounts=/users/bilge.guneyli/llm-evaluator/outputs:/opt/llm-evaluator/outputs,/users/bilge.guneyli/llm-evaluator/logs:/opt/llm-evaluator/logs
#SBATCH --time=08:00:00
#SBATCH --cpus-per-task=8
#SBATCH --mem=4G

source /opt/llm-evaluator/venv/bin/activate
git fetch --all && \
git checkout kaan-container && \
git pull origin kaan-container

python3 models/v3/model_test.py && \
# python3 tester.py llama3.1:70b powerful 3 coherence && \
# python3 tester.py llama3.1:70b powerful 3 fluency && \
# python3 tester.py llama3.1:70b powerful 3 relevance && \
python3 tester.py llama3.1:70b powerful 3 consistency 



