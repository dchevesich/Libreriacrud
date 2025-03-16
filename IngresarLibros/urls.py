from django.urls import path
from . import views

urlpatterns = [
    path('', views.AgregandoLibro, name="agregar_libros"),
    path('libros/', views.mostrarLibros,),
]
