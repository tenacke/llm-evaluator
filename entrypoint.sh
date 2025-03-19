#!/bin/bash
source /opt/evallm/venv/bin/activate
ollama serve > /dev/null 2>&1 < /dev/null &
exec "$@"