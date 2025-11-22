from django.contrib import admin
from .models import ThemeSetting

@admin.register(ThemeSetting)
class ThemeAdmin(admin.ModelAdmin):
    """
    Admin interface for managing the website's theme settings.
    """
    def has_add_permission(self, request):
        # Prevent adding new Theme if one already exists
        return not ThemeSetting.objects.exists()
