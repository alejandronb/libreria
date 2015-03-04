# Create your views here.
from django.shortcuts import render
from libreria.models import libro
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib import auth
from django.http import HttpResponseRedirect, Http404, HttpResponse



def listar_libros(request):
	libros = libro.objects.all()
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