from django.db import models

# Create your models here.

class User(models.Model):
    name        = models.CharField(max_length= 20)
    email       = models.CharField(max_length=250 , unique= True)
    password    = models.CharField(max_length=20)
    address     = models.CharField(max_length=12)
    information = models.CharField(max_length= 250)