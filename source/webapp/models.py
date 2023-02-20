from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(
        max_length=200, null=False, blank=False, verbose_name="Наименование")
    description = models.TextField(
        max_length=3000, null=True, blank=True, verbose_name="Описание")

    def __str__(self):
        return f"{self.category_name} - {self.category_name}"


class Product(models.Model):
    product_name = models.CharField(
        max_length=200, null=False, blank=False, verbose_name="Наименование")
    description = models.TextField(
        max_length=3000, null=True, blank=True, verbose_name="Описание")
    category = models.ForeignKey(
        to='webapp.Category',
        verbose_name='Категория',
        null=False,
        blank=False,
        related_name='categories',
        on_delete=models.RESTRICT
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Время и дата создания")
    price = models.DecimalField(
        decimal_places=2, max_digits=20, null=False, blank=False, verbose_name="Цена")
    image_url = models.CharField(
        max_length=200, null=False, blank=False, verbose_name="Картинка")

    def __str__(self):
        return f"{self.text} - {self.created_at}"
