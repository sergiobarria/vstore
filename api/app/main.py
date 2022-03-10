# import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, description=settings.DESCRIPTION)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Include API Endpoints
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/")
async def root():
    return "Hello World"


# if __name__ == "__main__":
#     uvicorn.run("app.main:app", host="0.0.0.0", port="8000", reload=True)
