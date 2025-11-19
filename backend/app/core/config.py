import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

settings = Settings()
