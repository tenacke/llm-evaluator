from connection.base import BaseConnection
from connection.ollama import OllamaConnection
from connection.openai import OpenAIConnection

from tasks.base import BaseEvaluator
from tasks.summarization import SummarizationEvaluator
from tasks.nli import NLIEvaluator
from tasks.pairwise import PairwiseEvaluator

from pydantic import BaseModel, Field

CONNECTION_MAP = {
    "ollama": OllamaConnection,
    "openai": OpenAIConnection,
}

TASK_MAP = {
    "summarization": SummarizationEvaluator,
    "nli": NLIEvaluator,
    "pairwise": PairwiseEvaluator,
}
