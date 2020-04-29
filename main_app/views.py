from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch
# Create your views here.
def home(request):
  return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

class FinchList(ListView):
    model = Finch

def get_queryset(self):
    return Finch.objects.all()
    
class FinchDetail(DetailView):
    model = Finch

class FinchCreate(CreateView):
     model = Finch
     fields = '__all__' 

class FinchUpdate(UpdateView):
    model = Finch
    fields = '__all__'

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'