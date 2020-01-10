from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
##############################################################################
class CategoriaResources(resources.ModelResource):
    class Meta:
        model = Categoria
##############################################################################

##############################################################################
class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre', 'estado', 'fecha_creacion']
    resource_class = CategoriaResources
##############################################################################

##############################################################################
class AutorResources(resources.ModelResource):
    class Meta:
        model = Autor
##############################################################################

##############################################################################
class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    #Barra de busqueda
    search_fields =['nombres', 'apellidos', 'estado', 'fecha_creacion']
    list_display = ('nombre','estado','fecha_creacion',)
    resource_class = AutorResources
##############################################################################

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post)
