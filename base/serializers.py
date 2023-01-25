from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Content, Profile
from django.contrib.auth.models import User

class RegistrationSerializer(ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'password2']
        extra_kwargs = { 'password': {'write_only': True} }

    def save(self):
        user = User(
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
    

class ContentSerializer(ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = Content
        fields = '__all__'