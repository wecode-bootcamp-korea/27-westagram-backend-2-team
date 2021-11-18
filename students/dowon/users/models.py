from enum import unique
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=45)
    phone = models.IntegerField(unique=True)
    information = models.CharField(max_length=300)

    class Meta:
        db_table = 'users'
    
    def __str__(self):
	    return self.name

# Create your models here.
