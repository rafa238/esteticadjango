from django.db import models


# Create your models here.
class Servicio(models.Model):
    detalle = models.CharField(max_length=300, verbose_name="Descripción")
    duracion = models.IntegerField(default=0, verbose_name="Duracion en minutos")
    precio = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Precio")
    status = models.BooleanField(verbose_name="¿Activo?")

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.detalle
