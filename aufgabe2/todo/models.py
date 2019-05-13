import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    task_text = models.CharField(max_length=200)
    deadline = models.DateField('Deadline')
    progress = models.IntegerField(default=0)
    done = models.IntegerField(default=0)
    def __str__(self):
        return self.task_text