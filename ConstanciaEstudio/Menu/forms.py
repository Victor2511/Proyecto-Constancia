from django import forms
from django.core import validators
# Importamos las clases de formulario de Django para crear un usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Creamos una clase que se vincula con el formulario por defecto de creacion de usuario
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']