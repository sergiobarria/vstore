# Import all the models, so that Base has them before being
# imported by Alembic

from app.database.base_class import Base
from app.models import BookModel
