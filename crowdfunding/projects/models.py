from django.db import models

class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    goal=models.IntegerField()
    image=models.URLField()
    is_open=models.BooleanField()
    date_created=models.DateTimeField(auto_now_add=True)
    owner=models.CharField(max_length=200) #user has to be a number so that we can reference them in the user data schema
# Create your models here.

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE, #CASCADE is so that everything get deleted if that is the case
        related_name= 'pledges'
    )
    supporter = models.CharField(max_length=200)
