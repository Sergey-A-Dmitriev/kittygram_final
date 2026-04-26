"""Модуль Админка."""

from django.contrib import admin

from cats.models import Achievement, Cat


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    """Админка для достижений."""

    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    """Админка для котов."""

    list_display = ('id', 'name', 'color', 'birth_year',
                    'owner')
    list_filter = ('birth_year',)
    search_fields = ('name', 'owner', 'color', 'achievements')
