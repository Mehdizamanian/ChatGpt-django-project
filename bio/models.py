from django.db import models
from django.utils import timezone

class Home(models.Model):
    title_owner= models.CharField(max_length=200)
    title_fixed= models.CharField(max_length=200)
    title_job= models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True,blank=True,upload_to="images/")
    thumbnailbio= models.ImageField(null=True,blank=True,upload_to="images/")
    status=models.BooleanField(default=True)



class About(models.Model):
    description= models.TextField()
    des_title= models.CharField(max_length=230)
    des_title_des= models.TextField()
    des_detail= models.TextField()
    extra_des= models.TextField()
    thumbnailabout = models.ImageField(null=True,blank=True,upload_to="images/")
    status=models.BooleanField(default=True)

class Resume(models.Model):
    description= models.TextField(blank=True)
    project_des = models.TextField()
    project_owner = models.CharField(max_length=230)
    project_owner_title = models.CharField(max_length=230)
    # picowner = models.ImageField(null=True,blank=True,upload_to="images/")
    ownerimg = models.ImageField(null=True,blank=True,upload_to="images/")
    status=models.BooleanField(default=True)

class Contact(models.Model):
    description= models.TextField()
    location = models.TextField()
    email = models.CharField(max_length=230)
    phone= models.CharField(max_length=230)
    age = models.IntegerField()
    degree = models.CharField(max_length=230)
    birthday = models.CharField(max_length=230)
    website = models.CharField(max_length=230)
    city = models.CharField(max_length=230)
    loc_pic = models.ImageField(null=True,blank=True,upload_to="images/")
    status=models.BooleanField(default=True)
    loc_src_map = models.TextField(blank=True)



class Social(models.Model):
    social_name= models.TextField()
    social_link = models.TextField()
    status=models.BooleanField(default=True)


# class project (models.Model):
#     pr_owner = models.CharField(max_length=230)
#     pr_owner_title = models.CharField(max_length=230)
#     prpicowner = models.ImageField(null=True,blank=True,upload_to="images/")
#     status=models.BooleanField(default=True)

# Create your models here.
