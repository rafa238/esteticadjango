from django.contrib.auth.models import AbstractUser
from django.db import models
from sucursal.models import Sucursal


# Create your models here.
class User(AbstractUser):
    tel = models.CharField(
        verbose_name="Télefono",
        max_length=50,
    )
    direction = models.CharField(
        verbose_name="Dirección",
        max_length=250,
    )

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return f"Usuario- {self.username}"


class Estilista(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuario")
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, verbose_name="Sucursal")
    entry_time = models.TimeField(verbose_name="Hora de entrada")
    departure_time = models.TimeField(verbose_name="Hora de salida")

    class Meta:
        verbose_name = "Estilista"
        verbose_name_plural = "Estilistas"
        permissions = [('es_estilista', 'Es estilista')]

    def __str__(self):
        return f"Estilista- {self.sucursal.name} {self.user.first_name} {self.user.last_name}"
