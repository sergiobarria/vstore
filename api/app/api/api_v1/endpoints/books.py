from typing import List
from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Response, status

from app import schemas
from app.dependencies import get_db
from app.helpers import book

router = APIRouter()


@router.get("/", response_model=List[schemas.BookInDatabase])
async def get_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all books from the Database
    """
    return await book.get_all(db, skip=skip, limit=limit)


@router.get("/{id}")
async def get_book_by_id(id: UUID, db: Session = Depends(get_db)):
    """Get single book by ID
    """
    return await book.get_by_id(db, id)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_book(request: schemas.BookSchema, db: Session = Depends(get_db)):
    """Add new book to the database
    """
    return await book.add(db, request)


@router.delete("/{id}")
async def delete_book(id: UUID, db: Session = Depends(get_db)):
    """Delete book from database
    """
    await book.delete_one(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}")
async def update_book(id: UUID, request: schemas.BookSchema, db: Session = Depends(get_db)):
    """Update book from database
    """
    return await book.update_one(db, id, request)
