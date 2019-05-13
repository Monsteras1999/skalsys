from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    # ex: /todo/
    path('', views.index, name='index'),
    # ex: /todo/5/edit
    path('<int:task_id>/edit', views.edit, name='edit'),
    # ex: /todo/5/delete
    path('<int:task_id>/delete', views.delete, name='delete'),
    # ex: /todo/new
    path('new', views.new, name='new'),
    # ex: /todo/new
    path('disclaimer', views.disclaimer, name='disclaimer')

]