from django.shortcuts import render,get_object_or_404
from .models import Post, Categoria
from django.db.models import Q
def index(request):
    #Si hay algo en la barra de busqueda se guarda aca
    queryset = request.GET.get("buscar")
    post = Post.objects.filter(estado__exact = True)
    if queryset:
        post = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()
    return render(request,'index.html', {'post':post})

def posteo(request,slug):
    #post = Post.objects.get(slug=slug)
    post = get_object_or_404(Post,slug=slug)
    return render(request,'posts.html',{'post':post})

def matematicas(request):
    post = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact='Matematicas')
        )
    return render(request,'matematicas.html', {'post':post})

def programacion(request):
    post = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact='Programacion')
        )
    return render(request,'programacion.html', {'post':post})

def fisica(request):
    post = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact='Fisica')
        )
    return render(request,'fisica.html', {'post':post})

def quimica(request):
    post = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact='Quimica')
        )
    return render(request,'quimica.html', {'post':post})
