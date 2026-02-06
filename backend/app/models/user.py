from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional
import enum


class UserRole(str, enum.Enum):
    USER = "user"
    ADMIN = "admin"


class UserBase(SQLModel):
    username: str = Field(unique=True, nullable=False, max_length=50)
    email: str = Field(unique=True, nullable=False, max_length=100)
    name: Optional[str] = Field(default=None, max_length=100)


class User(UserBase, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str = Field(nullable=False)
    role: UserRole = Field(default=UserRole.USER)
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship to todos - using string reference to avoid circular import
    todos: list["Todo"] = Relationship(back_populates="user", sa_relationship_kwargs={"lazy": "select"})