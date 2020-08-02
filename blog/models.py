from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

class BlogAuthor(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=1000, help_text='Describe yourself in 1000 caracters')


    class Meta:
        ordering = ['user', 'bio']

    def __str__(self):
        return user.username.name

    def get_absolute_url(self):
        return reverse('blogs-by-author', args=[str(self.id)])


class Blog(models.Model):

    title = models.CharField(max_length=80, help_text='the post title')
    post_date = models.DateField(default=date.today)
    content = models.TextField(max_length=2000, help_text='the post content')
    author = models.ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        ordering = ['-post_date']

    def __str__(self):

        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])
    

class BlogComment(models.Model):
    
    content = models.TextField(max_length=200, help_text='content of the comment')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['post_date']

    def __str__(self):
        return self.content
    

