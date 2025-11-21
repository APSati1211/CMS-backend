from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import SiteContent, Page

@admin.register(Page)
class PageAdmin(SortableAdminMixin, admin.ModelAdmin):
    """
    Admin configuration for the Page model with drag-and-drop ordering.
    """
    list_display = ('title', 'slug')
    search_fields = ('title', 'slug')
    ordering = ('page_order',)

@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    """
    Admin configuration for the SiteContent model.
    """
    list_display = ('page', 'section', 'title', 'updated_at')
    list_filter = ('page',)
    search_fields = ('title', 'content', 'section')
    list_editable = ('section', 'title',)
    ordering = ('page', 'section')
    save_on_top = True
    readonly_fields = ('updated_at',)