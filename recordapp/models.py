from django.db import models
from clientapp import models as client
from staffapp import models as staff
from serviceapp import models as service
# Create your models here.


class Record(models.Model):
    date = models.DateTimeField()
    id_client = models.ForeignKey(client.Client, on_delete=models.PROTECT)
    id_staff = models.ForeignKey(staff.Staff, on_delete=models.PROTECT)
    id_service = models.ForeignKey(service.Service, on_delete=models.PROTECT)
    price = models.FloatField()
    duration = models.IntegerField()
