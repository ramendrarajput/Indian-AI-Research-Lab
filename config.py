import os
from dotenv import load_dotenv

load_dotenv()

# ========= API Keys =========
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# ========= LLM =========
DEFAULT_MODEL = "gemini-2.5-flash"

TEMPERATURE = 0.3

# ========= RAG =========
CHUNK_SIZE = 1200
CHUNK_OVERLAP = 200

VECTOR_DB = "faiss_index"

# ========= Streamlit =========
PAGE_TITLE = "Indian AI Research Lab"

PAGE_ICON = "🤖"