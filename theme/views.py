from rest_framework import generics
from .models import ThemeSetting
from .serializers import ThemeSettingSerializer

class ThemeSettingDetail(generics.RetrieveAPIView):
    queryset = ThemeSetting.objects.all()
    serializer_class = ThemeSettingSerializer

    def get_object(self):
        return ThemeSetting.objects.first()
