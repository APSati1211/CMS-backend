from django.contrib import admin
from django.utils.html import format_html
from .models import Lead, ChatbotLead, WebsiteLead, NewsletterSubscriber

# --- 1. CHATBOT LEAD ADMIN (Customized) ---
@admin.register(ChatbotLead)
class ChatbotLeadAdmin(admin.ModelAdmin):
    # Ye wo columns hain jo list mein dikhenge
    list_display = (
        "name", 
        "email", 
        "phone", 
        "display_service",   # Interested Service
        "display_message",   # Message
        "display_date"       # Received On
    )
    
    # In fields par search kaam karega
    search_fields = ("name", "email", "phone", "service")
    
    # Side mein filter karne ka option
    list_filter = ("service", "created_at")
    
    # Nayi leads sabse upar
    ordering = ("-created_at",)
    
    # Detail page ke liye fields (Read-only)
    readonly_fields = ("created_at", "source", "message")

    # --- Custom Column Logic ---

    def get_queryset(self, request):
        """Sirf Chatbot wali leads filter karega"""
        return super().get_queryset(request).filter(source='chatbot')

    @admin.display(description='Interested Service')
    def display_service(self, obj):
        """Service column ko color aur format karega"""
        if not obj.service:
            return "-"
        return format_html(
            '<span style="color: #1565c0; font-weight: bold;">{}</span>',
            obj.service
        )

    @admin.display(description='Message')
    def display_message(self, obj):
        """Lamba message ho to shuruwat dikhaye, detail mein pura dikhega"""
        if obj.message and len(obj.message) > 50:
            return obj.message[:50] + "..."
        return obj.message

    @admin.display(description='Received On')
    def display_date(self, obj):
        """Date ko sahi format mein dikhaye (e.g., 12 Dec 2025, 14:30)"""
        return obj.created_at.strftime("%d %b %Y, %H:%M")


# --- 2. WEBSITE LEAD ADMIN ---
@admin.register(WebsiteLead)
class WebsiteLeadAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "email", "service", "created_at") 
    list_filter = ("service", "created_at")
    search_fields = ("name", "email", "company")
    readonly_fields = ("created_at", "source")
    ordering = ("-created_at",)

    def get_queryset(self, request):
        return super().get_queryset(request).filter(source='website')


# --- 3. ALL LEADS (Main Model) ---
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "source", "created_at")
    list_filter = ("source", "created_at")
    search_fields = ("name", "email")
    ordering = ("-created_at",)


# --- 4. NEWSLETTER SUBSCRIBERS ---
@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)
    ordering = ('-subscribed_at',)