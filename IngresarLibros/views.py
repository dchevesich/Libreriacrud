from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro


def crud_libros(request):
    # Procesar solicitud POST para agregar un libro
    if request.method == "POST" and "agregar_libro" in request.POST:
        titulo = request.POST.get("titulo")
        autor = request.POST.get("autor")
        if titulo and autor:
            Libro.objects.create(titulo=titulo, autor=autor)
        return redirect("crud_libros")  # Recargar la página después de agregar

    # Procesar solicitud POST para actualizar un libro
    if request.method == "POST" and "actualizar_libro" in request.POST:
        libro_id = request.POST.get("libro_id")
        titulo = request.POST.get("titulo")
        autor = request.POST.get("autor")
        if libro_id and titulo and autor:
            libro = get_object_or_404(Libro, id=libro_id)
            libro.titulo = titulo
            libro.autor = autor
            libro.save()
        # Recargar la página después de actualizar
        return redirect("crud_libros")

    # Procesar solicitud POST para borrar un libro
    if request.method == "POST" and "borrar_libro" in request.POST:
        libro_id = request.POST.get("libro_id")
        try:
            libro = Libro.objects.get(id=libro_id)
            libro.delete()
        except Libro.DoesNotExist:
            pass  # Manejar el error si el libro no existe
        return redirect("crud_libros")  # Recargar la página después de borrar

    # Obtener todos los libros para mostrar en la página
    libros = Libro.objects.all()
    return render(request, 'crud_libros.html', {"libros": libros})
