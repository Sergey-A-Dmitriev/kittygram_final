"""Модуль для описания приложений cats."""

from django.apps import AppConfig


class CatsConfig(AppConfig):
    """Класс CatsConfig."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cats'
