# conftest.py
import os
import django
import pytest

# Define qual settings usar
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "book.settings")  # ajuste se o nome do seu settings for outro

# Inicializa o Django
django.setup()

# Opcional: se você quiser usar fixtures do pytest-django
pytest_plugins = ["django.contrib.auth", "django.contrib.sessions"]
