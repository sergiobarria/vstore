from authors.models import Author
from genres.serializers import GenreSerializer
from rest_framework import serializers

from .models import Book


class AuthorSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "first_name", "last_name"]


class BookSerializer(serializers.ModelSerializer):
    """Book Serializer"""

    language = serializers.CharField(source="language.name")
    genres = GenreSerializer(many=True)

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "hardcover_price",
            "paperback_price",
            "published_year",
            "isbn",
            "authors",
            "language",
            "genres",
        ]


class BookDetailSerializer(serializers.ModelSerializer):
    """Get or update book details"""

    language = serializers.CharField(source="language.name")
    authors = AuthorSimpleSerializer(many=True)
    genres = GenreSerializer(many=True)

    class Meta:
        model = Book
        fields = "__all__"
