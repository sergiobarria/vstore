from typing import List
from uuid import UUID

from app.api.deps import get_session
from app.models import Book, BookCreate, BookRead, BookUpdate
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

router = APIRouter()

# TODO: SQLModel does not have a wrapper yet for AsyncSession
# TODO: Update import once it's available


@router.get("/", response_model=List[BookRead])
async def get_books(
    *, skip: int = 0, limit: int = 100, session: AsyncSession = Depends(get_session)
):
    """Get all books from database"""
    q = select(Book).offset(skip).limit(limit)
    result = await session.execute(q)
    books = result.scalars().all()
    return books


@router.post("/", response_model=BookRead, status_code=status.HTTP_201_CREATED)
async def add_book(*, session: AsyncSession = Depends(get_session), book: BookCreate):
    """Add new book to database"""
    db_book = Book.from_orm(book)
    session.add(db_book)
    await session.commit()
    await session.refresh(db_book)
    return db_book


@router.get("/{book_id}", response_model=BookRead)
async def get_book_by_id(
    *, book_id: UUID, session: AsyncSession = Depends(get_session)
):
    """Get single book by ID"""
    book = await session.get(Book, book_id)

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID of {book_id} not found",
        )

    return book


@router.patch("/{book_id}", response_model=BookRead)
async def update_book(
    *, book_id: UUID, book: BookUpdate, session: AsyncSession = Depends(get_session)
):
    """Update book by ID"""
    db_book = await session.get(Book, book_id)

    if not db_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID of {book_id} not found",
        )

    book_data = book.dict(exclude_unset=True)

    for key, value in book_data.items():
        setattr(db_book, key, value)

    session.add(db_book)
    await session.commit()
    await session.refresh(db_book)
    return db_book


@router.delete("/{book_id}")
async def delete_book(*, book_id: UUID, session: AsyncSession = Depends(get_session)):
    """Delete book by ID"""
    book = await session.get(Book, book_id)

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID of {book_id} not found",
        )

    await session.delete(book)
    await session.commit()
    return {"status": "ok"}
