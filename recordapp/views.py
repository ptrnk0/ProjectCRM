from django.views.generic import ListView
from django.views.generic.edit import CreateView
from recordapp.forms import RecordForm
from recordapp.models import Record


class CreateRecordView(CreateView):
    model = Record
    form_class = RecordForm
    template_name = ''
    success_url = 'record/create/'

    def post(self, request, *args, **kwargs):
        pass


class ListRecordView(ListView):
    model = Record
    template_name = ''
    paginate_by = 10
    ordering = '-date'

    def get(self, request, *args, **kwargs):
        pass
