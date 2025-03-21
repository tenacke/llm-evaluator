#!/bin/bash

ollama pull llama3.1:8b

ollama create evallm-coherence:v2.1 -f $(dirname "$(realpath "$0")")/ModelfileCoherence

ollama create evallm-fluency:v2.1 -f $(dirname "$(realpath "$0")")/ModelfileFluency

ollama create evallm-relevance:v2.1 -f $(dirname "$(realpath "$0")")/ModelfileRelevance

ollama create evallm-consistency:v2.1 -f $(dirname "$(realpath "$0")")/ModelfileConsistency