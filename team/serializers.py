from rest_framework import serializers

from .models import TeamMember

from rest_framework import serializers
from .models import TeamMember, Project, WorkExperience, Education, Achievement


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ['id', 'image', 'title', 'description', 'event', 'date', 'award', 'link']


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'image', 'degree', 'field_of_study', 'university', 'start_year', 'end_year', 'description']


class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ['id', 'image', 'company_name', 'position', 'start_date', 'end_date', 'description']


class ProjectSerializer(serializers.ModelSerializer):
    members = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'description', 'category', 'image', 'link',
            'start_date', 'end_date', 'members',
        ]


class TeamMemberDetailSerializer(serializers.ModelSerializer):
    educations = EducationSerializer(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    work_experiences = WorkExperienceSerializer(many=True, read_only=True)
    achievements = AchievementSerializer(many=True, read_only=True)

    class Meta:
        model = TeamMember
        fields = [
            'id', 'full_name', 'role', 'bio', 'photo',
            'linkedin', 'github', 'projects','skills',
            'work_experiences', 'educations', 'achievements'
        ]

class TeamMemberListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['id', 'full_name', 'role', 'bio', 'photo','skills', ]
