from django.urls import path
from . import views
from services.views import Servicios

urlpatterns = [
    path('', views.index, name="index"),
    path('servicios/', Servicios.as_view(), name="servicios"),
    path('contacto/', views.contacto, name="contacto"),
    path('cita/', views.cita, name="cita"),
    path('cita/<int:sucursal>/', views.estilistas),
    path('addCart/', views.add_cart, name="addCart"),
    path('deleteCart/', views.delete_cart, name="deleteCart")
]

