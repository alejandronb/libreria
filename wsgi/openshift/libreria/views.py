# Create your views here.
from django.shortcuts import render,render_to_response
from libreria import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib import auth
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib.auth.models import User


def listar_libros(request):
	libros = models.libro.objects.all()
	return render(request, 'listar_libros.html', { 'libros': libros })
    #return render(request, 'listar_libros.html', {})

def registro(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect('/')
	else:
		form = UserCreationForm()
		return render(request, "registro.html", {
		'form': form,})


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth.login(request,user)
            request.session['username'] = username
            return HttpResponseRedirect('/listado')
        else:
            return HttpResponse('<p>Usuario invalido</p>')
    else:
        return HttpResponse('<p>Login Incorrecto.<a href="/">Intentar de nuevo </a></p>')


def login2(request):
#     if request.session.get("username"):
# #        return render_to_response('1.html', {'data_raw': resp },)
#         resp = movies_popular()
#         return render(request, '1.html', {'data_raw': resp },)
#    else:
	return render(request, 'login.html', {})


def marcar(request,id_libro):
    username = request.session.get("username")
    user = User.objects.get(username=username)
    libro = models.libro.objects.get(id=id_libro)
    if len(models.userlibro.objects.filter(usuario=user,libro=libro,leido=1)) == 0:
        insert_user = models.userlibro(usuario=user,libro=libro,leido=1)
        insert_user.save()
        return HttpResponse('<p>Libro insertado en leidos</p><a href="/leidos"><p>Ir a la lista de leidos</p></a><a href="/listado"><p>Volver al listado</p></a>')
    else:
        return HttpResponse('<p>Ya esta insertado</p><a href="/leidos"><p>Ir a la lista de leidos</p></a><a href="/listado"><p>Volver al listado</p></a>')


def leidos(request):
    username = request.session.get("username")
    user = User.objects.get(username=username)
    userlibros_leidos = models.userlibro.objects.filter(usuario=user,leido=1).values('libro')
    respuesta = models.libro.objects.filter(id__in=userlibros_leidos)
    return render_to_response('leidos.html', {'libros':respuesta},)

def mostrar_detalle(request,id_libro):
    libro_concreto = models.libro.objects.get(id=id_libro)
    return render_to_response('detalles.html', {'info_libro':libro_concreto},)
