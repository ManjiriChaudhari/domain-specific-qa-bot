from pathlib import Path

# -------------------------------------------------
# Project Paths
# -------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT_DIR / "data"
MODELS_DIR = ROOT_DIR / "models"
ASSETS_DIR = ROOT_DIR / "assets"

UPLOADS_DIR = DATA_DIR / "uploads"

KNOWLEDGE_FILE = DATA_DIR / "trading_knowledge.txt"

FAISS_INDEX = MODELS_DIR / "trading_index.faiss"

# -------------------------------------------------
# Embedding Model
# -------------------------------------------------

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# -------------------------------------------------
# Language Model
# -------------------------------------------------

LLM_MODEL = "google/flan-t5-base"

# -------------------------------------------------
# Retrieval Settings
# -------------------------------------------------

TOP_K = 3

# -------------------------------------------------
# Chunk Settings
# -------------------------------------------------

CHUNK_SIZE = 500

CHUNK_OVERLAP = 50

# -------------------------------------------------
# Streamlit Settings
# -------------------------------------------------

APP_NAME = "Trading AI Assistant"

APP_ICON = "📈"
