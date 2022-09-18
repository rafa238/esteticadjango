from django.shortcuts import render
from django.views.generic import ListView
from .models import Servicio
# Create your views here.

class Servicios(ListView):
    model = Servicio
    context_object_name = "servicios"
    template_name = "mainapp/servicios.html"

