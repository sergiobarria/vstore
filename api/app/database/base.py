# Import all the models, so that Base has them before being
# imported by Alembic

from app.database.db import Base
from app.models.book import Book
