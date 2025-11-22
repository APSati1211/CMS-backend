from rest_framework import serializers
from .models import ThemeSetting

class ThemeSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThemeSetting
        fields = [
            'name', 'logo',
            'chatbot_welcome_message',
            'contact_phone', 'contact_email',
            'facebook_url', 'twitter_url', 'linkedin_url', 'instagram_url',
            'light_primary_color', 'light_secondary_color',
            'light_accent_color', 'light_background_color', 'light_text_color',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['primary_color'] = representation.pop('light_primary_color')
        representation['secondary_color'] = representation.pop('light_secondary_color')
        representation['accent_color'] = representation.pop('light_accent_color')
        representation['background_color'] = representation.pop('light_background_color')
        representation['text_color'] = representation.pop('light_text_color')
        return representation