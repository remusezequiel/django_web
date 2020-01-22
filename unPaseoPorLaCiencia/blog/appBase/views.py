from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
#Del modelo de esta carpeta importo la clase Contacto y Post
from .models import Contacto, Post

# Create your views here.

##############################################################################################
def index(request):
	contenido = {
	              'nombre_sitio': 'Un Paseo Por La Ciencia',
	              'posteo': Post.objects.all()[:3],
				 }
	return render(request, 'appBase/index.html', contenido)
##############################################################################################


##############################################################################################
def noticias(request):
    context = {
    'posts': Post.objects.all(),
	}
    return render(request, 'appBase/noticias.html',context)
##############################################################################################


##############################################################################################
def contacto(request):
    contenido = { 'nombre_sitio': 'Un Paseo Por La Ciencia' }
    if request.method == 'POST':
        #El parametro del get es el nombre del input del formulario
        email_r = request.POST.get('email')
        fecha_r = request.POST.get('fecha')
        asunto_r = request.POST.get('asunto')
        mensaje_r = request.POST.get('mensaje')
        #Este es el modelo
        c = Contacto(email=email_r,fecha=fecha_r, asunto=asunto_r, mensaje=mensaje_r)
        c.save()

        return render(request, 'appBase/index.html', {'contenido':contenido})
    else :
        return render(request, 'appBase/contacto.html', {'contenido':contenido})
##############################################################################################
