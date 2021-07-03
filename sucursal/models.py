from django.db import models

# Create your models here.
class Sucursal(models.Model):
    name = models.CharField(max_length=100, verbose_name="Sucursal")
    direction = models.CharField(max_length=200, verbose_name="Dirección")
    status = models.BooleanField(verbose_name="¿Activo?")
    
    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"
    
    def __str__(self):
        return self.name