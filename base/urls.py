from django.urls import path
from .views import ContentListView, ProfileListView

app_name = "base"

urlpatterns = [ 
    path("", ContentListView.as_view(), name="content-list"),
    path("categories", ProfileListView.as_view(), name="category-list"), 
]