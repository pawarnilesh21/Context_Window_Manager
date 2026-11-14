from app.core.tokenizer import count_tokens, count_messages_tokens
from app.core.budget import calculate_budget


def manage_context(
    system_prompt: str,
    messages: list,
    context_window: int,
    reserved_output_tokens: int,
    strategy: str = "truncation",
    model: str = "gpt-4o-mini",
):

    # 1. Calculate available input budget
    available_budget = context_window - reserved_output_tokens

    if available_budget < 0:
        raise ValueError("Reserved tokens exceed context window")

    # 2. Count system prompt tokens
    system_tokens = count_tokens(system_prompt, model)

    # 3. Calculate message tokens
    message_tokens = count_messages_tokens(messages, model)

    total_tokens = system_tokens + message_tokens

    # 4. Detect overflow
    budget = calculate_budget(
        context_window=context_window,
        reserved_output_tokens=reserved_output_tokens,
        input_tokens=total_tokens,
    )

    optimized_messages = messages.copy()

    # 5. Apply context management strategy
    if budget.is_overflow:
        if strategy == "truncation":
            # Remove oldest messages until context fits
            while optimized_messages:
                optimized_messages.pop(0)

                message_tokens = count_messages_tokens(optimized_messages, model)

                total_tokens = system_tokens + message_tokens

                if total_tokens <= available_budget:
                    break

        elif strategy == "sliding_window":
            # Keep the latest messages that fit
            selected_messages = []

            for message in reversed(messages):
                candidate = [message] + selected_messages

                candidate_tokens = count_messages_tokens(candidate, model)

                if system_tokens + candidate_tokens <= available_budget:
                    selected_messages = candidate
                else:
                    break

            optimized_messages = selected_messages

        else:
            raise ValueError("Invalid context management strategy")

    # 6. Calculate final token consumption
    final_message_tokens = count_messages_tokens(optimized_messages, model)

    final_total_tokens = system_tokens + final_message_tokens

    final_budget = calculate_budget(
        context_window=context_window,
        reserved_output_tokens=reserved_output_tokens,
        input_tokens=final_total_tokens,
    )

    # 7. Generate optimized prompt
    optimized_prompt = {"system_prompt": system_prompt, "messages": optimized_messages}

    return {
        "original_tokens": total_tokens,
        "optimized_tokens": final_total_tokens,
        "tokens_saved": max(0, total_tokens - final_total_tokens),
        "overflow_detected": budget.is_overflow,
        "optimization_applied": budget.is_overflow,
        "strategy": strategy,
        "budget": final_budget.model_dump(),
        "optimized_prompt": optimized_prompt,
    }
