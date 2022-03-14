from typing import List
from uuid import UUID

from app import models, schemas
from app.database.session import get_session
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.GenreRead])
async def get_genres(*, session: Session = Depends(get_session)):
    """Get all genres from DB"""
    genres = session.query(models.Genre).all()
    return genres


@router.post("/", response_model=schemas.GenreRead, status_code=status.HTTP_201_CREATED)
async def add_genre(
    *, session: Session = Depends(get_session), genre: schemas.GenreCreate
):
    """Add new genre to DB"""
    db_genre = models.Genre(**genre.dict())
    session.add(db_genre)
    session.commit()
    session.refresh(db_genre)
    return db_genre


# @router.get("/{genre_id}")
# async def get_genre_by_id():
#     pass


@router.put("/{genre_id}", response_model=schemas.GenreRead)
async def update_genre(
    *,
    genre_id: UUID,
    genre: schemas.GenreUpdate,
    session: Session = Depends(get_session),
):
    """Update genre by ID"""
    db_genre = session.query(models.Genre).filter_by(id=genre_id).first()

    if not db_genre:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Genre with ID of {genre_id} not found.",
        )

    # eclude_unset removes fields not provided in the request
    genre_data = genre.dict(exclude_unset=True)

    for key, value in genre_data.items():
        setattr(db_genre, key, value)

    session.add(db_genre)
    session.commit()
    session.refresh(db_genre)
    return db_genre


@router.delete("/{genre_id}")
async def delete_genre(*, genre_id: UUID, session: Session = Depends(get_session)):
    """Delete genre"""
    genre = session.query(models.Genre).filter_by(id=genre_id).first()

    if not genre:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Genre with ID of {genre_id} not found.",
        )

    session.delete(genre)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
