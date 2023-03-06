from django.shortcuts import render
from rest_framework.generics import ListAPIView 
from .models import Content, Profile

from .serializers import (
    ContentSerializer,
    ProfileSerializer,
)

class ContentListView(ListAPIView):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()

class ProfileListView(ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
