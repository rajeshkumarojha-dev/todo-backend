from django.db import models

# Create your models here.

class Todo(models.Model):
    task=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    class Meta:
        db_table='todo'