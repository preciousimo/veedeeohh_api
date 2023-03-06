from rest_framework import serializers
from .models import Content, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
    

class ContentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = Content
        fields = '__all__'
        depth = 1
