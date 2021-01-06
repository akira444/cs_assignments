from django.shortcuts import render, redirect 
from django.views import View
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.template.loader import render_to_string

from namecollect.models import Person


# Create your views here.

class MainView (View):
    def get(self, request):
        pl = Person.objects.all()

        ctx = {'person_list': pl}
        return render(request, 'namecollect/person_list.html', ctx)
        

class PersonCreate (CreateView):
    model=Person
    fields='__all__'
    success_url=reverse_lazy('namecollect:all')
    