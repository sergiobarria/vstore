from django.http import HttpRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from genres.models import Genre
from genres.serializers import GenreSerializer


@api_view(["GET", "POST"])
def genre_list(request: HttpRequest):
    """List all genres, or create a new genre"""
    if request.method == "GET":
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        response = {"status": "success", "data": serializer.data}

        return Response(response)

    if request.method == "POST":
        serializer = GenreSerializer(data=request.data)
        if not serializer.is_valid():
            response = {"status": "fail", "errors": serializer.errors}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        response = {"status": "success", "data": serializer.data}
        return Response(response, status=status.HTTP_201_CREATED)
