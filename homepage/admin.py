from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import HeroSection, Stat, Feature, BottomCTA

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cta_text', 'subtitle_preview')
    list_display_links = ('id', 'title')
    
    def subtitle_preview(self, obj):
        return obj.subtitle[:50] + "..." if obj.subtitle else ""
    subtitle_preview.short_description = "Subtitle"

    def has_add_permission(self, request):
        # Only allow 1 Hero Section
        return HeroSection.objects.count() == 0

@admin.register(Stat)
class StatAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'label', 'value', 'order')
    list_editable = ('label', 'value', 'order') # Direct Edit
    list_display_links = ('id',) # Click ID to open full form

@admin.register(Feature)
class FeatureAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'title', 'icon_name', 'desc_preview', 'order')
    list_editable = ('title', 'icon_name', 'order') # Direct Edit
    list_display_links = ('id',)

    def desc_preview(self, obj):
        return obj.description[:50] + "..."
    desc_preview.short_description = "Description"

@admin.register(BottomCTA)
class BottomCTAAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'button_text')
    list_display_links = ('id', 'title')

    def has_add_permission(self, request):
        return BottomCTA.objects.count() == 0