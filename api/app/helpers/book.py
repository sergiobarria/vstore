from sqlalchemy.orm import Session

from app import models, schemas


def get_all(db: Session, skip: int = 0, limit: int = 100):
    """Get all books from the database

    Args:
        db (Session): database to interact with
        skip (int, optional): the ammount of items to skip (useful for pagination).
        limit (int, optional): the max limit of items to retrieve for each request.
    """
    return db.query(models.Book).offset(skip).limit(limit).all()


def get_by_id(db: Session, id: int):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    return book


def add(db: Session, book: schemas.Book):
    """Add book to the database

    Args:
        db (Session): database to interact with
        book (BookSchema): book to add to the database
    """
    new_book = models.Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book
