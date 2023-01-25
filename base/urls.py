from django.urls import path
from .views import*

urlpatterns = [
    # AUTHENTICATION 
    path('signup/', signup, name='signup'),
    path('login/', login),

    # CONTENT
    path('', endpoints),
    path('contents/', content, name='contents'),

    # PROFILE
    path('profiles/', profile, name='profiles'),
    path('contents/<str:profile>/', profile_content), # I don't know why i created this path hopefully i'll figure it
]