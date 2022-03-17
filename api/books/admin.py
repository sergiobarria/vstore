from django.contrib import admin

from .models import Book, Language


class BookAdmin(admin.ModelAdmin):
    """Book representation on the admin site"""

    list_filter = ("title",)
    # list_display = (
    #     "title",
    #     "authors",
    # )


# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Language)
