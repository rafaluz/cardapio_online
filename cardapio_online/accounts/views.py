from django.shortcuts import render
from .models import *    
from .forms import *    
from django.urls import reverse_lazy    
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView, FormMixin   


class UsuarioCreate(CreateView):
    model = Usuario
    template_name = 'usuario/add.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('accounts:login')