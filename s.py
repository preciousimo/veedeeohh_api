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
    data = ['/profile', '/content', 'content/:title']
    return Response(data)


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def content_list(request):
    # Handles GET requests
    if request.method == 'GET':
        query = request.GET.get('query')

        if query == None:
            query = ''

        contents = Content.objects.filter(
            Q(username__icontains=query) | Q(bio__icontains=query))
        serializer = ContentSerializer(contents, many=True)

        return Response(serializer.data)

    if request.method == 'POST':
        content = Content.objects.create(
            username=request.data['username'],
            bio=request.data['bio']
        )
        serializer = ContentSerializer(content, many=False)

        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def content_detail(request, username):
    content = Content.objects.get(username=username)

    if request.method == 'GET':
        serializer = ContentSerializer(content, many=False)
        return Response(serializer.data)

    if request.method == 'PUT':
        content.username = request.data['username']
        content.bio = request.data['bio']

        content.save()

        serializer = ContentSerializer(content, many=False)
        return Response(serializer.data)

    if request.method == 'DELETE':
        content.delete()
        return Response('User was deleted!')


@api_view(['GET', 'POST'])
def profile_list(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)







def advocate_detail(request, username):
    advocate = Advocate.objects.get(username=username)

    if request.method == 'GET':
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)
        
    if request.method == 'PUT':
        advocate.username = request.data['username']
        advocate.bio = request.data['bio']

        advocate.save()

        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)





def advocate_list(request):
    # Handles GET requests
    if request.method == 'GET':
        query = request.GET.get('query')
        
        if query == None:
            query = ''
        
        advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
        serializer = AdvocateSerializer(advocates, many=True)

        return Response(serializer.data)

    if request.method == 'POST':
        advocate = Advocate.objects.create(
            username=request.data['username'],
            bio=request.data['bio']
        )
        serializer = AdvocateSerializer(advocate, many=False)
        
        return Response(serializer.data)









