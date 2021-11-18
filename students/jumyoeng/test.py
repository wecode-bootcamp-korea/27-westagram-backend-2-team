from enum import unique
from django.db.models.base import Model
from django.db import models

class User(models.Model) :
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    password = models.CharField(max_length=45)
    phone = models.CharField(max_length=15)
    descr = models.TextField(null=True)
    
    class Meta :
        db_table = 'users'
        unique_together = ('name', 'email')