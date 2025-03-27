#!/bin/bash
#SBATCH --job-name=powerful-test
#SBATCH --container-image ghcr.io\#tenacke/llm-evaluator
#SBATCH --container-mounts=/users/bilge.guneyli/llm-evaluator/csv:/opt/llm-evaluator/csv,/users/bilge.guneyli/llm-evaluator/logs:/opt/llm-evaluator/logs
#SBATCH --time=08:00:00
#SBATCH --gpus=1
#SBATCH --cpus-per-gpu=8
#SBATCH --mem-per-gpu=40G

source /opt/llm-evaluator/venv/bin/activate
mkdir -p /opt/llm-evaluator/logs
git fetch --all && \
git checkout kaan-container && \
git pull origin kaan-container
ollama serve > /dev/null 2>&1 < /dev/null &
echo "Waiting for the server to start..."
sleep 5
echo "Server is up! Proceeding with the next command."
# bash models/v3/model-compose.sh
ollama pull llama3.1:70b && \
python3 models/v3/model_test.py && \
python3 tester.py llama3.1:70b powerful 3 coherence && \
python3 tester.py llama3.1:70b powerful 3 fluency && \
python3 tester.py llama3.1:70b powerful 3 relevance && \
python3 tester.py llama3.1:70b powerful 3 consistency 



