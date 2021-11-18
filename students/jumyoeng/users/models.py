from django.db import models

class User(models.Model) :
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    descr = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta : 
        unique_together = ('name', 'email')
        db_table = 'users'