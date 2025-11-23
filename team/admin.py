from django.contrib import admin

from .models import TeamMember

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'role', 'linkedin', 'github')
    search_fields = ('full_name', 'role')
