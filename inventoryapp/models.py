from django.contrib.auth.models import User
from django.db import models
from decimal import Decimal


class Commodity(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    amount = models.IntegerField()

    class Meta:
        db_table = 'Commodity'

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    id_commodity = models.ForeignKey(Commodity, on_delete=models.PROTECT, related_name='commodity')
    id_employee = models.ForeignKey(User, on_delete=models.PROTECT, related_name='staff')
    amount = models.IntegerField()
    discount = models.IntegerField(null=True, default=None)

    class Meta:
        db_table = 'Order'

    def __str__(self):
        return f'{self.date}, {self.id_commodity}, {self.id_employee}, {self.amount}, {self.discount}'

    @property
    def total_price(self):
        if self.discount == None:
            return self.id_commodity.price
        else:
            return f'{self.id_commodity.price * Decimal(1 - self.discount/100):.2f}'