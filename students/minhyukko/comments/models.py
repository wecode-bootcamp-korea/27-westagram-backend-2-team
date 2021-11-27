from django.db          import models

from postings.models    import Post
from users.models       import User
from core.models        import TimeStampModel

class Comment(TimeStampModel):
    post    = models.ForeignKey(Post, on_delete=models.CASCADE)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length = 300)
    
    class Meta:
        db_table = 'comments'