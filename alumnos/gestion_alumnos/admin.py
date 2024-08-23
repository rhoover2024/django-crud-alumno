from django.contrib import admin
from .models import Alumno

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'edad', 'correo')  # Campos que se mostrarán en la lista
    search_fields = ('nombre', 'apellido', 'correo')  # Campos que se pueden buscar

admin.site.register(Alumno, AlumnoAdmin)
