from django.db import models

# Create your models here.
 
class Author (models.Model):
 name = models.CharField("Author", max_length = 50)

class Post(models.Model):
 heading = models.CharField("Heading",max_length=50)
 content = models.CharField("Content",max_length=1000)
 Author = models.ForeignKey(Author,related_name='posts', on_delete=models.CASCADE)

