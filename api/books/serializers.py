from authors.models import Author
from genres.serializers import GenreSerializer
from rest_framework import serializers

from .models import Book, Image


class AuthorSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "full_name"]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "url"]


class BookSerializer(serializers.ModelSerializer):
    """Book Serializer"""

    language = serializers.PrimaryKeyRelatedField(source="language.name", many=False, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    authors = AuthorSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        exclude = ["summary"]


class BookDetailSerializer(serializers.ModelSerializer):
    """Get or update book details"""

    language = serializers.PrimaryKeyRelatedField(source="language.name", many=False, read_only=True)
    authors = AuthorSimpleSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = "__all__"
