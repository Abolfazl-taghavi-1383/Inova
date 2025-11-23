from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import TeamMember
from .serializers import TeamMemberSerializer

@api_view(['GET'])
def team_list(request):
    members = TeamMember.objects.all()
    serializer = TeamMemberSerializer(members, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def team_detail(request, pk):
    member = get_object_or_404(TeamMember, pk=pk)
    serializer = TeamMemberSerializer(member)
    return Response(serializer.data, status=status.HTTP_200_OK)
