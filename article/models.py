from django.db import models

from django.utils import timezone

class Article (models.Model):
    title = models.CharField(max_length=200)
    slug=models.SlugField(max_length=200 , unique=True)
    description=models.TextField()  
    thumbnail=models.ImageField(null=True,blank=True,upload_to="images/")
    publish=models.DateTimeField(default=timezone.now) 
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True) 
    status=models.BooleanField(default=False)
     
    def __str__(self):
        return self.title


# Create your models here.
