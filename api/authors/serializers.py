from rest_framework import serializers

from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    """Author model serializer"""

    class Meta:
        model = Author
        fields = "__all__"
