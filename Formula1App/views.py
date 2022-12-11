from django.shortcuts import render, HttpResponse

from pilotos.models import Piloto


def home(request):
    return render(request, "Formula1App/home.html")

def escuderias(request):
    return render(request, "Formula1App/escuderias.html")

