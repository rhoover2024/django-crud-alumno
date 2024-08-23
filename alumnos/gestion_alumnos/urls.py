# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alumnos, name='lista_alumnos'),
    path('nuevo/', views.crear_alumno, name='crear_alumno'),
    path('editar/<int:id>/', views.actualizar_alumno, name='actualizar_alumno'),
    path('eliminar/<int:id>/', views.eliminar_alumno, name='eliminar_alumno'),
]
