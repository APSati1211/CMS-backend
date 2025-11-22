from rest_framework import serializers
from .models import Lead, NewsletterSubscriber  # <--- Updated Import

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = "__all__"

# --- NEW SERIALIZER ---
class NewsletterSubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscriber
        fields = '__all__'