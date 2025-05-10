# 🧪 task-evaluator

A lightweight, pluggable Python package to evaluate tasks using different model providers like **Ollama** and **OpenAI** — with a unified interface.

---

## 📦 Installation

```bash
pip install llm-evaluator
```

## 🚀 Usage

### Using Ollama

Before using the `LLMEvaluator` with Ollama, ensure you have an Ollama server running. If you don't have any, you can start one in your local environment using Ollama CLI. If you don't have it installed, you can download it from [here](https://ollama.com/download).

After that you can start a server with the following command:

```bash
ollama serve
```

This example assumes you are running a local Ollama server (e.g., at localhost:11434).

```python
from evaluator import LLMEvaluator

# Initialize the Evaluator with Ollama
evaluator = LLMEvaluator(connection="ollama", model="llama3.1:8b", task="summarization")

# Evaluate a task
result = evaluator.evaluate(
    text="The quick brown fox jumps over the lazy dog. The dog was not happy about it.",
    summary="A fox jumps over a dog.",
)
print(result)
```

Ollama uses port `11434` by default. If you want to change the port, you can specify the full URI when initializing the `LLMEvaluator`. For example, if you want to use port `12345`, you can do it like this:

```python
from evaluator import LLMEvaluator
evaluator = LLMEvaluator(connection="ollama", model="llama3.1:8b", url="http://localhost:12345", task="summarization")
```

### Using OpenAI

Since we do not deploy any LLM models globally, you can only use OpenAI models with your OpenAI API key. You can find the installation instructions [here](https://platform.openai.com/docs/quickstart).
You can set your OpenAI API key in your environment variables. For example, in a Unix-like terminal, you can do it like this:

```bash
export OPENAI_API_KEY="your_openai_api_key"
```

Or in a Windows terminal, you can do it like this:

```bash
set OPENAI_API_KEY="your_openai_api_key"
```

You can also set the OpenAI API key in your code directly, but it's not recommended for security reasons.

This example assumes you have set up your OpenAI API key in your environment variables.

```python
from evaluator import LLMEvaluator

import os

# Initialize the Evaluator with OpenAI
evaluator = Evaluator(connection="openai", model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"), task="summarization")

# Evaluate a task
result = evaluator.evaluate(
    text="The quick brown fox jumps over the lazy dog. The dog was not happy about it.",
    summary="A fox jumps over a dog.",
)
print(result)
```
