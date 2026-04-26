"""Модуль для описания моделей приложения cats."""

from django.contrib.auth import get_user_model
from django.db import models

from cats.constants import SIZE_ACHIV_NAME_FIELD, SIZE_FIELD, SIZE_TEXT_FIELD

User = get_user_model()


class Achievement(models.Model):
    """Модель Achievement."""

    name = models.CharField(max_length=SIZE_ACHIV_NAME_FIELD,
                            verbose_name='достижение')

    def __str__(self):
        """Магический метод __str__."""
        return self.name[:SIZE_TEXT_FIELD]


class Cat(models.Model):
    """Модель Cat."""

    name = models.CharField(max_length=SIZE_FIELD,
                            verbose_name='имя')
    color = models.CharField(max_length=SIZE_FIELD,
                             verbose_name='цвет')
    birth_year = models.IntegerField(verbose_name='год рождения')
    owner = models.ForeignKey(User,
                              related_name='cats',
                              on_delete=models.CASCADE,
                              verbose_name='хозяин')
    achievements = models.ManyToManyField(Achievement,
                                          through='AchievementCat',
                                          verbose_name='достижение')
    image = models.ImageField(
        upload_to='cats/images/',
        null=True,
        default=None
    )

    def __str__(self):
        """Магический метод __str__."""
        return self.name[:SIZE_TEXT_FIELD]


class AchievementCat(models.Model):
    """Промежуточная модель для связи Achievement и Cat."""

    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    class Meta:
        """Класс Meta."""

        verbose_name = 'Достижение кота'
        verbose_name_plural = 'Достижения кота'

    def __str__(self):
        """Магический метод __str__."""
        return f'{self.achievement} {self.cat}'
