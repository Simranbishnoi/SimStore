from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.book import Book
from app.schemas.common import BookResponse

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=list[BookResponse])
def get_books(category: str | None = None, db: Session = Depends(get_db)):#query parameter
    query = db.query(Book)

    if category:
        query = query.filter(Book.category == category)#sql query 

    return query.all()
@router.get("/{book_id}", response_model=BookResponse) #{new path parameter}
def get_book(book_id: str, db: Session = Depends(get_db)): #receives book_id from 
    book = db.query(Book).filter(Book.id == book_id).first()#SELECT * FROM books WHERE id = 'BOOK-007' LIMIT 1;
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")#fastAPI return {"detail": "Book not found"}

    return book 
    