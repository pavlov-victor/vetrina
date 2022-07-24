from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    middle_name = models.CharField('Отчество', max_length=120, default='')
    phone = models.CharField('Номер телефона', max_length=15)
    telegram_name = models.CharField('Имя в телеграме', max_length=30)
    hide = models.BooleanField('Статус скрытности', default=True)
