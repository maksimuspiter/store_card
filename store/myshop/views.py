import json
from django.db.models import Sum, F, Count
from django.http import HttpResponse
from django.shortcuts import render
from myshop.models import Category, Product
from card.models import Basket


def index(request):
    products = Product.objects.all()
    user_products = Basket.objects.filter(user=request.user)

    total_cost = user_products. \
        annotate(price_item=Sum(F('product__price') * F('quantity'))).aggregate(Sum('price_item'))['price_item__sum']
    # total_cost = Basket.objects.filter(user=request.user).\
    #     aggregate('product__price')
    # print(total_cost)

    total_cont = Basket.objects.filter(user=request.user).aggregate(Sum('quantity'))
    # print(total_cont)
    return render(request, 'index.html', {'products': products,
                                          'user_products': user_products,
                                          'total_cont': total_cont['quantity__sum'],
                                          'total_cost': '%.2f' % total_cost})


def index_fast(request):
    products = Product.objects.all().only('name', 'price', 'description')

    user_products = Basket.objects.filter(user=request.user).select_related('product'). \
        only('user', 'product', 'quantity')

    total_cost = user_products. \
        annotate(price_item=Sum(F('product__price') * F('quantity'))).aggregate(Sum('price_item'))['price_item__sum']

    total_cont = user_products.aggregate(Sum('quantity'))

    return render(request, 'index.html', {'products': products,
                                          'user_products': user_products,
                                          'total_cont': total_cont['quantity__sum'],
                                          'total_cost': '%.2f' % total_cost})


def raw(request):
    from django.db.models.expressions import RawSQL
    from django.db import connection

    # queryset.annotate(val=RawSQL("select col from sometable where othercol = %s", (param,)))

    with connection.cursor() as cursor:
        query = """
           SELECT name, description, price
           FROM myshop_product;
           """
        cursor.execute(query)
        row = cursor.fetchall() # this is tuple

    return render(request, 'raw.html', {'row': row})
