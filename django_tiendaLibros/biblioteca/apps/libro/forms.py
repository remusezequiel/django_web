from django import forms
from .models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        #REferencia a los campos que an a ser rellenados
        fields = ['nombre', 'apellidos', 'nacionalidad', 'descripcion']
