from django.db import models

# Create your models here.
#modelo de tareas
#creamos una clase nombre de la tabla
class Task(models.Model):
    title=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    done=models.BooleanField(default=False)

    def __str__(self):
        return self.title