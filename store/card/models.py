from django.contrib.auth.models import User
from django.db import models
from myshop.models import Product


class Basket(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='basket')

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(verbose_name='количество', default=1)

    def basket_item_cost(self):
        return self.product.price * self.quantity
