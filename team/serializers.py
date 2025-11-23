from rest_framework import serializers

from .models import TeamMember

from rest_framework import serializers
from .models import TeamMember, Project, WorkExperience, Education


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'degree', 'field_of_study', 'university', 'start_year', 'end_year', 'description']


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ['id', 'company_name', 'position', 'start_date', 'end_date', 'description']


class ProjectSerializer(serializers.ModelSerializer):
    members = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'description', 'category', 'image', 'link',
            'start_date', 'end_date', 'members'
        ]


class TeamMemberSerializer(serializers.ModelSerializer):
    educations = EducationSerializer(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    work_experiences = WorkExperienceSerializer(many=True, read_only=True)

    class Meta:
        model = TeamMember
        fields = [
            'id', 'full_name', 'role', 'bio', 'photo',
            'linkedin', 'github', 'projects', 'work_experiences',
            'educations', 
        ]


