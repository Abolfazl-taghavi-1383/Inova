from django.contrib import admin

from .models import TeamMember, Project, WorkExperience

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'role', 'linkedin', 'github')
    search_fields = ('full_name', 'role')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'start_date', 'end_date')
    search_fields = ('title', 'category')
    filter_horizontal = ('members',)
    
@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'position', 'member', 'start_date', 'end_date')
    search_fields = ('company_name', 'position', 'member__full_name')