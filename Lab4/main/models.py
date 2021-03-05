from django.db import models

class Todo(models.Model):
    number=models.CharField(max_length=30)
    created=models.CharField(max_length=30)
    dueTo=models.CharField(max_length=30)
    action=models.TextField()
    completed=models.BooleanField()