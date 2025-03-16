from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
# Create your views here.


def AgregandoLibro(request):

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')

        if titulo and autor:
            libro = Libro.objects.create(
                titulo=titulo,
                autor=autor
            )
            return redirect('libros/')
    return render(request, 'base.html')


def mostrarLibros(request):
    libros = Libro.objects.all()  # se obtienen todos los libros
    return render(request, 'mostrar_libros.html', {"libros": libros})


def borrando(request):
    if request.method == "POST":
        # Obtener el ID ingresado en el formulario
        libro_id = request.POST.get("libro_id")
        try:
            # Buscar el libro en la base de datos
            libro = Libro.objects.get(id=libro_id)
            libro.delete()  # Eliminar el libro
        except Libro.DoesNotExist:
            pass  # Si el libro no existe, no hacer nada

        # Redirigir a la lista de libros
        return redirect("libros/")
    return render(request, "libros/")  # Mostrar el formulario
