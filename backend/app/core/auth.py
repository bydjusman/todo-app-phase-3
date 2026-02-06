from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import os


# Secret key for JWT
SECRET_KEY = os.getenv("JWT_SECRET", "your-super-secret-jwt-key-change-in-production-immediately")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class TokenData(BaseModel):
    user_id: Optional[int] = None


class Token(BaseModel):
    access_token: str
    token_type: str


# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Security scheme for API docs
security_scheme = HTTPBearer()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against a hashed password."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Hash a plain password."""
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Create an access token with the given data."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str) -> Optional[TokenData]:
    """Verify an access token and return the token data."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id_str: str = payload.get("sub")
        if user_id_str is None:
            return None
        # Convert string user_id back to integer
        user_id = int(user_id_str) if user_id_str else None
        if user_id is None:
            return None
        token_data = TokenData(user_id=user_id)
        return token_data
    except (JWTError, ValueError):
        return None


def get_current_user_from_token(token: str, session):
    """Get the current user from the access token."""
    from ..models.user import User
    from sqlmodel import select

    token_data = verify_token(token)
    if token_data is None:
        return None

    # Get user by ID from token data
    statement = select(User).where(User.id == token_data.user_id)
    user = session.exec(statement).first()

    return user


async def get_current_user(credentials: HTTPAuthorizationCredentials = security_scheme):
    """Get the current user from the access token."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = verify_token(credentials.credentials)
    if token_data is None:
        raise credentials_exception
    return token_data