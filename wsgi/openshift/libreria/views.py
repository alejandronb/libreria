# Create your views here.
from django.shortcuts import render
from .models import libro


def listar_libros(request):
	libros = libro.objects.all()
	return render(request, 'listar_libros.html', { 'libros': libros })