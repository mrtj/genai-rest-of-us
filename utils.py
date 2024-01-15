import os, getpass
from dotenv import load_dotenv

load_dotenv()

def ensure_openai_api_key():
    if "OPENAI_API_KEY" not in os.environ:
        os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key:")