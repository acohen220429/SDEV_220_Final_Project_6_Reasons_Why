from django.shortcuts import render, redirect

from .forms import AppointmentForm
from .models import Appointment

def index(request):
    return render(request, "home/index.html")

def appointments_list(request):
    appointments = Appointment.objects.all().order_by('date', 'time')
    context = {
        "appointments": appointments
    }
    return render(request, "home/appointments_list.html", context)

def appointment_detail(request, pk):
    appointment = Appointment.objects.get(pk=pk)
    context = {
        "appointment": appointment
    }
    return render(request, "home/appointment_detail.html", context)

def appointment_create(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            return redirect('appointment_detail', pk=appointment.pk)
    else:
        form = AppointmentForm()
    
    context = {
        "form": form
    }
    return render(request, "home/appointment_form.html", context)