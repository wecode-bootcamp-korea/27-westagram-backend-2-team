from django.db import models

# Create your models here.

class User(models.Model):
    name        = models.CharField(max_length= 20)
    email       = models.CharField(max_length=250 , unique= True)
    password    = models.CharField(max_length=300)
    address     = models.CharField(max_length=20)
    information = models.CharField(max_length= 250)
    class Meta:
        db_table = 'users'