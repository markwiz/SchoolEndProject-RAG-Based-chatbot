from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"

QDRANT_PATH = BASE_DIR / "qdrant_data"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

EMBEDDING_MODEL = "text-embedding-3-large"
CHAT_MODEL = "gpt-4.1-mini"
COLLECTION_NAME = "tkk_knowledge_base"

PDF_FILE = RAW_DATA_DIR / "kkk.pdf"
