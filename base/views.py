from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404
from django.db.models import Q

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Content, Profile
from .serializers import ContentSerializer, ProfileSerializer


# Create your views here.
@api_view(['GET'])
def endpoints(request):

    data = ['/profiles', '/contents', 'contents/:profile']
    
    return Response(data)

@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def content(request):
    pass

@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def profile_content(request):
    pass

@api_view(['GET', 'POST'])
def profile(request):
    pass