from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
# En las migraciones se crearan las tablas

#########################################################
class Contacto(models.Model):
    email = models.EmailField('Correo Electronico', blank=False, null=False)
    fecha = models.CharField('Fecha',max_length=10,blank=False, null=False)
    asunto = models.CharField(max_length=200,blank=False, null=False)
    mensaje = models.TextField()


    def __str__(self):
        return (self.email)
#########################################################

##################################################################################################
class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de la Categoria',max_length=150, blank=False, null=False)
    estado = models.BooleanField('Categoria Activada/Categoria desactivada', default=True)
    fecha_creacion = models.DateField('Fecha de creacion',auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre
##################################################################################################


#########################################################
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    #El slug nos sirve como identificador de las noticias
    slug = models.CharField('Slug', max_length=100, blank=False, null=False)
    asignatura = models.CharField(max_length=100)
    tema = models.CharField(max_length=200)
    encabezado = RichTextField(null=True)
    contenido = RichTextUploadingField()
    #Al pazarle timezone.now la fecha se creara automaticamente
    #en el momento en el cual se crea el posteo
    fecha_posteo = models.DateTimeField(default=timezone.now)
    #Fijate que es una clave foranea la cual como parametro resive
    #al usuario el cual creara al posteo. Por lo que cuando creas al autor
    #en la base de datos primero tenes que tomar un autor en una variable
    #y pasarle esa vaiable al parametro de autor
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return ("%s,%s") %(self.titulo, self.autor)
#########################################################
