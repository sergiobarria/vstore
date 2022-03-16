from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """Book Serializer"""

    class Meta:
        model = Book
        fields = "__all__"  # also can be individual fields
