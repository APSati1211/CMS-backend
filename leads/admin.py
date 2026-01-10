import csv
from django.http import HttpResponse
from django.contrib import admin
from django.utils.html import format_html
from .models import Lead, ChatbotLead, WebsiteLead, NewsletterSubscriber, LeadShareHistory

# --- CSV Export Action ---
def export_to_csv(modeladmin, request, queryset):
    meta = modeladmin.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={meta}.csv'
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response

export_to_csv.short_description = "Export Selected to CSV"

# --- CHATBOT LEAD ---
@admin.register(ChatbotLead)
class ChatbotLeadAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "display_service", "display_date")
    search_fields = ("name", "email", "phone")
    list_filter = ("service", "created_at")
    actions = [export_to_csv]

    @admin.display(description='Service')
    def display_service(self, obj):
        return format_html('<b style="color:#1565c0">{}</b>', obj.service or "-")

    @admin.display(description='Date')
    def display_date(self, obj):
        return obj.created_at.strftime("%d %b %Y, %H:%M")

# --- WEBSITE LEAD ---
@admin.register(WebsiteLead)
class WebsiteLeadAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "company", "service", "created_at")
    search_fields = ("name", "email", "company")
    actions = [export_to_csv]

# --- ALL LEADS ---
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "source", "service", "created_at")
    list_filter = ("source", "created_at")
    actions = [export_to_csv]

# --- NEWSLETTER ---
@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    actions = [export_to_csv]

# --- SHARE HISTORY (New) ---
@admin.register(LeadShareHistory)
class LeadShareHistoryAdmin(admin.ModelAdmin):
    list_display = ('lead', 'recipient_name', 'recipient_phone', 'shared_by', 'shared_at')
    list_filter = ('shared_at', 'platform')