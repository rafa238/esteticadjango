from django.contrib import admin
from .models import Reservacion, Pago, DetalleReservacion


class ServiciosInline(admin.TabularInline):
    model = Reservacion.servicios.through


class ReservacionAdmin(admin.ModelAdmin):
    inlines = [
        ServiciosInline,
    ]


# Register your models here.
admin.site.register(Reservacion, ReservacionAdmin)
admin.site.register(Pago)
# admin.site.register(DetalleReservacion)
