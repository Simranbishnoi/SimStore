from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# 1. Create the engine (the core connection to the database)
engine = create_engine(settings.DATABASE_URL)

# 2. Create a session factory (to spawn individual conversations with the database)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. Create a Base class (our future models will inherit from this)
Base = declarative_base()

# 4. Create a dependency function to use in our API routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
