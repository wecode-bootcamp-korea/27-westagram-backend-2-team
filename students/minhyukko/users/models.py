from django.db import models

from core.models import TimeStampModel

class User(TimeStampModel): 
    name        = models.CharField(max_length= 100)
    email       = models.CharField(max_length=250 , unique= True)
    password    = models.CharField(max_length=300)
    address     = models.CharField(max_length=100)
    information = models.CharField(max_length= 250, null = True)
    
    class Meta: 
        db_table = 'users'