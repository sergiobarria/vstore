from typing import List
from uuid import UUID

from app.api.deps import get_session
from app.models import Author, AuthorCreate, AuthorRead, AuthorUpdate
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

router = APIRouter()


@router.get("/", response_model=List[AuthorRead])
async def get_authors(*, session: AsyncSession = Depends(get_session)):
    """Get all authors from DB"""
    q = select(Author)
    result = await session.execute(q)
    authors = result.scalars().all()
    return authors


@router.post("/", response_model=AuthorRead, status_code=status.HTTP_201_CREATED)
async def add_author(
    *, session: AsyncSession = Depends(get_session), author: AuthorCreate
):
    """Add new author to DB"""
    db_author = Author.from_orm(author)
    session.add(db_author)
    await session.commit()
    await session.refresh(db_author)
    return db_author


@router.get("/{author_id}", response_model=AuthorRead)
async def get_author_by_id(
    *, author_id: UUID, session: AsyncSession = Depends(get_session)
):
    """Get single author by ID"""
    author = await session.get(Author, author_id)

    if not author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Author with ID of {author_id} not found.",
        )

    return author


@router.patch("/{author_id}", response_model=AuthorRead)
async def update_author(
    *,
    author_id: UUID,
    author: AuthorUpdate,
    session: AsyncSession = Depends(get_session),
):
    """Update author by ID"""
    db_author = await session.get(Author, author_id)

    if not db_author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Author with ID of {author_id} not found",
        )

    author_data = author.dict(exclude_unset=True)

    for key, value in author_data.items():
        setattr(db_author, key, value)

    session.add(db_author)
    await session.commit()
    await session.refresh(db_author)
    return db_author


@router.delete("/{author_id}")
async def delete_author(
    *, author_id: UUID, session: AsyncSession = Depends(get_session)
):
    "Delete author by ID"
    author = await session.get(Author, author_id)

    if not author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Author with ID of {author_id} not found.",
        )

    await session.delete(author)
    await session.commit()
    return {"status": "ok"}
