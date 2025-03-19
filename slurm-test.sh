#!/bin/bash
#SBATCH --job-name=slurm-test
#SBATCH --container-image ghcr.io/tenacke/evallm:latest
#SBATCH --gpus=1
#SBATCH --cpus-per-gpu=8
#SBATCH --mem-per-gpu=40G

source /opt/evallm/venv/bin/activate
bash models/v2/model-compose.sh
python3 models/v2/model_test.py