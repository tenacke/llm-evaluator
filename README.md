# 🧪 task-evaluator

A lightweight, pluggable Python package to evaluate tasks using different model providers like **Ollama** and **OpenAI** — with a unified interface.

---

## 📦 Installation

```bash
pip install evallm
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

## 🔍 Tasks

Currently, the following tasks are supported:

- **📝 Summarization**: Evaluates the quality of a summary given an original text
- **🔎 NLI**: Natural Language Inference to determine relationships between text pairs
- **⚖️ Pairwise**: Compares two outputs to determine which one better meets specified criteria

## 🧪 Evaluation

The evaluation process is based on the task you choose. The `LLMEvaluator` class provides a unified interface for evaluating tasks using different model providers.

### Summarization

The `summarization` task evaluates the quality of a summary given an original text. It uses the `evaluate` method to compare the generated summary with the original text.

```python
from evaluator import LLMEvaluator

evaluator = LLMEvaluator(connection="ollama", model="llama3.1:8b", task="summarization")
result = evaluator.evaluate(
    text="The quick brown fox jumps over the lazy dog. The dog was not happy about it.",
    summary="A fox jumps over a dog.",
    metric="all"  # or "coherence", "fluency", "relevancy", "consistency"
)
print(result)
```

The `evaluate` method takes the following parameters:

- `text`: The original text to be summarized.
- `summary`: The generated summary to be evaluated.
- `metric`: The evaluation metric to be used. The default is `all`, which means all metrics will be used. You can also specify a single metric, such as `coherence`, `fluency`, `relevancy` and `consistency`.

The method returns a dataclass object containing the evaluation results, including the score and the explanation comes from the evaluation.

- `score`: The score of the evaluation (1-5).
- `explanation`: The explanation of the evaluation.
- `metric`: The metric used for the evaluation.

Note that if you use the `all` metric, the result will be a list of dataclass objects, each containing the score and explanation for each metric.

### NLI

The `nli` task evaluates the relationship between two text pairs and the label of the relationship. It uses the `evaluate` method to compare the generated summary with the original text.

```python
from evaluator import LLMEvaluator

evaluator = LLMEvaluator(connection="ollama", model="llama3.1:8b", task="nli")
result = evaluator.evaluate(
    premise="The quick brown fox jumps over the lazy dog.",
    hypothesis="The dog was not happy about it.",
    label="entailment",  # or "contradiction", "neutral"
)
```

The `evaluate` method takes the following parameters:

- `premise`: The premise of the inference.
- `hypothesis`: The hypothesis of the inference.
- `label`: The label of the inference. It should be one of these: `entailment`, `contradiction` or `neutral`.

The method returns a dataclass object containing the evaluation results, including the pass/fail status and the explanation comes from the evaluation.

- `status`: The status of the evaluation. It is `True` if the evaluation passed, otherwise `False`.
- `explanation`: The explanation of the evaluation.

### Pairwise

The `pairwise` task evaluates a question and two outputs to determine which one better meets the needs in the question. It uses the `evaluate` method to compare the two outputs.

```python
from evaluator import LLMEvaluator

evaluator = LLMEvaluator(connection="ollama", model="llama3.1:8b", task="pairwise")

result = evaluator.evaluate(
    question="Give me a sentence about a dog.",
    output1="The quick brown fox jumps over the lazy cat.",
    output2="The dog is barking at the cat.",
)
```

The `evaluate` method takes the following parameters:

- `question`: The question to be answered.
- `output1`: The first output to be evaluated.
- `output2`: The second output to be evaluated.

The method returns a dataclass object containing the evaluation results, including the choice and the explanation comes from the evaluation.

- `choice`: The choice of the evaluation. It is `1` if the first output is better, `2` if the second output is better.
- `explanation`: The explanation of the evaluation.
