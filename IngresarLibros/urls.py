from django.urls import path
from . import views

urlpatterns = [
    path('', views.crud_libros, name="crud_libros"),  # Página de CRUD
]
