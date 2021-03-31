from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['email', 'password1','password2', 'nome_completo', 'cpf', 'telefone']