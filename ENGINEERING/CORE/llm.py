from core.providers.gemini import get_model

PROVIDER = "gemini"

def get_llm():

    if PROVIDER == "gemini":
        return get_model()

    raise ValueError(f"Unknown provider: {PROVIDER}")