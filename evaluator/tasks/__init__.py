from .base import BaseTask
from .summarization import Summarization, SummarizationOutput
from .nli import NLI, NLIOutput
from .pairwise import Pairwise, PairwiseOutput
from .translation import Translation, TranslationOutput
from .prompts import (
    SUMMARIZATION_TEMPLATE,
    NLI_TEMPLATE,
    PAIRWISE_TEMPLATE,
    TRANSLATION_TEMPLATE,
    GENERIC_TEMPLATE,
)

__all__ = [
    "BaseTask",
    "Summarization",
    "NLI",
    "Pairwise",
    "Translation",
    "SummarizationOutput",
    "NLIOutput",
    "PairwiseOutput",
    "TranslationOutput",
    "SUMMARIZATION_TEMPLATE",
    "NLI_TEMPLATE",
    "PAIRWISE_TEMPLATE",
    "TRANSLATION_TEMPLATE",
    "GENERIC_TEMPLATE",
]
