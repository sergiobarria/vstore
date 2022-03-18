from uuid import uuid4

from django.db import models


class Author(models.Model):
    """Author model for database"""

    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)
    first_name = models.CharField(max_length=50, db_index=True, blank=False)
    last_name = models.CharField(max_length=50, db_index=True, blank=False)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Methods
    def get_full_name(self):
        """Join author first and last name"""
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        """String for representing the model object name"""
        return self.get_full_name()
