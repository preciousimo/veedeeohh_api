from django.urls import path
from .views import ContentListView, ProfileListView

app_name = "base"

urlpatterns = [ 
    path("contents/", ContentListView.as_view(), name="content-list"),
    path("profiles/", ProfileListView.as_view(), name="profile-list"), 
]