from django.shortcuts import render
from circuitos.models import Circuitos

def circuitos(request):
    circuitos = Circuitos.objects.all()
    return render(request, "circuitos/circuitos.html", {'circuitos': circuitos})


