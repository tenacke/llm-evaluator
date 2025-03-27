#!/bin/bash
#SBATCH --job-name=average-test
#SBATCH --container-image ghcr.io\#tenacke/llm-evaluator:latest-container
#SBATCH --container-mounts=/users/emre.kilic/llm-evaluator/outputs:/opt/llm-evaluator/outputs,/users/emre.kilic/llm-evaluator/logs:/opt/llm-evaluator/logs
#SBATCH --time=08:00:00
#SBATCH --cpus-per-task=8
#SBATCH --mem=4G

source /opt/llm-evaluator/venv/bin/activate

python3 models/v3/model_test.py && \
python3 tester.py deepseek-r1:32b average 3 coherence && \
python3 tester.py deepseek-r1:32b average 3 fluency && \
python3 tester.py deepseek-r1:32b average 3 relevance && \
python3 tester.py deepseek-r1:32b average 3 consistency 



