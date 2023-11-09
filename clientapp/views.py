from django.shortcuts import render
from django.template.loader import render_to_string
from clientapp import forms
from django.http import HttpResponse
from clientapp.models import Client

# Create your views here.
def client_form_view(request, subClient):
    if subClient == 'all_clients':
        data = Client.objects.all()
        context = {'form': data}
        return render(request, 'clients_db.html', context)
    elif subClient == 'insert_client':
        form = forms.ClientForm(initial={'phone': '+380'})
        if request.method == 'POST':
            form = forms.ClientForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                print('wrong date format')
            rendered = render_to_string('client_submited.html')
            return HttpResponse(rendered)
        context = {'form': form}
        
        return render(request, 'client_create.html', context)


def clientDelete(request):
    try:
        for i in request.POST.copy().pop('id'):
            Client.objects.get(id=int(i)).delete()
        rendered = render_to_string('client_deleted.html')
        return HttpResponse(rendered)
    except KeyError:
        data = Client.objects.all()
        context = {'form': data}
        return render(request, 'clients_db.html', context)