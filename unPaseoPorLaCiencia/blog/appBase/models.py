from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
# En las migraciones se crearan las tablas

#########################################################
class Contacto(models.Model):
    email = models.EmailField()
    fecha = models.CharField(max_length=10)
    asunto = models.CharField(max_length=200)
    mensaje = models.TextField()


    def __str__(self):
        return (self.email)
#########################################################

#########################################################
class Post(models.Model):
    titulo = models.CharField(max_length=200)
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
