from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import *
from django.urls import reverse_lazy   
from django.http import HttpResponseRedirect 
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class MenuCreate(CreateView):
    model = Menu
    template_name = 'menu/menu_create.html'
    fields = ['name','description','attachment'] 
    success_url = reverse_lazy('restaurant:listar_menu')
    
    def form_valid(self, form):
        menu = form.save(commit=False)
        menu.user = self.request.user
        menu.save()
        
        return HttpResponseRedirect(self.success_url)

@method_decorator(login_required, name='dispatch')
class MenuList(ListView):
    model = Menu
    template_name = 'menu/menu_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        cardapios = Menu.objects.filter(user = self.request.user)

        if self.request.GET.get('search_box'):
            cardapios = cardapios.filter(name__icontains = self.request.GET['search_box'])

        context.update({
            'object_list': cardapios,
            })
        return context

@method_decorator(login_required, name='dispatch')
class MenuDetail(DetailView):
    model = Menu
    template_name = 'menu/menu_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # if self.object.attachment:
        #     url_cardapio = str(self.request.scheme)+'://'+str(self.request.META['HTTP_HOST'])+str(self.object.attachment.url)
        #     context.update({
        #         'url_cardapio': url_cardapio,
        #         })
        return context

@method_decorator(login_required, name='dispatch')
class MenuUpdate(UpdateView):
    model = Menu
    template_name = 'menu/menu_create.html'
    fields = ['name','description','attachment'] 

    def get_success_url(self):
          return reverse_lazy('restaurant:detalhar_menu', kwargs={'pk': self.kwargs['pk']})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        # removendo o arquivo antigo
        if self.object.attachment and self.request.FILES.get('attachment', False):
            self.object.attachment.delete()

        return super().post(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class MenuDelete(DeleteView):
    model = Menu
    success_url = reverse_lazy('restaurant:listar_menu')
    # tela de confirmação de remoção
    template_name = 'menu/menu_confirm_delete.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # removendo o arquivo antigo
        if self.object.attachment:
            self.object.attachment.delete()
        return super().post(request, *args, **kwargs)