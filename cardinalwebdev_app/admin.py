from cardinalwebdev_app.models import *
from django.contrib import admin

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'major', 'attendance', 'interest', 'background', 'comments', 'created_at')
    list_filter = ('created_at',)
    ordering = ['-created_at']
    search_fields = ['name']

class ApplicationReviewAdmin(admin.ModelAdmin):
    list_display = ('application', 'total', 'charlie_decision', 'charlie_comments', 'kevin_decision', 'kevin_comments', 'kingston_decision', 'kingston_comments', 'created_at')
    list_filter = ('created_at',)
    ordering = ['-created_at']
    search_fields = ['application']

admin.site.register(Application, ApplicationAdmin)
admin.site.register(ApplicationReview, ApplicationReviewAdmin)
admin.site.register(Student)