from django.contrib.auth.models import User
from django.db import models


class Problem(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(blank=True, verbose_name='Текст')
    photo = models.ImageField(upload_to="photos", verbose_name='Фото')
    author = models.CharField(max_length=255, verbose_name='Автор')
    recipient = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Адресат')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
