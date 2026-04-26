"""Модуль views приложения cats."""

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from cats.models import Achievement, Cat
from cats.serializers import AchievementSerializer, CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    """Вьюсет Cat."""

    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        """Метод perform_create."""
        serializer.save(owner=self.request.user)


class AchievementViewSet(viewsets.ModelViewSet):
    """Вьюсет Achievement."""

    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    pagination_class = None
