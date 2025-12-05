from django.urls import path
from .views import ListPostAPIView, DetailPostAPIView, serve_universal_image

app_name = "blog"

urlpatterns = [
    path("", ListPostAPIView.as_view(), name="list_post"),
    path("<str:slug>/", DetailPostAPIView.as_view(), name="post_detail"),
    path('media/<str:model_type>/<uuid:pk>/', serve_universal_image, name='universal_image_serve'),
]