from django.contrib.auth.models import User

from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = RichTextField(blank=True,null=True)
    # content = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    post_image = models.ImageField(null=True, blank=True)
    blog_views = models.TextField(default=0)
    category=models.CharField(max_length=200,choices=(('Technology', 'Technology'),
                                                      ('Computer_Security', 'Computer_Security'),
                                                      ('Tips_and_Trick', 'Tips_and_Trick')))
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'id':self.id})

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    reply=models.ForeignKey('Comment',null=True,blank=True, related_name='replies',on_delete=models.CASCADE)
    content=models.TextField(max_length=200)
    Full_Name=models.CharField(max_length=200)
    email=models.EmailField()
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return  'by' +" "+ str(self.Full_Name)


class Suggestion(models.Model):
    name = models.TextField(max_length=200)
    email=models.EmailField()
    message = models.TextField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
#to store the ip address of all user
class User(models.Model):
    user=models.TextField(default=None)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user