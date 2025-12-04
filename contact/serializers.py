from rest_framework import serializers
from .models import ContactMessage, ContactPage, OfficeAddress

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = "__all__"

class OfficeAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeAddress
        fields = "__all__"

class ContactPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPage
        fields = "__all__"