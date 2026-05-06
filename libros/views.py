from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, Categoria


# -----------------------------
# LIBROS CRUD
# -----------------------------

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/lista.html', {'libros': libros})


def crear_libro(request):
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        anio = request.POST.get('anio')
        portada = request.FILES.get('portada')
        categoria_id = request.POST.get('categoria')

        if not categoria_id:
            return render(request, 'libros/crear.html', {
                'categorias': categorias,
                'error': 'Selecciona una categoría'
            })

        Libro.objects.create(
            titulo=titulo,
            autor=autor,
            anio=anio,
            portada=portada,
            categoria_id=categoria_id
        )

        return redirect('lista')

    return render(request, 'libros/crear.html', {'categorias': categorias})


def editar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        libro.titulo = request.POST.get('titulo')
        libro.autor = request.POST.get('autor')
        libro.anio = request.POST.get('anio')

        if request.FILES.get('portada'):
            libro.portada = request.FILES.get('portada')

        libro.categoria_id = request.POST.get('categoria')
        libro.save()

        return redirect('lista')

    return render(request, 'libros/editar.html', {
        'libro': libro,
        'categorias': categorias
    })


def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    libro.delete()
    return redirect('lista')


# -----------------------------
# CATEGORIAS CRUD
# -----------------------------

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/lista.html', {'categorias': categorias})


def crear_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        imagen = request.FILES.get('imagen')

        Categoria.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            imagen=imagen
        )

        return redirect('lista_categorias')

    return render(request, 'categorias/crear.html')


def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == 'POST':
        categoria.nombre = request.POST.get('nombre')
        categoria.descripcion = request.POST.get('descripcion')

        if request.FILES.get('imagen'):
            categoria.imagen = request.FILES.get('imagen')

        categoria.save()

        return redirect('lista_categorias')

    return render(request, 'categorias/editar.html', {'categoria': categoria})


def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    return redirect('lista_categorias')