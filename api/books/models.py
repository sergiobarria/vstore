from datetime import datetime
from uuid import uuid4

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    """Book model for database"""

    class Language(models.TextChoices):
        """Book language choices"""

        ENGLISH = "ENG", _("English")
        SPANISH = "SPN", _("Spanish")

    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200, db_index=True)
    summary = models.CharField(max_length=2000)
    hardcover_price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    paperback_price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    language = models.CharField(max_length=50, choices=Language.choices, default=Language.ENGLISH)
    published_year = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(1900, message="Min allowed year 1900"),
            MaxValueValidator(datetime.now().year, message=f"Max allowed year {datetime.now().year}"),
        ],
    )
    num_of_pages = models.PositiveIntegerField(blank=False, null=False)
    reading_age = models.PositiveIntegerField(blank=True, null=True)
    item_weight = models.PositiveIntegerField(blank=False, null=False, default=0)
    stock_qty = models.PositiveIntegerField(blank=False, null=False, default=1)
    is_bestseller = models.BooleanField(default=False)
    # dimensions = update when adding postgres as database
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Relationships
    genres = models.ManyToManyField("genres.Genre")
    authors = models.ManyToManyField("authors.Author")
