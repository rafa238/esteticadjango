from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('servicios/', views.servicios, name="servicios"),
    path('contacto/', views.contacto, name="contacto"),
    path('cita/', views.cita, name="cita"),
    path('cita/<int:sucursal>/', views.estilistas),
    path('addCart/', views.add_cart, name="addCart"),
    path('deleteCart/', views.delete_cart, name="deleteCart")
]

