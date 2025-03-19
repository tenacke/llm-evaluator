#!/bin/bash

ollama pull llama3.1:70b

ollama create evallm:v3 -f $(dirname "$(realpath "$0")")/Modelfile