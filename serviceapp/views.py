# from django.shortcuts import render
# from django.shortcuts import render
# from django.template.loader import render_to_string
# from serviceapp import forms
# from django.http import HttpResponse
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
    success_url = '/service/list_service/'


class ListResourceForServiceView(DetailView):
    model = Service
    template_name = 'serviceapp/resource_list_from_service.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["resource_list"] = Resource.objects.all()
        return context


class AddResourceForService(CreateView):
    model = Service
    form_class = AddResourceForServiceForm
    template_name = 'serviceapp/add_resource_for_service.html'
    success_url = '/service/list_service/'


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