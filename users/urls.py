from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.loguear, name="login"),
    path('logout/', views.logout_user, name="logout")
]
