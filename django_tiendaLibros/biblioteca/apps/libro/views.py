from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import AutorForm
from .models import Autor
#from .urls import path



# Create your views here.
################################################################################
def home(request):
    return render(request, 'index.html',{'nombre':'Tienda de Libros'})
################################################################################

################################################################################
def crearAutor(request):
    #Valido
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('index')
    else:
        autor_form = AutorForm()
    return render(request, 'libro/crear_autor.html', {'autor_form':autor_form})
################################################################################

################################################################################
def listarAutor(request):
    autores = Autor.objects.filter(estado=True)
    return render(request,
                  'libro/listar_autor.html',
                  {'autores':autores})
################################################################################

################################################################################
def editarAutor(request, id):
    autor_form = None
    error = None
    try:
        autor = Autor.objects.get(id=id)
        if request.method == 'GET':
            autor_form = AutorForm(instance=autor)
        else:
            autor_form = AutorForm(request.POST, instance=autor)
            if autor_form.is_valid():
                #nom = autor_forms.cleaned_dat['nombre']
                #print(nom)
                autor_form.save()
                return redirect('index')
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'libro/crear_autor.html',
                  {'autor_form':autor_form, 'error':error})
################################################################################

################################################################################
def eliminarAutor(request, id):
    autor = Autor.objects.get(id=id)
    if request.method == 'POST':
        #autor.delete()
        autor.estado = False
        return redirect('libro:listar_autor')
    return render(request,'libro/eliminar_autor.html', {'autor':autor})
################################################################################
