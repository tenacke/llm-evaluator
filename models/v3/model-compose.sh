#!/bin/bash

ollama pull deepseek-r1:32b

ollama create evallm-coherence:v3 -f $(dirname "$(realpath "$0")")/Modelfile-coherence
ollama create evallm-fluency:v3 -f $(dirname "$(realpath "$0")")/Modelfile-fluency
ollama create evallm-relevance:v3 -f $(dirname "$(realpath "$0")")/Modelfile-relevance
ollama create evallm-consistency:v3 -f $(dirname "$(realpath "$0")")/Modelfile-consistency