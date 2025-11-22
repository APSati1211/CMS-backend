from django.contrib import admin
from .models import Lead, ChatbotLead, WebsiteLead, NewsletterSubscriber  # <--- Updated Import

@admin.register(ChatbotLead)
class ChatbotLeadAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "service", "created_at")
    search_fields = ("name", "email", "service")
    list_filter = ("service",)

@admin.register(WebsiteLead)
class WebsiteLeadAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "email", "phone", "created_at")
    search_fields = ("name", "email", "company")

# --- NEW ADMIN ---
@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)