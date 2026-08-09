import os

from providers import gemini, openrouter


def get_provider():
    provider_name = os.getenv("LLM_PROVIDER").lower()

    if provider_name == "gemini":
        return gemini

    if provider_name == "openrouter":
        return openrouter

    raise ValueError(
        f"Unknown LLM provider: {provider_name}. "
    )