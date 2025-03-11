# EvalLM

Authors: [Emre Kılıç](https://github.com/tenacke), [Kristina Trajkovski](https://github.com/kristinatrajkovski), [Bilge Kaan Güneyli](https://github.com/kaanguneyli)

The LLM Evaluator. An evaluator model which analyses and scores of a LMM in terms of their performance in summarization task.

## Dataset

#### SummEval

We use [SummEval](https://github.com/Yale-LILY/SummEval) project in our tests. It uses the CNN and Daily Mail stories as data source. The summaries of the stories are created by different LLMs and annotated by human evaluators.
To recreate the dataset follow the instructions:

1. Download CNN Stories and Daily Mail Stories from [here](https://cs.nyu.edu/~kcho/DMQA/).
2. Create a cnndm directory and unpack downloaded files into the directory.
3. Download the model outputs and human annotations from [here](https://storage.googleapis.com/sfr-summarization-repo-research/model_annotations.aligned.jsonl) and add the json file into the cnndm directory.
4. Put the cnndm directory into the datasets directory.

## Installation

#### Ollama

It is necessary to install Ollama to recreate the EvalLM models. You can install Ollama from [here](https://ollama.com/download).

We will also use the Ollama's `python` package to run the tests. You can install it by running:

```bash
pip install ollama
```

#### Models

We store the descriptions of the models in the `models` directory. To recreate the models, you can run the following command:

```bash
bash models/<version>/model-compose.sh
```

#### Running the tests

After recreating the dataset and composing a model, you can run the test of the model in order to make sure everything goes well.
To run the test of a model, you can use the following command:

```bash
python3 models/<version>/model_test.py
```

## Usage

TBW
