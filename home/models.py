from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Appointment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    doctor = models.CharField(max_length=20)
    clinic = models.CharField(max_length=30)
    description = models.TextField(max_length=100)

    def __str__(self):
        details =  (f"Appointment details:\n"
                    f"Doctor: {self.doctor}\n"
                    f"Location: {self.clinic}\n"
                    f"Date: {self.date.strftime('%m/%d/%Y')}\n"
                    f"Time: {self.time.strftime('%I:%M %p')}\n")
        
        # return description if there is one
        if self.description:
                    details +=f"Description: {self.description}\n"

        return details
    