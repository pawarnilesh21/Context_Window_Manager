import tiktoken
from functools import lru_cache

DEFAULT_MODEL = "gpt-4o-mini"


@lru_cache(maxsize=10)
def get_encoding(model: str = DEFAULT_MODEL):
    """Get tokenizer encoding for the selected model."""
    try:
        return tiktoken.encoding_for_model(model)
    except KeyError:
        raise ValueError(f"Unsupported model: {model}")


def count_tokens(text: str, model: str = DEFAULT_MODEL) -> int:
    """Count tokens in a text string."""
    encoding = get_encoding(model)
    tokens = encoding.encode(text)

    return len(tokens)


def count_messages_tokens(messages: list, model: str = DEFAULT_MODEL) -> int:
    """Estimate token consumption of conversation messages."""

    encoding = get_encoding(model)

    total_tokens = 0

    for message in messages:
        total_tokens += 3  # Approximate message formatting overhead

        for key, value in message.items():
            if isinstance(value, str):
                total_tokens += len(encoding.encode(value))

    total_tokens += 3  # Approximate assistant reply priming

    return total_tokens
