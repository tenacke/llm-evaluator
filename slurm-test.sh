#!/bin/bash
#SBATCH --job-name=slurm-test
#SBATCH --container-image ghcr.io\#tenacke/llm-evaluator
#SBATCH --container-mounts=/users/emre.kilic/csv:/opt/llm-evaluator/csv
#SBATCH --container-save=/users/emre.kilic/llm-evaluator.sqsh
#SBATCH --time=02:00:00
#SBATCH --gpus=1
#SBATCH --cpus-per-gpu=8
#SBATCH --mem-per-gpu=40G

source /opt/llm-evaluator/venv/bin/activate
ollama serve > /dev/null 2>&1 < /dev/null &
bash models/v3/model-compose.sh
python3 models/v3/model_test.py
python3 tester-separate.py v2.1 poor 3

