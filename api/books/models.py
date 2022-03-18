from datetime import datetime
from uuid import uuid4

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Language(models.Model):
    """Model to represent a book Language"""

    name = models.CharField(max_length=200)

    def __str__(self):
        """String for representing the model object."""
        return self.name


class Book(models.Model):
    """Book model for database"""

    class Meta:
        ordering = ["title"]

    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200, db_index=True)
    summary = models.TextField()
    hardcover_price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    paperback_price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    published_year = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(1900, message="Min allowed year 1900"),
            MaxValueValidator(datetime.now().year, message=f"Max allowed year {datetime.now().year}"),
        ],
    )
    isbn = models.CharField("ISBN", max_length=13, unique=True)
    num_of_pages = models.PositiveIntegerField(blank=False, null=False)
    reading_age = models.PositiveIntegerField(blank=True, null=True)
    item_weight = models.FloatField(
        blank=False,
        null=False,
        default=0,
        validators=[MinValueValidator(0, message="Please add a valid weight value")],
    )
    stock_qty = models.PositiveIntegerField(blank=False, null=False, default=1)
    is_bestseller = models.BooleanField(default=False)
    # dimensions = update when adding postgres as database
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Relationships
    genres = models.ManyToManyField("genres.Genre", blank=True)
    authors = models.ManyToManyField("authors.Author", related_name="book_list", blank=True)

    # Methods
    def __str__(self):
        """String for representing the Model Object (in admin site)"""
        return self.title

    # def display_genre(self):
    #     """Creates a string for the Genre model. Required to display genre in admin."""
    #     return ", ".join([genre.name for genre in self.genres.all()[:3]])
