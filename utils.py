import os
from dotenv import load_dotenv

load_dotenv()

def get_openai_api_key():
    return os.getenv("OPENAI_API_KEY")

def get_serper_api_key():
    return os.getenv("SERPER_API_KEY")
