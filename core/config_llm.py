import os
from llama_index.core import Settings
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.llms.groq import Groq
from dotenv import load_dotenv

load_dotenv()

GENAI_API_KEY = os.getenv('GENAI_API_KEY')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

llm = Groq(model="openai/gpt-oss-120b", api_key=GROQ_API_KEY, context_window=131072, max_tokens=1024, temperature = 0.3)
 
Settings.llm = llm



