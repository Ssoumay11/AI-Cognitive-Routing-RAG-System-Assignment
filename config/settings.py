from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    MODEL = "openai/gpt-oss-120b"

    EMBEDDING_MODEL = "all-MiniLM-L6-v2"


