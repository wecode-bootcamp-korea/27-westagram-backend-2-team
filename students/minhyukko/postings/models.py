from django.db import models

from users.models import User

class Posting(models.Model): 
    user       = models.ForeignKey(User, on_delete= models.CASCADE)
    image      = models.CharField(max_length=300)
    post       = models.CharField(max_length=300, null = True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'postings'