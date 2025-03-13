# FastAPI entry point:
# 1. Initialize empty tables in the database bases on Base's metadata.
# 2. Create FastAPI app and register all routers.
from fastapi import FastAPI
from routers import auth, tasks
from database import engine, Base

# Initialize database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

# Register routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def home():
    return {"message": "Welcome to the Task Manager API"}
