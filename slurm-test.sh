#!/bin/bash
#SBATCH --job-name=slurm-test
#SBATCH --container-image /users/emre.kilic/ollama.sqsh
#SBATCH --container-mounts /users/emre.kilic/llm-evaluator:/evallm
#SBATCH --container-workdir /evallm
#SBATCH --container-save=/users/emre.kilic/ollama_installed.sqsh
#SBATCH --gpus=1
#SBATCH --cpus-per-gpu=8
#SBATCH --mem-per-gpu=40G

apt-get update 
&& apt-get -y install --no-install-recommends \
    git \
    wget \
    cmake \
    ninja-build \
    build-essential \
    python3.12 \
    python3-dev \
    python3-pip \
    python3-venv \
    python-is-python3 \
&& apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* 

python3 -m pip install --upgrade pip && \
python3 -m venv venv

source venv/bin/activate
pip install -r requirements.txt
bash models/v2/model-compose.sh
python3 models/v2/model_test.py

