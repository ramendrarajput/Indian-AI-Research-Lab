"""
Project BRAHMA

AI Provider Registry
"""

from config.settings import AI_PROVIDER
from core.providers.gemini import get_text_model
from core.providers.gemini import get_vision_model

PROVIDERS = {
    "gemini": {
        "chat": get_text_model,
        "vision": get_vision_model,
    }
}

def get_chat_model():
    """
    Return the configured chat model.
    """

    try:
        return PROVIDERS[AI_PROVIDER]["chat"]()

    except KeyError:
        raise ValueError(
            f"Unsupported AI Provider: {AI_PROVIDER}"
        )

def get_vision_model_instance():

    try:
        return PROVIDERS[AI_PROVIDER]["vision"]()

    except KeyError:
        raise ValueError(
            f"Unsupported AI Provider: {AI_PROVIDER}"
        )