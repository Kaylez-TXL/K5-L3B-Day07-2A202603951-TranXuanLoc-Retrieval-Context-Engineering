"""Estimated standard-global Haiku 5.5 API cost; not an invoice."""
SOURCE = 'https://platform.claude.com/docs/en/about-claude/pricing'
AS_OF = '2026-11-16'


def estimate_cost(model_calls):
    total = 0.0
    for call in model_calls:
        if call.get('model') != 'claude-haiku-5-5':
            return None
        u = call.get('usage', {})
        input_tokens = u.get('input_tokens', 0)
        read = u.get('cache_read_input_tokens', 0)
        write = u.get('cache_creation_input_tokens', 0)
        long = input_tokens + read + write > 100_000
        factor = 5 if long else 1
        creation = u.get('cache_creation', {}) or {}
        hour = creation.get('ephemeral_1h_input_tokens', 0)
        five_min = write - hour
        total += factor * (input_tokens * .10 + u.get('output_tokens', 0) * .50 +
                           read * .01 + five_min * .125 + hour * .20) / 1_000_000
    return total
