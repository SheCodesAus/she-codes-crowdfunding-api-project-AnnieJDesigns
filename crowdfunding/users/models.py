from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    about = models.CharField(max_length=200, blank=True, default='')
    charity_abn = models.IntegerField(blank=True, default=0)
    

def __str__(self):
    return self.username 
# str print as string
