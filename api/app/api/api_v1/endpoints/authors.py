from typing import List
from uuid import UUID

from app import models, schemas
from app.database.session import get_session
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.AuthorRead])
def get_authors(*, session: Session = Depends(get_session)):
    """Get all authors from DB"""
    authors = session.query(models.Author).all()
    return authors


@router.post(
    "/", response_model=schemas.AuthorRead, status_code=status.HTTP_201_CREATED
)
def add_author(
    *, session: Session = Depends(get_session), author: schemas.AuthorCreate
):
    """Add new author to DB"""
    db_author = models.Author(**author.dict())
    session.add(db_author)
    session.commit()
    session.refresh(db_author)
    return db_author


@router.get("/{author_id}", response_model=schemas.AuthorRead)
def get_author_by_id(*, author_id: UUID, session: Session = Depends(get_session)):
    """Get single author by ID"""
    author = session.query(models.Author).filter(models.Author.id == author_id).first()

    if not author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Author with ID of {author_id} not found.",
        )

    return author


@router.put("/{author_id}")
def update_author(
    *,
    author_id: UUID,
    author: schemas.AuthorUpdate,
    session: Session = Depends(get_session),
):
    """Update author by ID"""
    db_author = (
        session.query(models.Author).filter(models.Author.id == author_id).first()
    )

    if not db_author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Author with ID of {author_id} not found",
        )

    author_data = author.dict(exclude_unset=True)

    for key, value in author_data.items():
        setattr(db_author, key, value)

    session.add(db_author)
    session.commit()
    session.refresh(db_author)
    return db_author


@router.delete("/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_author(*, author_id: UUID, session: Session = Depends(get_session)):
    """Delete author by ID"""
    author = session.query(models.Author).filter_by(id=author_id).first()

    if not author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Author with ID of {author_id} not found.",
        )

    session.delete(author)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
