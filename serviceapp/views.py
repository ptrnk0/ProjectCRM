# from django.template.loader import render_to_string
# from serviceapp import forms
# from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from serviceapp.forms import ServiceForm, ResourceForm, AddResourceForServiceForm
from serviceapp.models import Resource, Service


class ListResourceView(ListView):
    model = Resource
    field = '__all__'
    context_object_name = 'list_resource'
    paginate_by = 10
    template_name = 'serviceapp/resource_list.html'


class DetailResourceView(DetailView):
    model = Resource
    template_name = 'serviceapp/resource_detail.html'
    context_object_name = 'detail_resource'


class DeleteResourceView(DeleteView):
    model = Resource
    template_name = 'serviceapp/delete_confirm.html'
    success_url = '/service/list_resource/'
    context_object_name = 'delete_obj'


class CreateResourceView(CreateView):
    model = Resource
    form_class = ResourceForm
    template_name = 'serviceapp/resource_create.html'
    success_url = '/service/list_resource/'


class ListServiceView(ListView):
    model = Service
    paginate_by = 10
    context_object_name = 'list_service'
    template_name = 'serviceapp/service_list.html'
    ordering = '-id'


class DetailServiceView(DetailView):
    model = Service
    template_name = 'serviceapp/service_detail.html'
    context_object_name = 'detail_service'


class DeleteServiceView(DeleteView):
    model = Service
    template_name = 'serviceapp/delete_confirm.html'
    success_url = '/service/list_service/'
    context_object_name = 'delete_obj'


class CreateServiceView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'serviceapp/service_create.html'
    success_url = '/service/create_service/'


def create_service_view(request):
    form = ServiceForm
    if request.method == 'POST':
        Service.objects.create(name=request.POST['name'])
    return render(request, 'serviceapp/service_create.html', {'form': form})


def detail_service_list_resources(request, pk):
    current_serv = Service.objects.get(id=pk)
    resources_list = current_serv.resources.all()
    return render(request, 'serviceapp/service_detail.html',
                  {'data_resource': resources_list, 'data_service': current_serv})


def list_resource_for_service(request, id_service):
    current_serv = Service.objects.get(id=id_service)
    resources_list = current_serv.resources.all()
    return render(request, 'serviceapp/resource_list_from_service.html',
                  {'data_resource': resources_list, 'data_service': current_serv.name.lower()})


# class AddResourceForService(CreateView):
#     model = Service
#     form_class = AddResourceForServiceForm
#     template_name = 'serviceapp/add_resource_for_service.html'
#     success_url = '/service/list_service/'


def add_resource_for_service(request, pk):
    form = AddResourceForServiceForm
    current_serv = Service.objects.get(id=pk)
    if request.method == 'POST':
        add_resource = Resource.objects.get(id=request.POST['resource'])
        current_serv.resources.add(add_resource)
    return render(request, 'serviceapp/add_resource_for_service.html', {'form': form})



# def service_form_view(request, subDir):
#     if subDir == 'service1':
#         form = forms.ServiceForm()
#         if request.method == 'POST':
#             form = forms.ServiceForm(request.POST)
#             if form.is_valid():
#                 form.save()
#             rendered = render_to_string('serviceapp/service_submited.html')
#             return HttpResponse(rendered)
#         context = {'form': form}
#         return render(request, 'serviceapp/service_detail.html', context)
#
#     elif subDir == 'resource':
#         form = forms.ResourceForm()
#         if request.method == 'POST':
#             form = forms.ResourceForm(request.POST)
#             if form.is_valid():
#                 form.save()
#             rendered = render_to_string('serviceapp/resource_submited.html')
#             return HttpResponse(rendered)
#         context = {'form': form}
#         return render(request, 'serviceapp/resource_detail.html', context)
#
#     elif subDir == 'service_table':
#         data = Service.objects.all()
#         context = {'form': data}
#         return render(request, 'serviceapp/service_list.html', context)
#
#     elif subDir == 'resource_table':
#         data = Resource.objects.all()
#         context = {'form': data}
#         return render(request, 'serviceapp/resource_list.html', context)
#
#
# def serviceDelete(request):
#     try:
#         for i in request.POST.copy().pop('id'):
#             Service.objects.get(id=int(i)).delete()
#         rendered = render_to_string('serviceapp/service_delete_confirm.html')
#         return HttpResponse(rendered)
#     except KeyError:
#         data = Service.objects.all()
#         context = {'form': data}
#         return render(request, 'serviceapp/service_list.html', context)
#
#
# def resourceDelete(request):
#     try:
#         for i in request.POST.copy().pop('id'):
#             Resource.objects.get(id=int(i)).delete()
#         rendered = render_to_string('serviceapp/resource_deleted.html')
#         return HttpResponse(rendered)
#     except KeyError:
#         data = Resource.objects.all()
#         context = {'form': data}
#         return render(request, 'serviceapp/resource_list.html', context)
