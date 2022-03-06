from typing import List
from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import insert, select, delete, update
from app.models import BookModel

from app import models, schemas


async def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[models.BookModel]:
    """Get all books from the database

    Args:
        db (Session): database to interact with
        skip (int, optional): the ammount of items to skip (useful for pagination).
        limit (int, optional): the max limit of items to retrieve for each request.
    """
    query = await db.execute(select(models.BookModel))
    return query.scalars().all()


async def get_by_id(db: Session, id: UUID) -> schemas.BookInDatabase:
    """Get single book from the database by ID

    Args:
        db (Session): database to interact with
    """
    query = await db.execute(select(models.BookModel).where(BookModel.id == id))
    result = query.scalars().first()

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Item with ID: {id} does not exist")

    return result


async def add(db: Session, book: schemas.BookSchema):
    """Add book to the database

    Args:
        db (Session): database to interact with
        book (BookSchema): book to add to the database
    """
    query = insert(models.BookModel).values(**book.dict())
    await db.execute(query)
    return models.BookModel(**book.dict())


async def delete_one(db: Session, id: UUID) -> None:
    """Delete book from database

    Args:
        db (Session): database to interact with
        id (UUID): Book ID
    """
    book = await db.execute(select(models.BookModel).where(BookModel.id == id))

    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Item with ID: {id} does not exist")

    query = delete(models.BookModel).where(BookModel.id == id)
    await db.execute(query)


async def update_one(db: Session, id: UUID, book: schemas.BookSchema) -> schemas.BookInDatabase:
    """Update book from database

    Args:
        db (Session): database to interact with
        id (UUID): Book ID
    """
    query = update(models.BookModel).where(
        BookModel.id == id).values(**book.dict())
    await db.execute(query)
    return {**book.dict()}
