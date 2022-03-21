# VStore

> Full-stack book store online ecommerce application

## Overview

Full-stack ecommerce application for online book selling. The application allows the user to register a new account and order different books on several formats and languages.

Once the user is registered he/she can order and review books if they have purchased them. Users have access to their profile where they can see all their recent activity on the website, like orders, reviews and so on.

## Tech Stack

- **Server Application:**
  - API: Python - Django
  - Database: SQL - PostgreSQL
- **Frontend Application:**
  - UI: JavaScript - Vue
  - Styling: Tailwind CSS
  - State Management: Pinia
- **Mobile Application:**
  - UI: Dart - Flutter
  - State Management:

## Folder Structure

The repository contains all the different applications related to the project, meaning:

- **API:** full api built using Python - Django and The Django Rest Frameworkd
- **Web App:** client application built with Vue to consume the back-end API
- **Mobile App:** client mobile app built with Flutter to consume the back-end API

### Global Repo Structure

```
vstore/
├── api
├── apps/
│ ├── mobile
│ └── web
├── assets
├── data
├── .gitignore
└── README.md
```

### API Folder Structure

Each folder inside the api directory (minus the templates subdirectore) represents a different Django App. The `Core` app represents the main API directory.

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
└── app/
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

### Web App Folder Structure

```
web/
├── public
├── src/
│   ├── assets
│   ├── components
│   ├── composables
│   ├── layout
│   ├── lib
│   ├── router
│   ├── stores
│   ├── styles
│   └── views
├── .eslintrc.js
├── .prettierrc
├── index.html
├── jsconfig.json
├── package.json
├── postcss.config.js
├── README.md
├── tailwind.config.js
└── vite.config.js
```

## Env Variables

Before running the application you need to create a `.env` file in the root of the repositorie with your environment variables, check `.env.example` in the repo root.

## Running each application

### Run server API

```bash
$ cd api
$ poetry install
$ poetry shell # to activate virtual env if not activate yet
$ python manage.py runserver
```

### Run web app

```bash
$ cd apps/web # from root directory

# Install dependencies and run dev server
$ yarn && yarn dev

# or if using npm

$ npm install && npm run dev
```
