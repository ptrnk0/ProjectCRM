from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from inventoryapp import models
from inventoryapp import forms

# Create your views here.
def inventory_form_view(request, subDir):
    if subDir == 'commodity':
        form = forms.ComodityForm()
        if request.method == 'POST':
            form = forms.ComodityForm(request.POST)
            if form.is_valid():
                form.save()
            rendered = render_to_string('commodity_submited.html')
            return HttpResponse(rendered)
        context = {'form': form}
        return render(request, 'commodity.html', context)
    
    elif subDir == 'order':
        form = forms.OrderForm()
        if request.method == 'POST':
            form = forms.OrderForm(request.POST)
            if form.is_valid():
                form.save()
            rendered = render_to_string('order_submited.html')
            return HttpResponse(rendered)
        context = {'form': form}
        return render(request, 'order.html', context)
    
    elif subDir == 'commodity_table':
        data = models.Commodity.objects.all()
        context = {'form': data}
        return render(request, 'commodity_db.html', context)
    
    elif subDir == 'order_table':
        data = models.Order.objects.all()
        context = {'form': data}
        return render(request, 'order_db.html', context)


def commodityDelete(request):
    try:
        for i in request.POST.copy().pop('id'):
            models.Commodity.objects.get(id=int(i)).delete()
        rendered = render_to_string('commodity_deleted.html')
        return HttpResponse(rendered)
    except KeyError:
        data = models.Commodity.objects.all()
        context = {'form': data}
        return render(request, 'commodity_db.html', context)
    

def orderDelete(request):
    try:
        for i in request.POST.copy().pop('id'):
            models.Order.objects.get(id=int(i)).delete()
        rendered = render_to_string('order_deleted.html')
        return HttpResponse(rendered)
    except KeyError:
        data = models.Order.objects.all()
        context = {'form': data}
        return render(request, 'order_db.html', context)