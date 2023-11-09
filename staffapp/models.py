from django.db import models
# Create your models here.


class Staff(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    sex = models.CharField(max_length=15)
    email = models.CharField(max_length=30, null=True, default=None)
    phone = models.CharField(max_length=15)
    job_title = models.CharField(max_length=15)
    access_level = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Schedule(models.Model):
    date = models.DateField()
    id_staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
