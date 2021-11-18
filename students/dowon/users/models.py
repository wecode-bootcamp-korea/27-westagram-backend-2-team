from django.db import models

class User(models.Model):
    name		= models.CharField(max_length=45)
    email		= models.CharField(max_length=45, unique=True)
    password	= models.CharField(max_length=200)
    phone_number= models.CharField(unique=True)
    information	= models.CharField(max_length=300)

    class Meta:
        db_table = 'users'
    
# Create your models here.
