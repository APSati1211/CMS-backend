from django.contrib import admin
from .models import JobOpening, JobApplication

@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'location', 'type', 'is_active', 'created_at')
    list_filter = ('is_active', 'type', 'department')
    search_fields = ('title', 'description')

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant_name', 'email', 'job', 'applied_at')
    list_filter = ('job',)
    search_fields = ('applicant_name', 'email')