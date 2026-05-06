from django.urls import path
from . import views

urlpatterns = [
    # LIBROS
    path('', views.lista_libros, name='lista'),
    path('crear/', views.crear_libro, name='crear'),
    path('editar/<int:id>/', views.editar_libro, name='editar'),
    path('eliminar/<int:id>/', views.eliminar_libro, name='eliminar'),

    # CATEGORIAS
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/crear/', views.crear_categoria, name='crear_categoria'),
    path('categorias/editar/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:id>/', views.eliminar_categoria, name='eliminar_categoria'),
]