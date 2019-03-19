from django.contrib import admin
from .models import Summary

class SummaryAdmin(admin.ModelAdmin):
    list_display = ('about_me', 'education')

# Register your models here.
admin.site.register(Summary, SummaryAdmin)
