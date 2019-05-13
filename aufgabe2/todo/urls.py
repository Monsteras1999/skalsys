from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    # ex: /todo/
    path('', views.index, name='index'),
    # ex: /todo/5/edit
    path('<int:pk>/edit', views.edit, name='edit')

]