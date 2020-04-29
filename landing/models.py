from django.db import models
from django.core import validators

class Subscriber(models.Model):
    name = models.CharField(max_length=128, verbose_name='имя')
    email = models.EmailField(verbose_name='адрес почты', validators = [validators.EmailValidator('адрес должен быть корректным')])
    class Meta:
        """определение метаданных"""
        verbose_name = 'подписчик'
        verbose_name_plural = 'подписчики'
        ordering = ['name']

    def __str__(self):
        return f'пользователь {self.name} {self.email}' 