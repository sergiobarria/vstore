# Generated by Django 4.0.3 on 2022-03-16 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_genre_book_created_at_book_is_bestseller_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(db_index=True, max_length=50, unique=True),
        ),
    ]