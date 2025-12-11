from django.shortcuts import render, redirect, get_object_or_404
from .forms import AppointmentForm
from .models import Appointment, Resource
import json
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "home/index.html")

@login_required
def appointments_list(request):
    appointments = Appointment.objects.all().order_by('date', 'time')
    context = {
        "appointments": appointments
    }
    return render(request, "home/appointments_list.html", context)

@login_required
def appointment_detail(request, pk):
    appointment = Appointment.objects.get(pk=pk)
    context = {
        "appointment": appointment
    }
    return render(request, "home/appointment_detail.html", context)

@login_required
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

@login_required
def appointment_edit(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            appointment = form.save()
            return redirect('appointment_detail', pk=appointment.pk)
    else:
        form = AppointmentForm(instance=appointment)
    
    context = {
        "form": form
    }
    return render(request, "home/appointment_form.html", context)

@login_required
def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == "POST":
        appointment.delete()
    return redirect("appointments_list")


def resources_map(request):
    resources = Resource.objects.all()
    resources_data = []
    for r in resources:
        resources_data.append({
            'name': r.name,
            'address': r.address,
            'phone': r.phone,
            'lat': r.latitude,
            'lng': r.longitude,
        })

    context = {
        'resources_json': mark_safe(json.dumps(resources_data))
    }
    return render(request, "home/resources_map.html", context)
