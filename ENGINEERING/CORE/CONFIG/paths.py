from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT_DIR / "data"

LOG_DIR = ROOT_DIR / "logs"

FAISS_DIR = ROOT_DIR / "faiss_index"

PROMPT_DIR = ROOT_DIR / "prompts"