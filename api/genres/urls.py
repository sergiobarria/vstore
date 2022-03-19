from django.urls import path

from .views import genre_list

# endpoint: /api/v1/genres/
urlpatterns = [path("", genre_list, name="add_get_genres")]
