import os
from dotenv import load_dotenv

load_dotenv()

# ========= API Keys =========
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY not found in .env"
    )
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
HUGGING_FACE_API_KEY = os.getenv("HUGGING_FACE_API_KEY")

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

# ========= LLM =========
from ENGINEERING.CORE.CONFIG.models import GEMINI_TEXT_MODEL

DEFAULT_MODEL = GEMINI_TEXT_MODEL

TEMPERATURE = 0.3

# ========= RAG =========
CHUNK_SIZE = 1200
CHUNK_OVERLAP = 200

VECTOR_DB = "faiss_index"

# ========= Streamlit =========
PAGE_TITLE = "Indian AI Research Lab"

PAGE_ICON = "🤖"

APP_NAME = "Project BRAHMA"

DEVELOPER_NAME = "Ramendra Singh Rajput"

VOICE_ENABLED = True

DEBUG = True

# ========= AI Provider =========

AI_PROVIDER = "gemini"