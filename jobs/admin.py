from django.contrib import admin
from .models import Job, Application

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'date_posted')
    search_fields = ('title', 'company', 'location', 'description')
    list_filter = ('company', 'location', 'date_posted')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('student', 'job', 'status', 'applied_on')
    search_fields = ('student__user__username', 'job__title', 'status')
    list_filter = ('status', 'applied_on')