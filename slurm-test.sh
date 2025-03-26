#!/bin/bash
#SBATCH --job-name=slurm-test
#SBATCH --container-image ghcr.io\#tenacke/llm-evaluator
#SBATCH --container-mounts=/users/emre.kilic/llm-evaluator/csv:/opt/llm-evaluator/csv
#SBATCH --time=08:00:00
#SBATCH --gpus=2
#SBATCH --cpus-per-gpu=8
#SBATCH --mem-per-gpu=40G

source /opt/llm-evaluator/venv/bin/activate
git fetch --all && \
git checkout container && \
git pull origin container
ollama serve > /dev/null 2>&1 < /dev/null &
echo "Waiting for the server to start..."
sleep 5
echo "Server is up! Proceeding with the next command."
bash models/v3/model-compose.sh
python3 models/v3/model_test.py && \
python3 tester.py evallm-coherence:v3 poor 3 && \
python3 tester.py evallm-fluency:v3 poor 3 && \
python3 tester.py evallm-relevance:v3 poor 3 && \
python3 tester.py evallm-consistency:v3 poor 3 && \


