from django.contrib import admin
from .models import AboutPage, TeamMember, Award

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    # Sirf 1 record allow karein taaki user confuse na ho
    def has_add_permission(self, request):
        # Agar 1 record already hai, toh naya add mat karne do
        return AboutPage.objects.count() == 0

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'order')
    list_editable = ('order',)

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('title', 'year')