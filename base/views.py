from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404
from django.db.models import Q
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Content, Profile
from .serializers import ContentSerializer, ProfileSerializer


# Create your views here.

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request) # data is a dictionary
            user = User.objects.create_user(username=data['username'], password=data['password'])
            user.save()

            token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)}, status=201)

        except IntegrityError:
            return JsonResponse({'error':'username taken, choose another username'}, status=400)
            

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(request, username=data['username'], password=data['password'])
        if user is None:
            return JsonResponse({'error':'unable to login. Check username and password'}, status=400)
        else: # return user token
            try:
                token = Token.objects.get(user=user)
            except: # If token not in db, create a new one
                token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)}, status=201)


@api_view(['GET'])
def endpoints(request):

    # data = ['/profiles', '/contents', 'contents/:profile']
    data = ['/contents']

    return Response(data)


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def content(request):
    contents = Content.objects.all()
    serializer = ContentSerializer(contents, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def profile_content(request):
    pass


@api_view(['GET', 'PUT', 'DELETE'])
def profile(request):
    pass
