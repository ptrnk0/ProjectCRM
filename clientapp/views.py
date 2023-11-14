from django.shortcuts import render
from django.template.loader import render_to_string
from clientapp import forms
from clientapp.models import Client
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# from django.views.generic import DeleteView

# Create your views here.
# def client_form_view(request, subClient):
#     if subClient == 'all_clients':
#         data = Client.objects.all()
#         context = {'form': data}
#         return render(request, 'clients_db.html', context)
#     elif subClient == 'insert_client':
#         form = forms.ClientForm(initial={'phone': '380 '})
#         if request.method == 'POST':
#             form = forms.ClientForm(request.POST, request.FILES)
#             if form.is_valid():
#                 form.save()
#             else:
#                 print('wrong date format')
#             rendered = render_to_string('client_submited.html')
#             return HttpResponse(rendered)
#         context = {'form': form}
#         return render(request, 'client_create.html', context)
#     else:
#         print(request.user.get_user_permissions())
#         return HttpResponse('nicht')

class ClientCreate(CreateView):
    model = Client
    form_class = forms.ClientForm
    initial = {'phone': '380 '}
    template_name = 'client_create.html'
    success_url = '/client/create/'


class ClientList(ListView):
    model = Client
    template_name = 'client_list.html'
    success_url = '/client/create/'
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


# def clientDelete(request):
#     try:
#         for i in request.POST.copy().pop('id'):
#             Client.objects.get(id=int(i)).delete()
#         rendered = render_to_string('client_deleted.html')
#         return HttpResponse(rendered)
#     except KeyError:
#         data = Client.objects.all()
#         context = {'form': data}
#         return render(request, 'clients_db.html', context)
