from uuid import uuid4

from django.db import models


class Author(models.Model):
    """Author model for database"""

    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)
    first_name = models.CharField(max_length=50, db_index=True, blank=False)
    last_name = models.CharField(max_length=50, db_index=True, blank=False)
    profile_img = models.ImageField(upload_to="authors/", blank=True)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Methods
    def __str__(self):
        """String for representing the model object name"""
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        """Returns author full name"""
        return "%s %s" % (self.first_name, self.last_name)
