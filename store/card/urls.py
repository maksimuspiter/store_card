from django.urls import path
from card import views

app_name = 'card'

urlpatterns = [
    path('', views.user_card, name='user-card'),
    path('add/<int:id_product>', views.add_in_basket, name='add-in-basket'),
]
