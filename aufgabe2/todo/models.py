from django.db import models

# Create your models here.

class Task(models.Model):
    task_text = models.CharField(max_length=200)
    deadline = models.DateField('Deadline')
    progress = models.IntegerField(default=0)

    def __str__(self):
        return self.task_text