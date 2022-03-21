# VStore - API

> Back-end server API for the VStore ecommerce

## Tech Stack

- **Language:** Python
- **Framework:** Django - Django Rest Framework
- **Database:** PostgreSQL
- **Authentication:** Djoser - SimpleJWT

## Folder Structure

```
api/
├── authors
├── books
├── core
├── genres
├── templates
├── .flake8
├── manage.py
├── poetry.lock
└── pyproject.toml
```

Each one of the API apps contains an structure similar to the following:

```
api/
└── books/
    ├── migrations/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

## Run server API

```bash
$ cd api
$ poetry install
$ poetry shell # to activate virtual env if not activate yet
$ python manage.py runserver
```
