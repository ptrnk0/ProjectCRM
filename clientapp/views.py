from typing import Any
from django.shortcuts import render
from django.template.loader import render_to_string
from clientapp import forms
from clientapp.models import Client
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse


class ClientCreate(CreateView):
    model = Client
    form_class = forms.ClientForm
    template_name = 'client_create.html'
    success_url = '/client/create/'

    def post(self, request, *args, **kwargs):
        super().post(request=request, args=args, kwargs=kwargs)
        return JsonResponse({
            'message': 'success'
        })
    

class ClientList(ListView):
    model = Client
    template_name = 'client_list.html'
    success_url = '/client/create/'
    context_object_name = 'client_list'
    paginate_by = 10


class ClientDetail(DetailView):
    model = Client
    template_name = 'client_detail.html'


class ClientUpdate(UpdateView):
    model = Client
    form_class = forms.ClientForm
    success_url = '/client/list/'
    template_name = 'client_update_form.html'


class ClientDelete(DeleteView):
    model = Client
    success_url = '/client/list/'
    template_name = 'client_confirm_delete.html'