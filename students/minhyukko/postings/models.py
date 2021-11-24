from django.db import models

from users.models import Users

class Posting(models.Model): 
    user       = models.ForeignKey(Users, on_delete= models.CASCADE)
    image      = models.CharField(max_length=300)
    post       = models.CharField(max_length=300, null = True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'postings'