from uuid import UUID

from django.http import HttpRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from books.models import Book
from books.serializers import BookSerializer


@api_view(["GET", "POST"])
def books_list(request: HttpRequest):
    """List all books in database, or create a new book and save it to database"""
    if request.method == "GET":
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)
        response = {"status": "success", "data": serializer.data}

        return Response(response)

    if request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PATCH", "DELETE"])
def book_detail(request: HttpRequest, book_id: UUID):
    """Get single book details, update or delete book"""
    try:
        book: Book | None = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        response = {"status": "fail", "message": f"Book with IF of {book_id} not found."}

        return Response(response, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BookSerializer(book)
        response = {"status": "success", "data": serializer.data}

        return Response(response)

    if request.method == "PATCH":
        serializer = BookSerializer(book, data=request.data, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        response = {"status": "success", "data": serializer.data}

        return Response(response)

    if request.method == "DELETE":
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
