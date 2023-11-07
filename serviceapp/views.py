from django.shortcuts import render
from django.shortcuts import render
from django.template.loader import render_to_string
from serviceapp import forms
from django.http import HttpResponse
from serviceapp.models import Resource, Service

# Create your views here.
def service_form_view(request, subDir):
    if subDir == 'service1':
        form = forms.ServiceForm()
        if request.method == 'POST':
            form = forms.ServiceForm(request.POST)
            if form.is_valid():
                form.save()
            rendered = render_to_string('service_submited.html')
            return HttpResponse(rendered)
        context = {'form': form}
        return render(request, 'service.html', context)
    
    elif subDir == 'resource':
        form = forms.ResourceForm()
        if request.method == 'POST':
            form = forms.ResourceForm(request.POST)
            if form.is_valid():
                form.save()
            rendered = render_to_string('resource_submited.html')
            return HttpResponse(rendered)
        context = {'form': form}
        return render(request, 'resource.html', context)
    
    elif subDir == 'service_table':
        data = Service.objects.all()
        context = {'form': data}
        return render(request, 'service_db.html', context)
    
    elif subDir == 'resource_table':
        data = Resource.objects.all()
        context = {'form': data}
        return render(request, 'resource_db.html', context)


def serviceDelete(request):
    try:
        for i in request.POST.copy().pop('id'):
            Service.objects.get(id=int(i)).delete()
        rendered = render_to_string('service_deleted.html')
        return HttpResponse(rendered)
    except KeyError:
        data = Service.objects.all()
        context = {'form': data}
        return render(request, 'service_db.html', context)
    

def resourceDelete(request):
    try:
        for i in request.POST.copy().pop('id'):
            Resource.objects.get(id=int(i)).delete()
        rendered = render_to_string('resource_deleted.html')
        return HttpResponse(rendered)
    except KeyError:
        data = Resource.objects.all()
        context = {'form': data}
        return render(request, 'resource_db.html', context)