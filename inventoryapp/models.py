from django.db import models
from .staffapp import models as staff

# Create your models here.
class Commodity(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    amount = models.IntegerField()


class Order(models.Model):
    date = models.DateTimeField()
    id_commodity = models.ForeignKey(Commodity)
    id_employee = models.ForeignKey(staff.Staff)
    amount = models.IntegerField()
    discount = models.FloatField()

