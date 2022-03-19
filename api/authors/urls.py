from django.urls import path

from .views import author_detail, author_list

# endpoint: /api/v1/authors
urlpatterns = [
    path("", author_list, name="add_get_authors"),
    path("<uuid:author_id>", author_detail, name="get_update_delete_author"),
]
