from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (
    HomePageContent, TrustedClient, Stat, 
    ProcessStep, Feature, Testimonial, FAQ
)
from cms.models import Service, CaseStudy # <--- Import from CMS app
from .serializers import (
    HomePageContentSerializer, TrustedClientSerializer, StatSerializer,
    ProcessStepSerializer, FeatureSerializer, TestimonialSerializer, FAQSerializer
)
from cms.serializers import ServiceSerializer, CaseStudySerializer # <--- Import Serializers

class HomePageDataView(APIView):
    def get(self, request):
        content = HomePageContent.objects.first()
        
        return Response({
            "content": HomePageContentSerializer(content).data if content else None,
            "clients": TrustedClientSerializer(TrustedClient.objects.all(), many=True).data,
            "stats": StatSerializer(Stat.objects.all(), many=True).data,
            "process": ProcessStepSerializer(ProcessStep.objects.all(), many=True).data,
            "features": FeatureSerializer(Feature.objects.all(), many=True).data,
            "testimonials": TestimonialSerializer(Testimonial.objects.all(), many=True).data,
            "faq": FAQSerializer(FAQ.objects.all(), many=True).data,
            # --- NEW DATA FOR HOME PAGE STRUCTURE ---
            "services": ServiceSerializer(Service.objects.all()[:6], many=True).data, # Top 6 Services
            "case_studies": CaseStudySerializer(CaseStudy.objects.all()[:3], many=True).data, # Top 3 Case Studies
        })