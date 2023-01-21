from django.db import models
from django.db.models import F
# from django.contrib.auth.models import User
from django.forms import BooleanField, CharField, ImageField
# from django.utils.translation import gettext_lazy as _
from django.shortcuts import reverse


class ColorK(models.Model):
    picture = models.ImageField(upload_to="product__image", blank=True, verbose_name="Картинка цветов", db_index=True)
    # products = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.picture

class Products(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField()
    color = models.CharField(max_length=100, null=True, blank=True)
    tekstil = models.CharField(max_length=155, null=True, blank=True)
    fixed__price__i = 4
    colors = models.ManyToManyField(ColorK, related_name='colors')
    # slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True, blank=True)
    # heading = models.ForeignKey(
    #     to="HeadingArticle",
    #     on_delete=models.PROTECT,
    #     null=True,
    #     related_name="article",
    #     verbose_name=_("Рубрика")
    # )

    # readers = models.ManyToManyField(
    #     to=User,
    #     related_name="readed_articles",
    #     blank=True,
    #     verbose_name=_("Читатели")
    # )

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
    )

    # metades = models.TextField(null=True, blank=True, verbose_name=_("Ключевые слова"))

    picture = models.FileField(
        upload_to="product_image",
        blank=True,
        verbose_name="Картинки товаров"    
    )

    def __str__(self):
        return self.title
