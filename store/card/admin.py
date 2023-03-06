from django.contrib import admin
from card.models import Basket


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity']
