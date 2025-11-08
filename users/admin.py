from django.contrib import admin
from .models import StudentProfile

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'skills', 'major', 'yos', 'resume' )
    search_fields = ('user__username', 'location', 'skills')
    list_filter = ('location',)
