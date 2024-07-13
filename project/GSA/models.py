# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser



class Register(AbstractUser):
    mobile = models.CharField(max_length=15, null=True, blank=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
  

    def __str__(self):
        return self.username

class Task(models.Model):
    STATUS_CHOICE=[
        ('pending','Pending'),
        ('completed','Completed')
    ]
    task_name = models.CharField(max_length=200)
    due_date = models.DateField()
    time = models.DateTimeField(auto_now=True)
    assigned_by = models.CharField(max_length=200)
    assigned_to=models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=200,choices=STATUS_CHOICE,default=False,null=True)

    def __str__(self):
        return self.task_name
