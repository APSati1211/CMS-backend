from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import CareersPage, Benefit, JobOpening, JobApplication

@admin.register(CareersPage)
class CareersPageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return CareersPage.objects.count() == 0

@admin.register(Benefit)
class BenefitAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'icon_name', 'order')

@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'type', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('department', 'type', 'is_active')

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant_name', 'job', 'email', 'applied_at')
    list_filter = ('job', 'applied_at')
    search_fields = ('applicant_name', 'email')