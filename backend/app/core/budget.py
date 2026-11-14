from pydantic import BaseModel, Field


class TokenBudget(BaseModel):
    context_window: int = Field(gt=0)
    reserved_output_tokens: int = Field(ge=0)
    input_tokens: int = Field(ge=0)

    total_input_budget: int = 0
    remaining_tokens: int = 0
    is_overflow: bool = False


def calculate_budget(
    context_window: int, reserved_output_tokens: int, input_tokens: int
) -> TokenBudget:

    if reserved_output_tokens > context_window:
        raise ValueError("Reserved output tokens cannot exceed context window")

    available_input_tokens = context_window - reserved_output_tokens

    remaining_tokens = available_input_tokens - input_tokens

    return TokenBudget(
        context_window=context_window,
        reserved_output_tokens=reserved_output_tokens,
        input_tokens=input_tokens,
        total_input_budget=available_input_tokens,
        remaining_tokens=max(0, remaining_tokens),
        is_overflow=input_tokens > available_input_tokens,
    )
