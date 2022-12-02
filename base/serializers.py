from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Content, Profile


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        read_only_fields = '__all__'
    

class ContentSerializer(ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = Content
        read_only_fields =  ['photo', 'title', 'profile']