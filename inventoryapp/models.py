from django.contrib.auth.models import User
from django.db import models
from staffapp import models as staff


class Commodity(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
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
    discount = models.FloatField(null=True, default=None)

    class Meta:
        db_table = 'Order'

    def __str__(self):
        return f'{self.date}, {self.id_commodity}, {self.id_employee}, {self.amount}, {self.discount}'
