# 🧪 task-evaluator

A lightweight, pluggable Python package to evaluate tasks using different model providers like **Ollama** and **OpenAI** — with a unified interface.

---

## 📦 Installation

```bash
pip install llm-evaluator
```

## 🚀 Usage

### Using Ollama

This example assumes you are running a local Ollama server (e.g., at localhost:11434).

```python
from llm_evaluator import Evaluator

# Initialize the Evaluator with Ollama
evaluator = Evaluator(model="llama3.1:8b", provider="ollama",
task="summarization")

# Evaluate a task
result = evaluator.evaluate(
    text="The quick brown fox jumps over the lazy dog. The dog was not happy about it.",
    summary="A fox jumps over a dog.",
)
print(result)
```

### Using OpenAI

This example assumes you have set up your OpenAI API key in your environment variables.

```python
from llm_evaluator import Evaluator

import os

# Initialize the Evaluator with OpenAI
evaluator = Evaluator(model="gpt-3.5-turbo", provider="openai", api_key=os.getenv("OPENAI_API_KEY"), task="summarization")

# Evaluate a task
result = evaluator.evaluate(
    text="The quick brown fox jumps over the lazy dog. The dog was not happy about it.",
    summary="A fox jumps over a dog.",
)
print(result)
```
