import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Google AI with the new google-genai package
import google.genai as genai

# Initialize the API with your key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Model configuration
MODEL_NAME = "gemini-2.5-flash"
chat_model = genai.GenerativeModel(MODEL_NAME)

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")