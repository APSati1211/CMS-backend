from django.urls import path
from .views import ThemeSettingDetail

urlpatterns = [
    # Frontend is endpoint par request karega: /api/theme-settings/
    path('theme-settings/', ThemeSettingDetail.as_view(), name='theme-settings'),
]