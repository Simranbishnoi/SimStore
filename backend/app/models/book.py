from sqlalchemy import Column, String, Integer
from app.core.database import Base

class Book(Base):
    __tablename__ = "books"

    # We will use string IDs like "BOOK-001"
    id = Column(String, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    author = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)
    
    # We store prices in whole numbers (cents/paise) to avoid math errors with decimals
    price = Column(Integer, nullable=False) 
    stock = Column(Integer, default=0)
    category = Column(String, index=True, nullable=False)
    cover_url = Column(String, nullable=True)
