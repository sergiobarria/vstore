from typing import List
from uuid import UUID

from app import schemas
from app.dependencies import get_db
from app.helpers import book
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.BookInDatabase])
async def get_all_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all books from the Database"""
    requested_books = await book.get(db, skip=skip, limit=limit)

    return requested_books


@router.get("/{id}", response_model=schemas.BookInDatabase)
async def get_book_by_id(id: UUID, db: Session = Depends(get_db)):
    """Get single book by ID"""
    requested_book = await book.get_by_id(db, id)

    if not requested_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID of {id} does not exists",
        )

    return requested_book


@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_book(request: schemas.Book, db: Session = Depends(get_db)):
    """Add new book to the database"""
    created_book = await book.add(db, request)

    if not created_book:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="There was an error creating new item",
        )

    return created_book


@router.delete("/{id}")
async def delete_book(id: UUID, db: Session = Depends(get_db)):
    """Delete book from database"""
    await book.delete_one(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}")
async def update_book(id: UUID, request: schemas.Book, db: Session = Depends(get_db)):
    """Update book from database"""
    return await book.update_one(db, id, request)
