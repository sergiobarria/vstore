from django.urls import path

# from .views import add_book, get_books
from .views import book_detail, books_list

# endpoint: /api/v1/books/
urlpatterns = [
    path("", books_list, name="add_get_books"),
    path("<int:book_id>", book_detail, name="get_update_delete_book"),
]
