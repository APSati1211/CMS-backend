from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin
from .models import Stakeholder

@admin.register(Stakeholder)
class StakeholderAdmin(SortableAdminMixin, admin.ModelAdmin):
    # ID shuru mein dikhegi, jis par click karke full edit khulega
    list_display = ('id', 'title', 'icon_preview', 'desc_preview', 'order')
    
    # Ye fields seedhe list mein edit ho jayenge
    list_editable = ('title', 'order') 
    
    # ID par click karne se form khulega
    list_display_links = ('id',)
    
    search_fields = ('title', 'description')

    # Description ka chhota preview dikhane ke liye function
    def desc_preview(self, obj):
        return obj.description[:75] + "..." if obj.description else "-"
    desc_preview.short_description = "Description"

    # Icon/Image ka preview dikhane ke liye function
    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<img src="{}" style="width: 40px; height: 40px; object-fit: contain;" />', obj.icon.url)
        return "❌ No Icon"
    icon_preview.short_description = "Icon"