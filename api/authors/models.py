from uuid import uuid4

from django.db import models


class Author(models.Model):
    """Author model for database"""

    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=100, db_index=True, unique=True, null=False, blank=False)
    bio = models.CharField(max_length=7000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Relationships
    books = models.ManyToManyField("books.Book", blank=True)
