from django.urls import path
from myshop import views

app_name = 'myshop'

urlpatterns = [
    path('', views.index, name='all-products'),
]
