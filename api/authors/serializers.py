from books.models import Book
from rest_framework import serializers

from .models import Author


class BookSimpleSerializer(serializers.ModelSerializer):
    """Simple book model serializer"""

    class Meta:
        model = Book
        fields = ["id", "title"]


class AuthorSerializer(serializers.ModelSerializer):
    """Author model serializer"""

    book_list = BookSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "full_name", "profile_img", "book_list"]


class AuthorDetailSerializer(serializers.ModelSerializer):
    """Get or update authors details"""

    book_list = BookSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "full_name", "profile_img", "bio", "book_list"]
