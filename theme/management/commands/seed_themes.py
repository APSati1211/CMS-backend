from django.core.management.base import BaseCommand
from theme.models import ThemeSetting

class Command(BaseCommand):
    help = 'Seeds the database with predefined professional themes.'

    def handle(self, *args, **kwargs):
        self.stdout.write('🎨 Seeding Themes...')

        themes_data = [
            {
                "name": "XpertAI Corporate (Default)",
                # Light Mode (Professional Blue & Teal)
                "light_primary_color": "#2563EB",    # Blue 600
                "light_secondary_color": "#0F172A",  # Slate 900
                "light_accent_color": "#0D9488",     # Teal 600
                "light_background_color": "#FFFFFF",
                "light_text_color": "#1F2937",       # Gray 800
                # Dark Mode
                "dark_primary_color": "#3B82F6",     # Blue 500
                "dark_secondary_color": "#F8FAFC",   # Slate 50
                "dark_accent_color": "#14B8A6",      # Teal 500
                "dark_background_color": "#0F172A",
                "dark_text_color": "#F3F4F6",
            },
            {
                "name": "FinTech Green (Trust & Money)",
                # Light Mode (Emerald & Gold)
                "light_primary_color": "#059669",    # Emerald 600
                "light_secondary_color": "#064E3B",  # Emerald 900
                "light_accent_color": "#D97706",     # Amber 600
                "light_background_color": "#F0FDF4", # Light Mint
                "light_text_color": "#064E3B",
                # Dark Mode
                "dark_primary_color": "#10B981",     # Emerald 500
                "dark_secondary_color": "#ECFDF5",
                "dark_accent_color": "#F59E0B",      # Amber 500
                "dark_background_color": "#064E3B",
                "dark_text_color": "#ECFDF5",
            },
            {
                "name": "Innovation Purple (SaaS/Tech)",
                # Light Mode (Violet & Pink)
                "light_primary_color": "#7C3AED",    # Violet 600
                "light_secondary_color": "#4C1D95",  # Violet 900
                "light_accent_color": "#DB2777",     # Pink 600
                "light_background_color": "#FFFFFF",
                "light_text_color": "#111827",
                # Dark Mode
                "dark_primary_color": "#8B5CF6",     # Violet 500
                "dark_secondary_color": "#F5F3FF",
                "dark_accent_color": "#EC4899",      # Pink 500
                "dark_background_color": "#2E1065",
                "dark_text_color": "#F5F3FF",
            },
            {
                "name": "Sunset Warmth (Creative)",
                # Light Mode (Orange & Red)
                "light_primary_color": "#EA580C",    # Orange 600
                "light_secondary_color": "#7C2D12",  # Orange 900
                "light_accent_color": "#DC2626",     # Red 600
                "light_background_color": "#FFF7ED", # Light Orange
                "light_text_color": "#431407",
                # Dark Mode
                "dark_primary_color": "#F97316",     # Orange 500
                "dark_secondary_color": "#FFEDD5",
                "dark_accent_color": "#EF4444",      # Red 500
                "dark_background_color": "#431407",
                "dark_text_color": "#FFEDD5",
            },
            {
                "name": "Midnight Charcoal (Minimalist)",
                # Light Mode (Black & White)
                "light_primary_color": "#18181B",    # Zinc 900
                "light_secondary_color": "#52525B",  # Zinc 600
                "light_accent_color": "#2563EB",     # Blue 600
                "light_background_color": "#FFFFFF",
                "light_text_color": "#000000",
                # Dark Mode
                "dark_primary_color": "#E4E4E7",     # Zinc 200
                "dark_secondary_color": "#A1A1AA",   # Zinc 400
                "dark_accent_color": "#60A5FA",      # Blue 400
                "dark_background_color": "#000000",
                "dark_text_color": "#FFFFFF",
            }
        ]

        for data in themes_data:
            theme_name = data.pop("name")
            obj, created = ThemeSetting.objects.update_or_create(
                name=theme_name,
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✅ Created theme: {theme_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'🔄 Updated theme: {theme_name}'))

        self.stdout.write(self.style.SUCCESS('🎉 All themes seeded successfully!'))