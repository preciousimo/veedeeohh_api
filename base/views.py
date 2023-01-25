from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q 
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Content, Profile
from .serializers import ContentSerializer, ProfileSerializer, RegistrationSerializer


# Create your views here.

@csrf_exempt
@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "New user registered"
            data['username'] = user.username
            token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)}, status=201)
        else:
            data = serializer.errors
        return Response(data)
            
            

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
@permission_classes([IsAuthenticated])
def content(request):
    contents = Content.objects.all()
    serializer = ContentSerializer(contents, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def profile_content(request):
    pass


@api_view(['GET', 'PUT', 'DELETE'])
def profile(request):
    pass
