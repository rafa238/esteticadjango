from django.db import models
from users.models import User
from users.models import Estilista
from services.models import Servicio

# Create your models here.
class Reservacion(models.Model):
    user = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name="Dia de cita")
    hora_inicio = models.TimeField(verbose_name="Inicio")
    hora_fin = models.TimeField(verbose_name="Fin")
    total = models.DecimalField(decimal_places=2, max_digits=6, verbose_name="Total")
    servicios = models.ManyToManyField(Servicio, through='DetalleReservacion')
    class Meta:
        verbose_name = "Reservacion"
        verbose_name_plural = "Reservaciones"

    def __str__(self):
        return f"{self.user.first_name}-{self.fecha}"

class Pago(models.Model):
    reserva = models.ForeignKey(Reservacion, on_delete=models.CASCADE, verbose_name="Reservacion")
    pago = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Pago")
    fecha_captura = models.DateTimeField(auto_now_add=True, verbose_name="Fecha del pago")

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
    
    def __str__(self):
        return f"{self.reserva.user.first_name}-{self.fecha_captura}"

class DetalleReservacion(models.Model):
    estilista = models.ForeignKey(Estilista, on_delete=models.CASCADE, verbose_name="Estilista")
    reservacion = models.ForeignKey(Reservacion, on_delete=models.CASCADE, verbose_name="Reservación")
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, verbose_name="Servicio")
    hora_inicios = models.TimeField(verbose_name="Inicio del servicio")
    hora_fins = models.TimeField(verbose_name="Fin del servicio")
    orden_servicio = models.IntegerField(verbose_name="Orden de servicio", default=1)

    class Meta:
        verbose_name = "Servicio de la reservación"
        verbose_name_plural = "Servicios de la reservación"

    def __str__(self):
        return f"Servicio {self.servicio.detalle}"