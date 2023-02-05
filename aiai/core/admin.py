from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(ProductImage)


# class ColorKAdmin(admin.ModelAdmin):
#   pass


# class ColorKInline(admin.StackedInline):
#   model = ColorK
#   max_num = 10
#   extra = 0


# class ProductAdmin(admin.ModelAdmin):
#   inlines = [ColorKInline,]

# admin.site.register(ColorK, ColorKAdmin)
# admin.site.register(Products, ProductAdmin)
admin.site.register(Products)
admin.site.register(ColorK)
admin.site.register(Customer)
admin.site.register(CodeP)
admin.site.register(Order)