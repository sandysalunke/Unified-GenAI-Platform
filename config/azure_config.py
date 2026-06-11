import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()
DATA_PATH = "data/"
AZURE_API_KEY = os.getenv("AZURE_API_KEY")
API_ENDPOINT = os.getenv("API_ENDPOINT")
API_VERSION = os.getenv("API_VERSION")
CHAT_MODEL = os.getenv("CHAT_MODEL")
IMAGE_MODEL = os.getenv("IMAGE_MODEL")
WHISPER_MODEL = os.getenv("WHISPER_MODEL")
EMBED_MODEL = os.getenv("EMBED_MODEL")

client = AzureOpenAI(
    api_key=AZURE_API_KEY,
    api_version=API_VERSION,
    azure_endpoint=API_ENDPOINT
)