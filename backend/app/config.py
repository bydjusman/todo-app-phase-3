import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Initialize Google AI
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Model configuration
MODEL_NAME = "gemini-2.5-flash"
chat_model = genai.GenerativeModel(MODEL_NAME)

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")