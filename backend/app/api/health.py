from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/health")
async def health_check():
    """
    Health check endpoint to verify API is running
    """
    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy",
            "message": "API is running successfully",
            "service": "todo-chatbot-api"
        }
    )

@router.get("/ready")
async def readiness_check():
    """
    Readiness check endpoint
    """
    # Add any additional checks here if needed
    return JSONResponse(
        status_code=200,
        content={
            "status": "ready",
            "message": "Service is ready to accept requests"
        }
    )