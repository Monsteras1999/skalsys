from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Task

# Create your views here.

def index(request):
    task_list = Task.objects.order_by('-deadline')
    template = loader.get_template('todo/index.html')
    context = {'task_list': task_list}
    return HttpResponse(template.render(context, request))

def edit(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'todo/content/edittodo.html', {'task': task})
    # template = loader.get_template('todo/content/edittodo.html')
    # context = {'task': task}
    # return HttpResponse(template.render(context, request))

def delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'todo/content/deletetodo.html', {'task': task})

def new(request):
    return render(request, 'todo/content/newtodo.html', {})

def disclaimer(request):
    return render(request, 'todo/content/disclaimer.html', {})