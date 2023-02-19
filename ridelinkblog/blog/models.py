from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

# class Topic(models.Model):
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=200, default='Ridelink Series')
    # topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null = True)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now = True)
    

    class Meta :
        ordering = ['-date_posted']
        
    def __str__(self):
        return self.title + '|' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('article-detail',args =(str(self.id)))


