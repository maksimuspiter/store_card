import json

from django.http import HttpResponse
from django.shortcuts import render
from .models import Category, Product


def index(request):
    products = Product.objects.all()
    return HttpResponse(products)
