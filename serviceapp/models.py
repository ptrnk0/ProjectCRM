from django.db import models
# Create your models here.


class Resource(models.Model):
    name = models.CharField(max_length=50)
    amount = models.IntegerField()

    def __str__(self):
        return f'{self.name}'


class Service(models.Model):
    name = models.CharField(max_length=50)
    id_resource = models.ForeignKey(Resource, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.id_resource}'
