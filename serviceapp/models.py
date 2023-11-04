from django.db import models
# Create your models here.


class Resource(models.Model):
    name = models.CharField(max_length=50)
    amount = models.IntegerField()


class Service(models.Model):
    name = models.CharField(max_length=50)
    id_resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
