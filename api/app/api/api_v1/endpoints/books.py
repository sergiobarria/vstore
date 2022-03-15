from typing import List
from uuid import UUID

from app import models
from app.database.session import get_session
from app.schemas.book import BookCreate, BookRead, BookSchema, BookUpdate
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session, joinedload

# from sqlmodel import select

router = APIRouter()


@router.get("/", response_model=List[BookRead])
async def get_books(
    *, skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    """Get all books from database"""
    books = (
        session.query(models.Book)
        .options(joinedload(models.Book.authors))
        .offset(skip)
        .limit(limit)
        .all()
    )
    return books


@router.post("/", response_model=BookRead, status_code=status.HTTP_201_CREATED)
async def add_book(*, session: Session = Depends(get_session), book: BookCreate):
    """Add new book to database"""
    db_book = models.Book(**book.dict())
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book


@router.get("/{book_id}", response_model=BookRead)
async def get_book_by_id(*, book_id: UUID, session: Session = Depends(get_session)):
    """Get single book by ID"""
    book = session.query(models.Book).filter_by(id=book_id).first()

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID of {book_id} not found",
        )

    return book


@router.put("/{book_id}", response_model=BookRead)
async def update_book(
    *, book_id: UUID, book: BookUpdate, session: Session = Depends(get_session)
):
    """Update book by ID"""
    db_book = session.query(models.Book).filter_by(id=book_id).first()

    if not db_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID of {book_id} not found",
        )

    book_data = book.dict(exclude_unset=True)

    for key, value in book_data.items():
        setattr(db_book, key, value)

    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book


@router.delete("/{book_id}")
async def delete_book(*, book_id: UUID, session: Session = Depends(get_session)):
    """Delete book by ID"""
    book = session.query(models.Book).filter_by(id=book_id).first()

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID of {book_id} not found",
        )

    session.delete(book)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
