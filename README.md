# EvalLM

Authors: [Emre Kılıç](https://github.com/tenacke), [Kristina Trajkovski](https://github.com/kristinatrajkovski), [Bilge Kaan Güneyli](https://github.com/kaanguneyli)

The LLM Evaluator. An evaluator model which analyses and scores an LMM in terms of their performance in the summarization task.

## Dataset

#### SummEval

We use [SummEval](https://github.com/Yale-LILY/SummEval) project in our tests. It uses the CNN and Daily Mail stories as data sources. The summaries of the stories are created by different LLMs and annotated by human evaluators.
To recreate the dataset, follow the instructions:

1. Download CNN Stories and Daily Mail Stories from [here](https://cs.nyu.edu/~kcho/DMQA/).
2. Create a cnndm directory and unpack downloaded files into the directory.
3. Download the model outputs and human annotations from [here](https://storage.googleapis.com/sfr-summarization-repo-research/model_annotations.aligned.jsonl) and add the json file into the cnndm directory.
4. Put the cnndm directory into the datasets directory.

## Installation

#### Ollama

We use Ollama to form our evaluation models. To recreate the EvalLM models, you must install Ollama. You'll be able to do so from [here](https://ollama.com/download).

We also use the Ollama's `python` package to run the tests. You can install it by running:

```bash
pip install ollama
```

#### Models

We store the descriptions of the models in the `models` directory. To recreate the models, you can run the following command:

```bash
bash models/<version>/model-compose.sh
```

#### Running the tests

After recreating the dataset and composing a model, you can run the model's test to ensure everything goes well.
To run the test of a model, you can use the following command:

```bash
python3 models/<version>/model_test.py
```

## Usage

TBW
