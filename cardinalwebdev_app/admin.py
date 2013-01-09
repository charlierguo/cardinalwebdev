from cardinalwebdev_app.models import *
from django.contrib import admin

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'major', 'attendance', 'interest', 'background', 'comments', 'created_at')
    list_filter = ('created_at',)
    ordering = ['-created_at']
    search_fields = ['name']

admin.site.register(Application, ApplicationAdmin)