from django.shortcuts import render

from pilotos.models import Piloto

def pilotos(request):
    pilotos = Piloto.objects.all()
    return render(request, "pilotos/pilotos.html", {'pilotos': pilotos})
