from django.contrib import admin

from .models import Book, Image, Language


class BookAdmin(admin.ModelAdmin):
    """Book representation on the admin site"""

    list_filter = ("title", "authors")
    list_display = ("title", "hardcover_price", "paperback_price", "published_year")


class ImageAdmin(admin.ModelAdmin):
    """Image representation on the admin site"""

    list_display = ("id", "book")
    list_filter = ("book",)


# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Language)
