from django.contrib import admin
from .models import Profile, Content, Topic
# Register your models here.

admin.site.register(Profile)
admin.site.register(Topic)
admin.site.register(Content)