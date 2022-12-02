from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=200)
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