from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/', verbose_name='Фотография')
    caption = models.CharField(max_length=200, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    favorite_users = models.ManyToManyField(
        User,
        related_name='favorite_photos',
        blank=True,
        verbose_name='Пользователи, добавивишие в избранное'
    )

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
