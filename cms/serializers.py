from rest_framework import serializers
from .models import SiteContent, CaseStudy, Resource, Service, ServiceSubService, Page

class SiteContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteContent
        fields = ['id', 'page', 'section', 'title', 'content', 'image', 'updated_at']

class CaseStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseStudy
        fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'

# --- SERVICE SERIALIZERS ---

class ServiceSubServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceSubService
        fields = ['id', 'title', 'description', 'order']

class ServiceSerializer(serializers.ModelSerializer):
    # This will automatically include the sub-services array in the JSON response
    sub_services = ServiceSubServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = '__all__'

# --- PAGE SERIALIZER (For Navbar/SEO) ---
class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'