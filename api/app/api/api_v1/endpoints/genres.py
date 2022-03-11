from typing import List
from uuid import UUID

from app.api.deps import get_session
from app.models import Genre, GenreCreate, GenreRead, GenreUpdate
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

router = APIRouter()


@router.get("/", response_model=List[GenreRead])
async def get_genres(*, session: AsyncSession = Depends(get_session)):
    """Get all genres from DB"""
    q = select(Genre)
    result = await session.execute(q)
    genres = result.scalars().all()
    return genres


@router.post("/", response_model=GenreRead, status_code=status.HTTP_201_CREATED)
async def add_genre(
    *, session: AsyncSession = Depends(get_session), genre: GenreCreate
):
    """Add new genre to DB"""
    db_genre = Genre.from_orm(genre)
    session.add(db_genre)
    await session.commit()
    await session.refresh(db_genre)
    return db_genre


# @router.get("/{genre_id}")
# async def get_genre_by_id():
#     pass


@router.patch("/{genre_id}", response_model=GenreRead)
async def update_genre(
    *, genre_id: UUID, genre: GenreUpdate, session: AsyncSession = Depends(get_session)
):
    """Update genre by ID"""
    db_genre = await session.get(Genre, genre_id)

    if not db_genre:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Genre with ID of {genre_id} not found.",
        )

    genre_data = genre.dict(exclude_unset=True)

    for key, value in genre_data.items():
        setattr(db_genre, key, value)

    session.add(db_genre)
    await session.commit()
    await session.refresh(db_genre)
    return db_genre


@router.delete("/{genre_id}")
async def delete_genre(*, genre_id: UUID, session: AsyncSession = Depends(get_session)):
    """Delete genre"""
    genre = await session.get(Genre, genre_id)

    if not genre:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Genre with ID of {genre_id} not found.",
        )

    await session.delete(genre)
    await session.commit()
    return {"status": "ok"}
