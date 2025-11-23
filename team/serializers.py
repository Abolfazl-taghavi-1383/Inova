from rest_framework import serializers

from .models import TeamMember

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['id', 'full_name', 'role', 'bio', 'photo', 'linkedin', 'github']
