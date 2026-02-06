from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import logging
import traceback

# Load environment variables from .env file
load_dotenv()

from .api.health import router as health_router
from .api.todos import router as todos_router
from .api.auth import router as auth_router
from .api.mcp_tools import router as mcp_tools_router
from .api.chat import router as chat_router
from .database.session import create_db_and_tables

# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI-Powered Todo Chatbot with MCP",
    description="API for managing todos through natural language commands using MCP tools",
    version="1.0.0"
)

# Configure CORS for Next.js frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include API routers under /api prefix
app.include_router(health_router, prefix="/api")
app.include_router(todos_router, prefix="/api")
app.include_router(auth_router, prefix="/api")
app.include_router(mcp_tools_router, prefix="/api")
app.include_router(chat_router, prefix="/api")


# Create database tables on startup
@app.on_event("startup")
def on_startup():
    logger.info("Creating database tables...")
    create_db_and_tables()
    logger.info("Database tables created successfully")


# Global exception handler for better error reporting
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"Unhandled exception: {exc}\nTraceback: {traceback.format_exc()}")
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": "An unexpected error occurred",
            "detail": str(exc) if app.debug else "Internal server error"
        }
    )


@app.get("/")
async def root():
    return {
        "message": "AI-Powered Todo Chatbot with MCP API",
        "version": "1.0.0",
        "endpoints": [
            "/api/health",
            "/api/chat",
            "/api/auth",
            "/api/todos"
        ]
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)