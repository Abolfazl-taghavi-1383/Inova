from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import StreamingHttpResponse, Http404
import boto3
import mimetypes
from django.conf import settings

from .models import TeamMember, Project, WorkExperience, Education, Achievement
from .serializers import (
                          ProjectSerializer,
                          TeamMemberDetailSerializer,
                          TeamMemberListSerializer,
                          )

MODEL_CONFIG = {
    'member': {'model': TeamMember, 'field': 'photo'},
    'project': {'model': Project, 'field': 'image'},
    'experience': {'model': WorkExperience, 'field': 'image'},
    'education': {'model': Education, 'field': 'image'},
    'achievement': {'model': Achievement, 'field': 'image'}
}


@api_view(['GET'])
@permission_classes([AllowAny])
def serve_universal_image(request, model_type, pk):
    config = MODEL_CONFIG.get(model_type)
    
    if not config:
        raise Http404("Invalid resource type")

    model_class = config['model']
    field_name = config['field']

    obj = get_object_or_404(model_class, pk=pk)
    
    image_field = getattr(obj, field_name)

    if not image_field:
        return Response({'message': 'object has no image',}, status=status.HTTP_200_OK)

    try:
       file_handle = image_field.open(mode='rb')
       content_type, _ = mimetypes.guess_type(image_field.name)
       
       if content_type is None:
            content_type = 'application/octet-stream'
            response = StreamingHttpResponse(file_handle, content_type=content_type)

            response['Content-Disposition'] = f'inline; filename="{image_field.name.split("/")[-1]}"'
            response['Content-Length'] = image_field.size

            return response

    except Exception as e:
        print(f"Error serving file from S3 storage: {e}")
        raise Http404("File could not be retrieved from storage.")


@api_view(['GET'])
def team_list(request):
    members = TeamMember.objects.all()
    serializer = TeamMemberListSerializer(members, many=True, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def team_detail(request, pk):
    member = get_object_or_404(TeamMember, pk=pk)
    serializer = TeamMemberDetailSerializer(member, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def project_list(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, context={'request': request})
    serializer = ProjectSerializer(project)
    return Response(serializer.data, status=status.HTTP_200_OK)
