from django.shortcuts import render
from .forms import toDoFormModel

def index(request):
    context = {}
    form = toDoFormModel(request.POST)
    if form.is_valid():
        form.save()
    
    context['form'] = form
    return render(request, 'index.html', context)

def cadastro(request):