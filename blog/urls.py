from django.urls import path
from .views import ListPostAPIView, DetailPostAPIView

app_name = "posts"

urlpatterns = [
    path("", ListPostAPIView.as_view(), name="list_post"),
    path("<str:slug>/", DetailPostAPIView.as_view(), name="post_detail"),
]