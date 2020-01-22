###############################################################################
from django.shortcuts import render,get_object_or_404
#Importo los modelos que utilizo
from .models import Post, Categoria
from django.db.models import Q
###############################################################################

#------------------------------------------------------------------------------
#   Nota: 
#       Investigar vistas basadas en clases para reduccion
#       de codigo.
#------------------------------------------------------------------------------

###############################################################################
def index(request):
    """
    Vista correspondiente al index de la pagina.  
    Sobre este se define la barra de busqueda
    el cual filtra segun el titulo del post y datos
    de la descripcion
    """ 
    #Si hay algo en la barra de busqueda se guarda aca
    queryset = request.GET.get("buscar")
    post = Post.objects.filter(estado__exact = True)
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()
    return render(request,'index.html', {'post':post})
###############################################################################

###############################################################################
def posteo(request,slug):
    """
    Vista correspondiente a la seccion de posteos
    Sobre el contexto se utiliza get_object_or_404
    el cual recive el modelo Post y el slug del post
    como parametros. Si el slug no existe devuelve
    un error 404
    """
    #post = Post.objects.get(slug=slug)
    post = get_object_or_404(Post,slug=slug)
    return render(request,'posts.html',{'post':post})
###############################################################################

###############################################################################
def matematicas(request):
    """
     Vista correspondiente al template dedicado a la seccion matematicas
     en el cual estaran alojadas todos los posteos correspondientes a
     dicha categoria siempre y cuando su estado sea verdadero. 
    """
    post = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact='Matematicas')
        )
    return render(request,'matematicas.html', {'post':post})
###############################################################################

###############################################################################
def programacion(request):
    """
    """
    post = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact='Programacion')
        )
    return render(request,'programacion.html', {'post':post})
###############################################################################

###############################################################################
def fisica(request):
    """
    """
    post = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact='Fisica')
        )
    return render(request,'fisica.html', {'post':post})
###############################################################################

###############################################################################
def quimica(request):
    """
    """
    post = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact='Quimica')
        )
    return render(request,'quimica.html', {'post':post})
###############################################################################