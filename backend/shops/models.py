from django.db import models


class MarketTag(models.Model):
    name = models.CharField('Название тега', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег мазагина'
        verbose_name_plural = 'Теги мазагинов'


class Market(models.Model):
    name = models.CharField('Название магазина', max_length=50)
    description = models.TextField('Описание магазина', default='')
    phone = models.CharField('Основной номер', max_length=15)
    tags = models.ManyToManyField(MarketTag, blank=True, verbose_name='Теги')
    logo = models.FileField(upload_to='shops/logotypes/')
    is_verify = models.BooleanField('Статус верификации', default=False)
    is_active = models.BooleanField('Активность магазина', default=False)
    owner = models.ForeignKey('users.User', models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class MarketItem(models.Model):
    name = models.TextField('Название')
    description = models.TextField('Описание')
    price = models.IntegerField('Цена', default=None, null=True, blank=True)
    amount = models.IntegerField('Количество', default=1)
    market = models.ForeignKey(Market, models.CASCADE, null=True)

    attributes = models.JSONField('Атрибуты', null=True, blank=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
