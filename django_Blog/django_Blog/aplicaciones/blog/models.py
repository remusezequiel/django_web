from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
##################################################################################################
class Categoria(models.Model):
    
    id = models.AutoField(primary_key = True)
    
    nombre = models.CharField(
        'Nombre de la Categoria',
        max_length=150, 
        blank=False, 
        null=False
    )

    estado = models.BooleanField(
        'Categoria Activada/Categoria desactivada',
        default=True
     )

    fecha_creacion = models.DateField(
        'Fecha de creacion',
        auto_now=False,
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre
##################################################################################################

##################################################################################################
class Autor(models.Model):
    
    id = models.AutoField(primary_key = True)
    
    nombre = models.CharField(
        'Nombre de Autor',
        max_length=255,
        blank=False, 
        null=False
    )
    
    apellidos = models.CharField(
        'Apellidos de Autor',
        max_length=255, 
        blank=False, 
        null=False
    )
    
    facebook = models.URLField(
        'Facebook',
        blank=True,
        null=True
    )
    
    twiter = models.URLField(
        'twiter', 
        blank=True, 
        null=True
    )
    
    instagram = models.URLField(
        'instagram', 
        blank=True,
        null=True
    )
    
    web = models.URLField(
        'web', 
        blank=True, 
        null=True
    )
    
    email = models.EmailField(
        'Correo Electronico', 
        blank=False,
        null=False
    )
    
    fecha_creacion = models.DateField(
        'Fecha de creacion',
        auto_now=False,
         auto_now_add=True
    )
    
    estado = models.BooleanField(
        'Autor Activo/Autor desactivado', 
        default=True
    )

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return "{0},{1}".format(self.apellidos, self.nombre)
##################################################################################################

##################################################################################################
class Post(models.Model):
    
    id = models.AutoField(primary_key = True)
    
    titulo = models.CharField(
        'Titulo post',
        max_length=255,
        blank=False, 
        null=False
    )
    
    #Por esto accedemos a cada una de las instancias del modelo post
    slug = models.CharField(
        'Slug', 
        max_length=100, 
        blank=False, 
        null=False
    )
    
    descripcion = models.CharField(
        'Titulo post',
        max_length=500, 
        blank=False, 
        null=False
    )
    
    #El contenido carca una clase de ckeditor 
    contenido = RichTextField()
    
    imagen = models.URLField(
        max_length=255, 
        blank=False, 
        null=False
    )
    
    #Recibira el id de un autor
    autor = models.ForeignKey(
        Autor, 
        on_delete=models.CASCADE
    )
    
    #Recibira el id de una categoria
    categoria = models.ForeignKey(
        Categoria, 
        on_delete = models.CASCADE
    )
    
    estado = models.BooleanField(
        'Publicado/No Publicado', 
        default=True
    )
    
    fecha_creacion = models.DateField(
        'Fecha de creacion',
        auto_now=False, 
        auto_now_add=True
    )
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo
##################################################################################################
