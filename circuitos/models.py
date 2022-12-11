from django.db import models


class Circuitos(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='circuitos')
    vuelta_rapida = models.CharField(max_length=50)
    longitud = models.CharField(max_length=50)
    numero_de_vueltas = models.CharField(max_length=50)
    fecha_de_apertura = models.CharField(max_length=50)
    numero_de_curvas = models.CharField(max_length=50)



    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Circuito'
        verbose_name_plural = 'Circuitos'



