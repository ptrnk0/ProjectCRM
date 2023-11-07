from django.db import models

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=30, blank=True, default='')
    birthday = models.DateField(null=True, blank=True, default=None)
    comment = models.CharField(max_length=150, blank=True, default='')
    #image = models.FileField(upload_to=None, height_field=None, width_field=None, max_length=500)

    def __str__(self) -> str:
        return f'{self.first_name}, {self.last_name}, {self.phone}, {self.email}, {self.birthday}, {self.comment}'
