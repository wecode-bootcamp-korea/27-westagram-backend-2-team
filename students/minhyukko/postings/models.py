from django.db import models

from users.models import User
from core.models import TimeStampModel

class Post(TimeStampModel): 
    posting_user = models.ForeignKey(User, on_delete= models.CASCADE)
    title        = models.CharField(max_length=200)
    image        = models.URLField(max_length=300, null = True)
    context      = models.CharField(max_length=300, null = True)
        

    class Meta:
        db_table = 'posts'