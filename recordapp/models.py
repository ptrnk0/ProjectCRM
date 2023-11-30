import datetime
from django.contrib.auth.models import User
from django.db import models
from clientapp import models as client
from serviceapp import models as service


class Record(models.Model):
    date = models.DateField()
    time = models.TimeField()
    id_client = models.ForeignKey(client.Client, on_delete=models.PROTECT)
    id_staff = models.ForeignKey(User, on_delete=models.PROTECT)
    id_service = models.ForeignKey(service.Service, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.IntegerField(max_length=2)

    class Meta:
        db_table = 'Record'
        unique_together = ['date', 'time', 'id_staff', 'id_client']
        ordering = ['-date']
        constraints = [
            models.CheckConstraint(check=models.Q(date__gte=datetime.date.today()), name="date__gte_today"),
            models.CheckConstraint(check=models.Q(price__gt=0), name="price__gte_0"),
            models.CheckConstraint(check=models.Q(duration__gte=5), name='duration__gte_5')
        ]

    def __str__(self):
        return f'{self.date} {self.id_client.full_name}'
