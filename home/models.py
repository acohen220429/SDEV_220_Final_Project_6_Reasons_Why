from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Appointment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    dr = models.CharField(max_length=20)
    clinic = models.CharField(max_length=30)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.title
    