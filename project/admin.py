"""
Registers the project and skill models to the admin page.

Author: Benjamin Garrard
Date: 5/12/2019
"""
from django.contrib import admin
from .models import Project, Skill


class SkillAdmin(admin.ModelAdmin):
    """Set the display in admin to skill and score only."""

    list_display = ('skill', 'score')


class ProjectAdmin(admin.ModelAdmin):
    """Set the display in admin to project_name only."""

    list_display = ('project_name',)


# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)