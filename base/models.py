from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True, blank=True)
    img = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.name

class Content(models.Model):
    photo = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    view = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title