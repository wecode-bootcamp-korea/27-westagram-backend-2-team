from django.db import models

class User(models.Model):
    name        = models.CharField(max_length=20)
    email       = models.EmailField(max_length=200,unique=True)
    password    = models.CharField(max_length=200)
    phone_number= models.CharField(max_length=50)
    birthday    = models.DateField(null=True)
    gender      = models.CharField(max_length=20,blank=True,null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class meta:
        db_table = 'users'
