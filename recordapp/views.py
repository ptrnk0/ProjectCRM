from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from recordapp.forms import RecordForm
from recordapp.models import Record


class CreateRecordView(CreateView):
    model = Record
    form_class = RecordForm
    template_name = 'record_main.html'
    success_url = '/record/create/'

    # def post(self, request, *args, **kwargs):
    #     print(request.POST)
    #     super().post(request, *args, **kwargs)
    #     return HttpResponse({
    #         'message': 'success'
    #     })


class ListRecordView(ListView):
    model = Record
    template_name = 'record_main.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        date = request.GET.get('date')
        obj = Record.objects.filter(date=date)
        obj_json = serializers.serialize('json', obj)
        return HttpResponse(obj_json, content_type='application/json')
