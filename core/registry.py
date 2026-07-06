"""
Project BRAHMA

AI Provider Registry
"""

from config.settings import AI_PROVIDER
from core.providers.gemini import get_text_model


PROVIDERS = {
    "gemini": get_text_model,
}


def get_chat_model():
    """
    Return the configured chat model.
    """

    try:
        return PROVIDERS[AI_PROVIDER]()

    except KeyError:
        raise ValueError(
            f"Unsupported AI Provider: {AI_PROVIDER}"
        )