from rest_framework import serializers

from genres.models import Genre


class GenreSerializer(serializers.ModelSerializer):
    """Genre Serializer"""

    class Meta:
        model = Genre
        fields = ["id", "name"]
