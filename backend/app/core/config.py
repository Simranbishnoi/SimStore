import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load the variables from our backend/.env file
load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "The Reading Room API"
    
    # Database Configuration
    DATABASE_URL: str = os.environ.get("DATABASE_URL", "postgresql://bookstore:password123@localhost:5432/bookstore")
    
    # Authentication Settings
    JWT_SECRET: str = os.environ.get("JWT_SECRET", "supersecretkey")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 # 7 days
    
    # Google OAuth (We'll use these in Phase 11)
    GOOGLE_CLIENT_ID: str = os.environ.get("GOOGLE_CLIENT_ID", "")
    GOOGLE_CLIENT_SECRET: str = os.environ.get("GOOGLE_CLIENT_SECRET", "")

settings = Settings()
