from django.shortcuts import render
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
        form = forms.ClientForm()
        if request.method == 'POST':
            form = forms.ClientForm(request.POST)
            if form.is_valid():
                form.save()
        context = {'form': form}

        return render(request, 'client.html', context)