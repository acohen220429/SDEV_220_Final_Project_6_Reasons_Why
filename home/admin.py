from django.contrib import admin
from .models import Appointment, Resource

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Resource)