# My-store

A simple Django-based e-commerce project.

## Overview

This repository contains a Django project named `ecom` with a `store` app. It includes a sample SQLite database (`ecom/db.sqlite3`) and some static/media files for development.

## Features

- Product listing and basic store views
- Admin interface (Django admin)
- Templates and static files included for quick testing

## Requirements

- Python 3.8 or newer
- pip

## Setup (development)

1. Clone the repository:

   git clone https://github.com/yashpawar69/My-store.git
   cd My-store/ecom

2. (Recommended) Create and activate a virtual environment:

   python -m venv env
   source env/bin/activate   # macOS/Linux
   env\Scripts\activate    # Windows (PowerShell)

   Note: This repo contains a `virt/` directory that appears to be a committed virtual environment. It's recommended to remove committed virtual environments and add `virt/` to `.gitignore`.

3. Install dependencies:

   If you have a requirements.txt file, run:

   pip install -r requirements.txt

   Otherwise, install Django manually:

   pip install django

4. Apply migrations:

   python manage.py migrate

5. (Optional) If you want to use the included sample database, it's located at `ecom/db.sqlite3`. Be aware it may contain sample data.

6. Create a superuser to access the admin:

   python manage.py createsuperuser

7. Run the development server:

   python manage.py runserver

8. Open http://127.0.0.1:8000/ in your browser.

## Notes & Recommendations

- Consider removing `db.sqlite3` and the `virt/` directory from the repository and add them to `.gitignore` to avoid committing environment-specific files and database data.
- Add a `requirements.txt` to make dependency installation reproducible (generate with `pip freeze > requirements.txt`).
- Configure `ALLOWED_HOSTS` and secret key handling before deploying to production.

## Project structure (high level)

- ecom/ - Django project folder
  - ecom/settings.py
  - ecom/urls.py
  - manage.py
  - db.sqlite3 (sample database)
  - store/ - Django app with models, views, templates

## License

Add a license as needed.
