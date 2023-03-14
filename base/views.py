from django.shortcuts import render
from rest_framework.generics import ListAPIView 
from .models import Content, Profile, Topic

from .serializers import (
    ContentSerializer,
    TopicSerializer,
    ProfileSerializer,
)

class ContentListView(ListAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()

class TopicListView(ListAPIView):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()

class ProfileListView(ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
