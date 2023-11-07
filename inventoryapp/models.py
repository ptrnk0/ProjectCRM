from django.db import models
from staffapp import models as staff

# Create your models here.
class Commodity(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    amount = models.IntegerField()

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    date = models.DateTimeField()
    id_commodity = models.ForeignKey(Commodity, on_delete=models.PROTECT, related_name='commodity')
    id_employee = models.ForeignKey(staff.Staff, on_delete=models.PROTECT, related_name='staff')
    amount = models.IntegerField()
    discount = models.FloatField()

    def __str__(self):
        return f'{self.date}, {self.id_commodity}, {self.id_employee}, {self.amount}, {self.discount}'
