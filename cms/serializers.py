from rest_framework import serializers
from .models import SiteContent, CaseStudy, Resource, Service # <--- Service Added

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

class ServiceSerializer(serializers.ModelSerializer): # <--- NEW SERIALIZER
    class Meta:
        model = Service
        fields = '__all__'