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

def edit(request):
    task = get_object_or_404(Task, pk=task_id)
    template = loader.get_template('todo/content/edittodo.html')
    context = {'task': task}
    return HttpResponse(template.render(context, request))