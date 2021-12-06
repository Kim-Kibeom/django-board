from django.db import models
from user.models import User

# Create your models here.
class Post (models.Model):
    author      = models.ForeignKey("user.User", on_delete=models.CASCADE)
    title       = models.CharField(max_length=200)
    content     = models.CharField(max_length=200)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    # method
    def __str__(self):
        return self.title
    
