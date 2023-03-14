from rest_framework import serializers
from .models import Content, Profile, Topic

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'
    

class ContentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = Content
        fields = '__all__'
        depth = 1
