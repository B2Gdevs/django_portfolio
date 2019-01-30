from django.contrib import admin
from .models import Project, Skill

class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill', 'score')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name',)

# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)