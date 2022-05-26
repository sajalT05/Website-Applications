from pydoc import describe
from pyexpat import model
from django.db import models
import uuid
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# pygments
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


# --> Create your models here

# column_name=models.TextField(max_length=50)

# todo list form database model 
# forms database: [TodolistForm]
class TodolistForm(models.Model):
    # creating datable from 
    # -- create models for form database
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_description=models.TextField(max_length=50)
    # string representation of the object
    # attribute title of the saved form in the admin backend database
    def __str__(self):
        return self.first_name+" "+self.last_name+" | ("+self.user_email+")"

# blog model
class Blog(models.Model):
    serialnumber=models.AutoField(primary_key=True)
    blog_title=models.CharField(max_length=200)
    blog_content=models.TextField()
    blog_slug=models.CharField(max_length=100)
    blog_time=models.DateTimeField(auto_now_add=True)
    # string representation of the blog object
    # attribute title of the saved blog in the admin backend database
    def __str__(self):
        return self.blog_title