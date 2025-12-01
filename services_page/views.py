from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (
    ServiceHero, ServiceProcess, ServiceFeature, 
    ServiceTestimonial, ServiceFAQ, ServiceCTA
)
from .serializers import (
    ServiceHeroSerializer, ServiceProcessSerializer, ServiceFeatureSerializer, 
    ServiceTestimonialSerializer, ServiceFAQSerializer, ServiceCTASerializer
)
# CMS App se Service List laane ke liye
from cms.models import Service
from cms.serializers import ServiceSerializer

class ServicePageDataView(APIView):
    def get(self, request):
        hero = ServiceHero.objects.first()
        cta = ServiceCTA.objects.first()
        
        return Response({
            "hero": ServiceHeroSerializer(hero).data if hero else None,
            "process": ServiceProcessSerializer(ServiceProcess.objects.all(), many=True).data,
            "features": ServiceFeatureSerializer(ServiceFeature.objects.all(), many=True).data,
            "testimonials": ServiceTestimonialSerializer(ServiceTestimonial.objects.all(), many=True).data,
            "faq": ServiceFAQSerializer(ServiceFAQ.objects.all(), many=True).data,
            "cta": ServiceCTASerializer(cta).data if cta else None,
            
            # Actual Services List (Dynamic)
            "services_list": ServiceSerializer(Service.objects.all().order_by('order'), many=True).data
        })