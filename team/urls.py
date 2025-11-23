from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_list, name='team-list'),
    path('<int:pk>/', views.team_detail, name='team-detail'),
    path('projects/', views.project_list, name='project-list'),
    path('projects/<int:pk>/', views.project_detail, name='project-detail'),
    path('experiences/', views.experience_list, name='experience-list'),
    path('experiences/<int:pk>/', views.experience_detail, name='experience-detail'),
]
