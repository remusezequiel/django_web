from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from ckeditor.widgets import CKEditorwidget


#https://github.com/django-ckeditor/django-ckeditor
#content = forms.CharField(widget=CKEditorWidget())
