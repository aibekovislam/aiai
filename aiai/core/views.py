from .models import * 
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

User = get_user_model()

def products(request):
    products = Products.objects.all()
    products = Products.objects.order_by('-created_at')
    paginator = Paginator(products, per_page=30)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "products": page_obj.object_list,
        "paginator": paginator,
        "page_number": int(page_number)
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



def sign_in(request):
    customer = Customer.objects.all()
    codep = CodeP.objects.all()
    context = {
        "customer": customer,
        "codep": codep
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        phone__number = request.POST.get('phone_number')
        password = request.POST.get('password')
        user = authenticate(username=username, phone__number=phone__number, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(products)
                
    return render(request, 'user.html', context=context)


def sign_out(request):
    logout(request)
    return redirect(products)


def registration(request):
    customer = Customer.objects.all()
    codep = CodeP.objects.all()
    context = {
        "customer": customer,
        "codep": codep
    }
    if request.method == "GET":
        return render(request, 'create.html', context=context)
    # elif request.method == "POST":
    #     form = request.POST
    #     phone_number = form.get('phone_number')
    #     phone_code = form.get('phone_code')
    #     name = form.get('name')
    #     newCusomer = Customer()
    #     newCusomer.phone_number = phone_number
    #     newCusomer.name = name
    #     newCusomer.phone_code = phone_code
    #     newCusomer.save()
    #     username = request.POST.get('username')
    #     password_1 = request.POST.get('password_1')
    #     password_2 = request.POST.get('password_2')
    #     if password_1 != password_2:
    #         return render(request, 'create.html', {'message': 'Пароли не совпадают!'}, context=context)
    #     elif User.objects.filter(username=username).exists():
    #         return render(request, 'create.html', {'message': 'Логин уже используется'}, context=context)
    #     else:
    #         User.objects.create_user(
    #             username=username,
    #             password=password_1,
    #         )
    #         return redirect(products)

def messageSuccessBuy(request):
    return render(request, template_name='message.html');


def createOrder(request, id):
    order = Order.objects.all()
    product = get_object_or_404(Products, id=id)
    colors = ColorK.objects.all()
    codep = CodeP.objects.all()

    context = {
                "order": order,
                "product": product,
                "colors": colors,
                "codep": codep,
            }
    if request.method == "GET":
        return render(request, 'cart.html', context=context)
    elif request.method == 'POST':
        form = request.POST
        phoneNumber = form.get('phoneNumber')
        phoneCode = form.get('phoneCode')
        name = form.get('name')
        cityAddress = form.get('cityAddress')
        productChoosed = form.get('productChoosed')
        # quantity = form.get('quantity')
        colors = form.get('colors')
        colorsValue = form.get('colorsValue')
        cashMethod = form.get('cashMethod')
        bankCartMethod = form.get('bankCartMethod')
        mbank = form.get('mbank')
        newOrder = Order()
        newOrder.phoneCode = phoneCode
        newOrder.phoneNumber = phoneNumber
        newOrder.cityAddress = cityAddress
        newOrder.productChoosed = productChoosed
        newOrder.name = name
        # newOrder.quantity = quantity
        # newOrder.colors = colors
        newOrder.colorsValue = colorsValue
        newOrder.cashMethod = cashMethod
        newOrder.bankCartMethod = bankCartMethod
        newOrder.mbank = mbank
        newOrder.save()
        return redirect(messageSuccessBuy)
        