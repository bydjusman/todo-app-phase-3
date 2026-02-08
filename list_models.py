import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Initialize Google AI
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# List available models
models = genai.list_models()
print("Available models:")
for model in models:
    print(f"- {model.name}")
    print(f"  Supported operations: {model.supported_generation_methods}")
    print()