from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

#Clase que maneja los posteos
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #Al pazarle timezone.now la fecha se creara automaticamente
    #en el momento en el cual se crea el posteo
    date_posted = models.DateTimeField(default=timezone.now)
    #Fijate que es una clave foranea la cual como parametro resive
    #al usuario el cual creara al posteo. Por lo que cuando creas al autor
    #en la base de datos primero tenes que tomar un autor en una variable
    #y pasarle esa vaiable al parametro de autor
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return ("%s,%s") %(self.title, self.author)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})    
