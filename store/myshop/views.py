import json
from django.db.models import Sum, F, Count
from django.http import HttpResponse
from django.shortcuts import render
from myshop.models import Category, Product
from card.models import Basket


def index(request):
    products = Product.objects.all()
    user_products = Basket.objects.filter(user=request.user)
    # total_cost = not Basket.objects.filter(user=request.user). \
    #     annotate(price_item=Sum(F('product__price')*F('quantity'))).aggregate(Sum('price_item'))
    # total_cost = Basket.objects.filter(user=request.user).\
    #     aggregate('product__price')
    # print(total_cost)

    total_cont = Basket.objects.filter(user=request.user).aggregate(Sum('quantity'))
    print(total_cont)
    return render(request, 'index.html', {'products': products,
                                          'user_products': user_products,
                                          'total_cont': total_cont['quantity__sum']})
