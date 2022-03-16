from uuid import UUID

from django.http import HttpRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from authors.models import Author
from authors.serializers import AuthorSerializer


@api_view(["GET", "POST"])
def author_list(request: HttpRequest):
    """List all authors in database, or create a new author"""

    if request.method == "GET":
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        response = {"status": "success", "data": serializer.data}

        return Response(response)

    if request.method == "POST":
        serializer = AuthorSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        response = {"status": "success", "data": serializer.data}
        return Response(response, status=status.HTTP_201_CREATED)


@api_view(["GET", "PATCH", "DELETE"])
def author_detail(request: HttpRequest, author_id: UUID):
    """Get single author, update or delete author"""
    try:
        author: Author | None = Author.objects.get(pk=author_id)
    except Author.DoesNotExist:
        response = {"status": "fail", "message": f"Author with ID of {author_id} not found."}

        return Response(response, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = AuthorSerializer(author)
        response = {"status": "success", "data": serializer.data}

        return Response(response)

    if request.method == "PATCH":
        serializer = AuthorSerializer(author, data=request.data, partial=True)

        if not serializer.is_valid():
            response = {"status": "fail", "errors": serializer.errors}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        response = {"status": "success", "data": serializer.data}

        return Response(response)

    if request.method == "DELETE":
        author.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
