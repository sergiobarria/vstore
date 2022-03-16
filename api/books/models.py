from django.db import models


class Book(models.Model):
    """Book model for database"""

    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=7000)
    hardcover_price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    paperback_price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
