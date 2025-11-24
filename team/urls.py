from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_list, name='team-list'),
    path('<uuid:pk>/', views.team_detail, name='team-detail'),
    path('projects/', views.project_list, name='project-list'),
    path('projects/<uuid:pk>/', views.project_detail, name='project-detail'),
    path('media/<str:model_type>/<uuid:pk>/', views.serve_universal_image, name='universal_image_serve'),
]
