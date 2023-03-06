from django.shortcuts import render, redirect
from card.models import Basket
from myshop.models import Product


def add_in_basket(request, id_product: int):
    basket, created = Basket.objects.get_or_create(user=request.user, product=Product.objects.get(pk=id_product))

    print(basket, created)

    if not created:
        basket.quantity += 1
        basket.save()

    return redirect('myshop:all-products')


def user_card(request):
    products = Basket.objects.filter(user=request.user)
    return render(request, 'card/card.html', {'products': products})
