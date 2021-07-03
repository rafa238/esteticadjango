from django.contrib import admin
from .models import User, Estilista

# Register your models here.
class AdminPage(admin.ModelAdmin):
    search_fields = ("username", "id")
    readonly_fields = ["last_login", "date_joined"]

admin.site.register(User, AdminPage)
admin.site.register(Estilista)