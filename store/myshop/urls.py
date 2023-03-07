from django.urls import path
from myshop import views

app_name = 'myshop'

urlpatterns = [
    path('', views.index, name='all-products'),
    path('fast', views.index_fast, name='all-products-f'),
]
