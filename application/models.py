from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Тип товару')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Тип товару'
        verbose_name_plural = 'Типи товарів'


class Product(models.Model):
    name = models.CharField(max_length=128, blank=False, verbose_name='Назва продукту')
    category = models.ForeignKey(Category, blank=False, verbose_name='Тип')
    price = models.PositiveIntegerField(blank=False, default=0, verbose_name='Ціна')
    image = models.ImageField(upload_to='production_image/', verbose_name='Фото')
    description = models.TextField(verbose_name='Опис')
    flag = models.BooleanField(default=True, verbose_name='акт/деакт')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    updated = models.DateTimeField(auto_now=True, verbose_name='Оновлено')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'
