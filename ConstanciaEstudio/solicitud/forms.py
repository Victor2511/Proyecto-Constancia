from django import forms
from .models import DataForm
"""Aqui se crea un formulario con los campos requeridos que esta vinculado al modelo de base de datos"""
class SolicitudForm(forms.ModelForm):
    class Meta:
        model = DataForm
        #fields = '__all__' #Para mostrar todos los campos
        fields = ['nombres', 'apellidos', 'edad', 'pnf', 'seccion', 'semestre', 'cedula']