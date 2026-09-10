from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    # We use Google's unique ID as the primary key since they handle login
    id = Column(String, primary_key=True, index=True) 
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    picture = Column(String, nullable=True)
    
    # Automatically records when the user first logged in
    created_at = Column(DateTime(timezone=True), server_default=func.now())
