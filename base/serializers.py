from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Content, Profile


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
    

class ContentSerializer(ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = Content
        fields = '__all__'