from django.db import models

# Create your models here.

#########################################################################################
class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=200, blank=False)
    apellidos = models.CharField(max_length=200, blank=False)
    nacionalidad = models.CharField(max_length=200, blank=False)
    descripcion = models.TextField(blank=False, null=False)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now = True, auto_now_add = False)
    estado = models.BooleanField('Estado', default='True')

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']

#########################################################################################
def __str__(self):
    return self.nombre

#########################################################################################
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=255, blank=False, null=False)
    fecha_publicacion = models.DateField('Fecha de Publicacion', blank=False, null=False)
    #Referencia al id del autor
    autor_id = models.ManyToManyField(Autor)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now = True, auto_now_add = False)
    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['id']

    def __str__(self):
        return self.titulo
#########################################################################################
