from typing import List
from uuid import UUID

from app import models, schemas
from fastapi import HTTPException, status
from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncResult
from sqlalchemy.orm import Session


async def get(db: Session, skip: int = 0, limit: int = 100) -> List[models.Book]:
    """Get all books from the database

    Args:
        db (Session): database to interact with
        skip (int, optional): the ammount of items to skip (useful for pagination).
        limit (int, optional): the max limit of items to retrieve for each request.
    """
    query = select(models.Book).offset(skip).limit(limit)
    result: AsyncResult = await db.execute(query)
    return result.scalars().all()


async def get_by_id(db: Session, id: UUID) -> schemas.BookInDatabase:
    """Get single book from the database by ID

    Args:
        db (Session): database to interact with
    """
    query = select(models.Book).where(models.Book.id == id)
    result: AsyncResult = await db.execute(query)

    return result.scalars().first()


async def add(db: Session, book: schemas.Book):
    """Add book to the database

    Args:
        db (Session): database to interact with
        book (BookSchema): book to add to the database
    """
    query = insert(models.Book).values(**book.dict())
    result: AsyncResult = await db.execute(query)
    print(result.__dict__)
    # return models.Book(**book.dict())
    return result.scalars().first()


async def delete_one(db: Session, id: UUID) -> None:
    """Delete book from database

    Args:
        db (Session): database to interact with
        id (UUID): Book ID
    """
    book = await db.execute(select(models.Book).where(models.Book.id == id))

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID: {id} does not exist",
        )

    query = delete(models.Book).where(models.Book.id == id)
    await db.execute(query)


async def update_one(
    db: Session, id: UUID, book: schemas.Book
) -> schemas.BookInDatabase:
    """Update book from database

    Args:
        db (Session): database to interact with
        id (UUID): Book ID
    """
    query = update(models.Book).where(models.Book.id == id).values(**book.dict())
    await db.execute(query)
    return {**book.dict()}
