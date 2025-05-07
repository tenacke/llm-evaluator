from .base import BaseTask
from .summarization import Summarization, SummarizationOutput
from .nli import NLI, NLIOutput
from .pairwise import Pairwise, PairwiseOutput
from .prompts import (
    COHERENCE_PROMPT,
    RELEVANCE_PROMPT,
    FLUENCY_PROMPT,
    CONSISTENCY_PROMPT,
    PAIRWISE_PROMPT,
    NLI_PROMPT,
)

__all__ = [
    "BaseTask",
    "Summarization",
    "NLI",
    "Pairwise",
    "SummarizationOutput",
    "NLIOutput",
    "PairwiseOutput",
    "COHERENCE_PROMPT",
    "RELEVANCE_PROMPT",
    "FLUENCY_PROMPT",
    "CONSISTENCY_PROMPT",
    "PAIRWISE_PROMPT",
    "NLI_PROMPT",
]
