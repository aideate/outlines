import pytest
from transformers import AutoTokenizer

from outlines.fsm.fsm import RegexFSM
from outlines.models.transformers import TransformerTokenizer


@pytest.fixture
def tokenizer():
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    return TransformerTokenizer(tokenizer)


@pytest.fixture
def ensure_numba_compiled(tokenizer):
    RegexFSM("a", tokenizer)
    return True
