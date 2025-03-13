# Ensures type validation for routes' inputs and responses
from pydantic import BaseModel
from typing import Optional

# User Schema (for Signup & Response)
class UserCreate(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    email: str
    password: str

# Task Schema (for CRUD Operations)
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TaskResponse(TaskCreate):
    id: int
    user_id: int

    class Config:
        from_attributes = True
