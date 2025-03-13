# Database Connection:
# 1. Establish connection to the PostgreSQL database.
# 2. Create Base class of all database models
# 3. Prepare database session dependency.

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/taskdb"

# The engine manages connection to the database
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class which is a foundation for all database models.
Base = declarative_base()

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
