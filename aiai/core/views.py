from .models import * 
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404

# Create your views here.

from django import template
register = template.Library()

@register.simple_tag()
def multiply(qty, *args, **kwargs):
    # you would need to do any localization of the result here
    return qty * 4


def products(request):
    products = Products.objects.all()
    products = Products.objects.order_by('-created_at')
    context = {
        "products": products,
    }
    return render(
        request,
        "index.html",
        context=context
    )

def products_page(request, id):
    product = get_object_or_404(Products, id=id)
    products = Products.objects.all()
    colors = ColorK.objects.all()
    context = {
        "product": product,
        "products": products,
        "colors": colors,
    }
    return render(request, "page.html", context=context)