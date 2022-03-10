from app.api.api_v1.endpoints import authors, books, genres
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(books.router, prefix="/books", tags=["Books"])
api_router.include_router(authors.router, prefix="/authors", tags=["Authors"])
api_router.include_router(genres.router, prefix="/genres", tags=["Genres"])
