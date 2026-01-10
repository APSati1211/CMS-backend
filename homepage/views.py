from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import (
    HomePageContent, TrustedClient, Stat, 
    ProcessStep, Feature, Testimonial, FAQ
)
from cms.models import Service, CaseStudy 
from .serializers import (
    HomePageContentSerializer, TrustedClientSerializer, StatSerializer,
    ProcessStepSerializer, FeatureSerializer, TestimonialSerializer, FAQSerializer
)
from cms.serializers import ServiceSerializer, CaseStudySerializer 

# --- 1. Aggregated Data View (For Public Home Page) ---
class HomePageDataView(APIView):
    def get(self, request):
        # Ensure at least one content object exists
        content, created = HomePageContent.objects.get_or_create(id=1)
        
        return Response({
            "content": HomePageContentSerializer(content).data,
            "clients": TrustedClientSerializer(TrustedClient.objects.all(), many=True).data,
            "stats": StatSerializer(Stat.objects.all(), many=True).data,
            "process": ProcessStepSerializer(ProcessStep.objects.all(), many=True).data,
            "features": FeatureSerializer(Feature.objects.all(), many=True).data,
            "testimonials": TestimonialSerializer(Testimonial.objects.all(), many=True).data,
            "faq": FAQSerializer(FAQ.objects.all(), many=True).data,
            # Data from other apps
            "services": ServiceSerializer(Service.objects.all()[:6], many=True).data, 
            "case_studies": CaseStudySerializer(CaseStudy.objects.all()[:3], many=True).data, 
        })

# --- 2. Admin CRUD ViewSets ---

class HomePageContentViewSet(viewsets.ModelViewSet):
    queryset = HomePageContent.objects.all()
    serializer_class = HomePageContentSerializer

class TrustedClientViewSet(viewsets.ModelViewSet):
    queryset = TrustedClient.objects.all()
    serializer_class = TrustedClientSerializer

class StatViewSet(viewsets.ModelViewSet):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer

class ProcessStepViewSet(viewsets.ModelViewSet):
    queryset = ProcessStep.objects.all()
    serializer_class = ProcessStepSerializer

class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer