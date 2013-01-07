from cardinalwebdev_app.models import *
from django.contrib import admin

class EmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    list_filter = ('created_at',)
    ordering = ['-created_at']
    search_fields = ['email']

admin.site.register(Email, EmailAdmin)