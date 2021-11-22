from django.db import models

class User(models.Model):
    name         = models.CharField(max_length=30)
    email        = models.CharField(max_length=100, unique=True)
    password     = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=100)
    address      = models.CharField(max_length=100, blank=True)
    job          = models.CharField(max_length=30, blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Users"
    