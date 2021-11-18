from django.db import models

class User(models.Model):
    name       = models.CharField(max_length=20)
    email      = models.EmailField(max_length=20,unique=True)
    password   = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=20)
    birthday   = models.CharField(max_length=20)
    gender     = models.CharField(max_length=20)

    class meta:
        db_table = 'users'



