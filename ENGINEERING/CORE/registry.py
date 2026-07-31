"""
Project BRAHMA

AI Provider Registry
"""

from ENGINEERING.CORE.CONFIG.settings import AI_PROVIDER
from ENGINEERING.CORE.providers.gemini import get_model #get_text_model
from ENGINEERING.CORE.providers.gemini import get_vision_model

PROVIDERS = {
    "gemini": {
        "chat": get_model,
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