from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# class Topic(models.Model):
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    # topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null = True)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now = True)
    

    class Meta :
        ordering = ['-date_posted']
        
    def __str__(self):
        return self.content[0:50]
    



