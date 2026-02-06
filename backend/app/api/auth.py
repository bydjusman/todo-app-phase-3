from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlmodel import Session
from datetime import timedelta
from typing import Dict
from ..database.session import get_session
from ..models.user import User
from ..schemas.user import UserCreate, UserResponse
from ..core.auth import create_access_token, get_password_hash, get_current_user_from_token
from ..core.user_service import UserService

router = APIRouter(prefix="/auth", tags=["auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


@router.post("/register", response_model=UserResponse)
async def register_user(user_create: UserCreate, session: Session = Depends(get_session)):
    """Register a new user."""
    try:
        # Create user using UserService
        user = UserService.create_user(session, user_create)

        # Return the created user in the expected format
        return UserResponse(
            id=user.id,
            email=user.email,
            name=user.name if user.name else user.username,
            created_at=user.created_at,
            updated_at=user.updated_at
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while registering user: {str(e)}"
        )


@router.post("/signup", response_model=UserResponse)
async def signup_user(user_create: UserCreate, session: Session = Depends(get_session)):
    """Sign up a new user."""
    try:
        # Create user using UserService
        user = UserService.create_user(session, user_create)

        # Return the created user in the expected format
        return UserResponse(
            id=user.id,
            email=user.email,
            name=user.name if user.name else user.username,
            created_at=user.created_at,
            updated_at=user.updated_at
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while signing up user: {str(e)}"
        )


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    """Authenticate user and return access token."""
    user = UserService.authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=30)  # 30 minutes default
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    }


@router.post("/logout")
async def logout():
    """Logout user (client-side cleanup required)."""
    return {"message": "Successfully logged out"}


@router.get("/me", response_model=UserResponse)
async def get_current_user_endpoint(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)):
    """Get current user info."""

    from ..core.auth import verify_token
    token_data = verify_token(token)
    if token_data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Get user by ID from token data
    user = UserService.get_user_by_id(session, token_data.user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return UserResponse(
        id=user.id,
        email=user.email,
        name=user.name if user.name else user.username,  # Use name if available, otherwise use username
        created_at=user.created_at,
        updated_at=user.updated_at
    )