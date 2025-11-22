from django.db import models

class ThemeSetting(models.Model):
    name = models.CharField(max_length=100, default="Default Theme")
    
    # --- EXISTING FIELDS ---
    logo = models.ImageField(upload_to='site_config/', blank=True, null=True, help_text="Upload a transparent PNG logo for Header & Footer")
    light_primary_color = models.CharField(max_length=7, default='#10B981')
    light_secondary_color = models.CharField(max_length=7, default='#F59E0B')
    light_accent_color = models.CharField(max_length=7, default='#059669')
    light_background_color = models.CharField(max_length=7, default='#FFFFFF')
    light_text_color = models.CharField(max_length=7, default='#1F2937')
    dark_primary_color = models.CharField(max_length=7, default='#34D399')
    dark_secondary_color = models.CharField(max_length=7, default='#FBBF24')
    dark_accent_color = models.CharField(max_length=7, default='#10B981')
    dark_background_color = models.CharField(max_length=7, default='#111827')
    dark_text_color = models.CharField(max_length=7, default='#F3F4F6')

    # --- NEW DYNAMIC FIELDS (Footer & Chatbot) ---
    chatbot_welcome_message = models.TextField(
        default="👋 Hi! I’m XpertAI Assistant. How can I help you today?",
        help_text="Initial message shown by the chatbot."
    )
    contact_phone = models.CharField(max_length=20, default="+91 98765 43210", help_text="Phone number for Header/Footer")
    contact_email = models.EmailField(default="hello@xpertai.global", help_text="Email address for Header/Footer")
    
    # Social Media Links
    facebook_url = models.URLField(blank=True, help_text="Facebook URL")
    twitter_url = models.URLField(blank=True, help_text="Twitter/X URL")
    linkedin_url = models.URLField(blank=True, help_text="LinkedIn URL")
    instagram_url = models.URLField(blank=True, help_text="Instagram URL")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Theme Settings"