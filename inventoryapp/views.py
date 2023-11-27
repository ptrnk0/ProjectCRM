from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse
from inventoryapp.models import Commodity, Order
from inventoryapp import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
# def inventory_form_view(request, subDir):
#     if subDir == 'commodity':
#         form = forms.ComodityForm()
#         if request.method == 'POST':
#             form = forms.ComodityForm(request.POST)
#             if form.is_valid():
#                 form.save()
#             rendered = render_to_string('commodity_submited.html')
#             return HttpResponse(rendered)
#         context = {'form': form}
#         return render(request, 'commodity.html', context)
    
#     elif subDir == 'order':
#         form = forms.OrderForm()
#         if request.method == 'POST':
#             form = forms.OrderForm(request.POST)
#             if form.is_valid():
#                 form.save()
#             rendered = render_to_string('order_submited.html')
#             return HttpResponse(rendered)
#         context = {'form': form}
#         return render(request, 'order.html', context)
    
#     elif subDir == 'commodity_table':
#         data = models.Commodity.objects.all()
#         context = {'form': data}
#         return render(request, 'commodity_db.html', context)
    
#     elif subDir == 'order_table':
#         data = models.Order.objects.all().select_related()
#         context = {'form': data}
#         return render(request, 'order_db.html', context)


class CommodityCreate(CreateView):
    model = Commodity
    form_class = forms.ComodityForm
    template_name = 'commodity_create.html'
    success_url = '/commodity/create/'


class CommodityList(ListView):
    model = Commodity
    template_name = 'commodity_list.html'
    success_url = '/commodity/create/'
    ordering = '-id'
    paginate_by = 10


class CommodityDetail(DetailView):
    model = Commodity
    template_name = 'commodity_detail.html'


class CommodityUpdate(UpdateView):
    model = Commodity
    form_class = forms.ComodityForm
    success_url = '/commodity/list/'
    template_name = 'commodity_update_form.html'


class CommodityDelete(DeleteView):
    model = Commodity
    success_url = '/commodity/list/'
    template_name = 'commodity_confirm_delete.html'






class OrderCreate(CreateView):
    model = Order
    form_class = forms.OrderForm
    template_name = 'order_create.html'
    success_url = '/order/create/'


class OrderList(ListView):
    model = Order
    template_name = 'order_list.html'
    success_url = '/order/create/'
    paginate_by = 10


class OrderDetail(DetailView):
    model = Order
    template_name = 'order_detail.html'


class OrderUpdate(UpdateView):
    model = Order
    form_class = forms.OrderForm
    success_url = '/order/list/'
    template_name = 'order_update_form.html'


class OrderDelete(DeleteView):
    model = Order
    success_url = '/order/list/'
    template_name = 'order_confirm_delete.html'



def commodityDelete(request):
    try:
        for i in request.POST.copy().pop('id'):
            Commodity.objects.get(id=int(i)).delete()
        rendered = render_to_string('commodity_deleted.html')
        return HttpResponse(rendered)
    except KeyError:
        data = Commodity.objects.all()
        context = {'form': data}
        return render(request, 'commodity_db.html', context)
    

def orderDelete(request):
    try:
        for i in request.POST.copy().pop('id'):
            Order.objects.get(id=int(i)).delete()
        rendered = render_to_string('order_deleted.html')
        return HttpResponse(rendered)
    except KeyError:
        data = Order.objects.all()
        context = {'form': data}
        return render(request, 'order_db.html', context)