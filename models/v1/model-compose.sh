#!/bin/bash

ollama pull llama3.1:8b

ollama create evallm:v1 -f $(dirname "$(realpath "$0")")/Modelfile
