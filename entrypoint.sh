#!/bin/bash
source /opt/llm-evaluator/venv/bin/activate
# ollama serve > /dev/null 2>&1 < /dev/null &
exec "$@"