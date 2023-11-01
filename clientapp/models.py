from django.db import models

# Create your models here.


class Client(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=30, null=True, default=None)
    birthday = models.DateField(null=True, default=None)
    sex = models.CharField(max_length=15, default=None)
    comment = models.CharField(max_length=150, null=True, default=None)
    # image = models.FileField(upload_to=None, height_field=None, width_field=None, max_length=500)
