# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Alumno
from .forms import AlumnoForm

def lista_alumnos(request):
    query = request.GET.get('q', '')  # Parámetro de búsqueda
    edad_filter = request.GET.get('edad', '')  # Parámetro de filtrado por edad

    # Obtener opciones únicas de edad para el filtro
    edades = Alumno.objects.values_list('edad', flat=True).distinct()

    # Aplicar filtrado por edad si se proporciona
    if edad_filter:
        alumnos = Alumno.objects.filter(edad=edad_filter)
    else:
        alumnos = Alumno.objects.all()

    # Aplicar búsqueda si se proporciona una consulta de búsqueda
    if query:
        alumnos = alumnos.filter(
            nombre__icontains=query
        ).distinct()

    context = {
        'alumnos': alumnos,
        'query': query,
        'edad_filter': edad_filter,
        'edades': edades,  # Opciones de edad para el filtro
    }
    return render(request, 'alumnos/lista_alumnos.html', context)

def crear_alumno(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'alumnos/form_alumno.html', {'form': form})

def actualizar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    if request.method == "POST":
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, 'alumnos/form_alumno.html', {'form': form})

def eliminar_alumno(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    if request.method == "POST":
        alumno.delete()
        return redirect('lista_alumnos')
    return render(request, 'alumnos/eliminar_alumno.html', {'alumno': alumno})

