from django.db import models
from django.contrib.auth.models import User


class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_pub = models.BooleanField(default=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    birth_date = models.DateField(null=True, blank=True)

class Task(models.Model):
    problem = models.CharField(max_length=255)
    answer = models.IntegerField()
