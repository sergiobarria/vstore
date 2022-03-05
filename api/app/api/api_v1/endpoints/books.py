from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status

from app import deps, schemas
from app.helpers import book

router = APIRouter()


@router.get("/", response_model=List[schemas.BookInDatabase])
def get_all(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    """Get all books from the Database
    """
    return book.get_all_books(db, skip=skip, limit=limit)


@router.get("/{id}")
def get_book_by_id(id: int, db: Session = Depends(deps.get_db)):
    """Get single book by ID
    """
    return book.get_by_id(db, id)


@router.post("/", status_code=status.HTTP_201_CREATED)
def add_book(request: schemas.Book, db: Session = Depends(deps.get_db)):
    return book.add(db, request)
