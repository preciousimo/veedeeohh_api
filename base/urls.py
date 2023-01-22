from django.urls import path
from . import views

urlpatterns = [
    # CONTENT
    path('', views.endpoints),
    path('contents/', views.content, name='contents'),

    # PROFILE
    path('profiles/', views.profile, name='profiles'),
    path('contents/<str:profile>/', views.profile_content), # I don't know why i created this path hopefully i'll figure it
    path('signup/', views.signup),
]