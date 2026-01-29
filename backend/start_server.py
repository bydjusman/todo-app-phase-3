import os
import uvicorn
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get host and port from environment variables, with defaults
host = os.getenv("HOST", "0.0.0.0")
port = int(os.getenv("PORT", "8000"))
reload = os.getenv("RELOAD", "0").strip().lower() in {"1", "true", "yes", "y"}

if __name__ == "__main__":
    print(f"Starting server on {host}:{port}")
    print(f"Using database: {os.getenv('DATABASE_URL', 'sqlite:///./test.db')}")

    uvicorn.run(
        "app.main:app",
        host=host,
        port=port,
        reload=reload
    )