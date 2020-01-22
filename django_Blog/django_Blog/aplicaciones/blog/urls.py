##############################################################################
from django.urls import path
from .views import index,matematicas,programacion,fisica,quimica,posteo
##############################################################################

##############################################################################
urlpatterns = [
    path('', index, name='index'),
    path('matematicas/', matematicas, name='matematicas'),
    path('programacion/', programacion, name='programacion'),
    path('fisica/', fisica, name='fisica'),
    path('quimica/', quimica, name='quimica'),
    path('<slug:slug>/', posteo, name='posteo'),
]
##############################################################################


#-----------------------------------------------------------------------------
#   REFERENCIAS:
#       https://wsvincent.com/django-slug-tutorial/
#
#
#-----------------------------------------------------------------------------