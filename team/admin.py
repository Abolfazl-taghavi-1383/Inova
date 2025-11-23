from django.contrib import admin

from .models import TeamMember, Project

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'role', 'linkedin', 'github')
    search_fields = ('full_name', 'role')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'start_date', 'end_date')
    search_fields = ('title', 'category')
    filter_horizontal = ('members',)