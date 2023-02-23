from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date , datetime
from ckeditor.fields import RichTextField
# Create your models here.

# class Topic(models.Model):
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    header_image = models.ImageField(null=True, blank=True, upload_to="images")
    title_tag = models.CharField(max_length=200, default='Ridelink Series')
    # topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null = True)
    # content = models.TextField()
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add = True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    

    class Meta :
        ordering = ['-date_posted']
        
    def __str__(self):
        return self.title + '|' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('article-detail',args =(str(self.id)))


