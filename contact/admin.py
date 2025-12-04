from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import ContactMessage, ContactPage, OfficeAddress

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email", "message")
    readonly_fields = ("created_at",)

@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return ContactPage.objects.count() == 0

@admin.register(OfficeAddress)
class OfficeAddressAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'email', 'order')