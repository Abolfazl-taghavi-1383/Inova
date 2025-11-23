from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import TeamMember, Project
from .serializers import (
                          ProjectSerializer,
                          WorkExperience,
                          WorkExperienceSerializer,
                          TeamMemberDetailSerializer,
                          TeamMemberListSerializer,
                          )

@api_view(['GET'])
def team_list(request):
    members = TeamMember.objects.all()
    serializer = TeamMemberListSerializer(members, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def team_detail(request, pk):
    member = get_object_or_404(TeamMember, pk=pk)
    serializer = TeamMemberDetailSerializer(member)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def project_list(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    serializer = ProjectSerializer(project)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def experience_list(request):
    exps = WorkExperience.objects.all()
    serializer = WorkExperienceSerializer(exps, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def experience_detail(request, pk):
    exp = get_object_or_404(WorkExperience, pk=pk)
    serializer = WorkExperienceSerializer(exp)
    return Response(serializer.data, status=status.HTTP_200_OK)