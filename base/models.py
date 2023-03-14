from django.db import models 
from users.models import CustomUser


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True, blank=True)
    img = models.ImageField(null=True, blank=True, upload_to="profile/images/")


    def __str__(self):
        return self.name
    
class Topic(models.Model):
    name = models.CharField(max_length=200) 

    def __str__(self):
        return self.name 

class Content(models.Model):
    thumbnail = models.ImageField(null=True, blank=True, upload_to="content/thumbnails/")
    video = models.FileField(blank=True, null=True, upload_to="content/videos/")
    title = models.CharField(max_length=500, null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    view = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title