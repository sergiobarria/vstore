from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """Book Serializer"""

    language = serializers.CharField(source="language.name")

    class Meta:
        model = Book
        fields = "__all__"  # also can be individual fields
        # depth = 1
