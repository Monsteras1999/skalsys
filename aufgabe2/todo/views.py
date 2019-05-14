from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Task

# Create your views here.

def index(request):
    task_list = Task.objects.order_by('deadline')
    return render(request, 'todo/index.html', {'task_list': task_list})

def saveedit(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    try:
        new_task = request.POST['todo']
        if not new_task:
            return render(request, 'todo/content/edittodo.html', {'task': task, 'error_message': "An Error occured."})
        new_deadline = request.POST['deadline']
        if not new_deadline:
            return render(request, 'todo/content/edittodo.html', {'task': task, 'error_message': "An Error occured."})
        new_progress = int(request.POST['progress'])
        if new_progress<0 or new_progress>100:
            return render(request, 'todo/content/edittodo.html', {'task': task, 'error_message': "An Error occured."})
    except:
        return render(request, 'todo/content/edittodo.html', {
            'task': task,
            'error_message': "An Error occured.",
        })
    else:
        task.task_text = new_task
        task.deadline = new_deadline
        task.progress = new_progress
        task.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('todo:index'))

def savenew(request):
    try:
        new_task = request.POST['todo']
        if not new_task:
            return render(request, 'todo/content/newtodo.html', {'error_message': "An Error occured."})
        new_deadline = request.POST['deadline']
        if not new_deadline:
            return render(request, 'todo/content/newtodo.html', {'error_message': "An Error occured."})
        new_progress = int(request.POST['progress'])
        if new_progress<0 or new_progress>100:
            return render(request, 'todo/content/newtodo.html', {'error_message': "An Error occured."})
    except:
        return render(request, 'todo/content/newtodo.html', {'error_message': "An Error occured."})
    else:
        new_todo = Task(task_text=new_task, deadline=new_deadline, progress=new_progress)
        new_todo.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('todo:index'))

def edit(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'todo/content/edittodo.html', {'task': task})

def delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    # Always return an HttpResponseRedirect after successfully dealings
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('todo:index'))

def new(request):
    return render(request, 'todo/content/newtodo.html', {})

def disclaimer(request):
    return render(request, 'todo/content/disclaimer.html', {})