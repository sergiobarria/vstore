from uuid import uuid4

from django.db import models


class Genre(models.Model):
    """Genre model for database"""

    class Meta:
        ordering = ["name"]

    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=50, null=False, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
