from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import ResourcesHero, SectionTitles, CaseStudy, DownloadableResource

@admin.register(ResourcesHero)
class ResourcesHeroAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle')
    list_display_links = ('id', 'title')
    
    def has_add_permission(self, request):
        return ResourcesHero.objects.count() == 0

@admin.register(SectionTitles)
class SectionTitlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'case_studies_title', 'downloads_title')
    list_display_links = ('id',)
    list_editable = ('case_studies_title', 'downloads_title') # Direct Edit

    def has_add_permission(self, request):
        return SectionTitles.objects.count() == 0

@admin.register(CaseStudy)
class CaseStudyAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'title', 'client_name', 'result_stat', 'order')
    list_editable = ('title', 'client_name', 'result_stat', 'order') # Direct Edit
    list_display_links = ('id',)

@admin.register(DownloadableResource)
class DownloadableResourceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'title', 'resource_type', 'file_status', 'order')
    list_editable = ('title', 'resource_type', 'order') # Direct Edit
    list_display_links = ('id',)
    list_filter = ('resource_type',)

    def file_status(self, obj):
        return "✅ Uploaded" if obj.file else "❌ Missing"
    file_status.short_description = "File"