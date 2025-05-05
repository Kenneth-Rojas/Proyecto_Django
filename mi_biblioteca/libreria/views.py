from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Libro
from .forms import LibroForm

# Create your views here.

# Vista para crear un libro
@login_required
def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save(commit=False)
            libro.usuario = request.user  # Asignar el libro al usuario actual
            libro.save()
            return redirect('libreria:lista_libros')  # Redirige a la lista de libros
    else:
        form = LibroForm()
    return render(request, 'libreria/crear_libro.html', {'form': form})

# Vista para ver la lista de libros del usuario
@login_required
def lista_libros(request):
    libros = Libro.objects.filter(usuario=request.user)
    return render(request, 'libreria/lista_libros.html', {'libros': libros})

# Vista para ver los detalles de un libro
@login_required
def detalle_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk, usuario=request.user)
    return render(request, 'libreria/detalle_libro.html', {'libro': libro})

# Vista para editar un libro
@login_required
def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('libreria:detalle_libro', pk=libro.pk)
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libreria/editar_libro.html', {'form': form, 'libro': libro})

# Vista para eliminar un libro
@login_required
def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk, usuario=request.user)
    if request.method == 'POST':
        libro.delete()
        return redirect('libreria:lista_libros')
    return render(request, 'libreria/eliminar_libro.html', {'libro': libro})
