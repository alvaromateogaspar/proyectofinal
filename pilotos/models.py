from django.db import models


class Piloto(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=50)
    numero = models.IntegerField()
    escuderia = models.CharField(max_length=50)
    victorias = models.IntegerField()
    podios = models.IntegerField()
    puntos = models.IntegerField()
    imagen = models.ImageField(upload_to='pilotos')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'piloto'
        verbose_name_plural = 'pilotos'

    def __str__(self):
        return self.nombre
