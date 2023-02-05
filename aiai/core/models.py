from django.db import models
from django.db.models import F
from django.contrib.auth.models import User


class CodeP(models.Model):
    code = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        return self.code
    

class Customer(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=133, verbose_name='Имя заказсчика')
    # phone_code = models.ForeignKey(CodeP, on_delete=models.CASCADE, null=True, blank=True)
    phone_code = models.CharField(max_length=10, null=True, blank=True)
    phone_number = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return str(self.name)

class ColorK(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название", null=True)
    picture = models.ImageField(upload_to="product__image", blank=True, verbose_name="Картинка цветов", db_index=True)

    def __str__(self):
        return str(self.name)

class Products(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField()
    color = models.CharField(max_length=100, null=True, blank=True)
    tekstil = models.CharField(max_length=155, null=True, blank=True)
    fixed__price__i = 4
    colors = models.ManyToManyField(ColorK, related_name='colors')
    discount = models.IntegerField(null=True)
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
    )

    picture = models.FileField(
        upload_to="product_image",
        blank=True,
        verbose_name="Картинки товаров"    
    )

    def __str__(self):
        return self.title


class Order(models.Model):
    name = models.CharField(max_length=255, null=True)
    phoneNumber = models.CharField(max_length=255, null=True)
    phoneCode = models.CharField(max_length=255, null=True)
    # address = models.CharField(max_length=255, null=True)
    cityAddress = models.CharField(max_length=255, null=True)
    # quantity = models.CharField(max_length=150, null=True)
    productChoosed = models.CharField(max_length=255, null=True)
    # colors = models.CharField(max_length=355, null=True)
    # total = models.CharField(max_length=255, null=True)
    colorsValue = models.CharField(max_length=255, null=True, verbose_name="Расцветки")
    cashMethod = models.CharField(max_length=255, null=True, blank=True, verbose_name="Наличные")
    bankCartMethod = models.CharField(max_length=255, null=True, blank=True, verbose_name="Банковская карта")
    mbank = models.CharField(max_length=255, null=True, blank=True, verbose_name="МБанк")
