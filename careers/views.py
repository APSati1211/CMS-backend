from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CareersPage, Benefit, JobOpening, JobApplication, EmployeeTestimonial
from .serializers import (
    CareersPageSerializer, BenefitSerializer, 
    JobOpeningSerializer, JobApplicationSerializer, EmployeeTestimonialSerializer
)

# --- 1. Public Data View (Read Only) ---
class CareersPageDataView(APIView):
    def get(self, request):
        # Use get_or_create to prevent "NoneType" errors on frontend
        content, created = CareersPage.objects.get_or_create(id=1)
        
        return Response({
            "content": CareersPageSerializer(content).data,
            "benefits": BenefitSerializer(Benefit.objects.all(), many=True).data,
            "testimonials": EmployeeTestimonialSerializer(EmployeeTestimonial.objects.all(), many=True).data,
            # Show only active jobs to the public
            "jobs": JobOpeningSerializer(JobOpening.objects.filter(is_active=True).order_by('-created_at'), many=True).data
        })

# --- 2. Admin CRUD ViewSets (Editable) ---

class CareersPageViewSet(viewsets.ModelViewSet):
    """
    For editing Hero, Culture, and Text sections.
    """
    queryset = CareersPage.objects.all()
    serializer_class = CareersPageSerializer

class BenefitViewSet(viewsets.ModelViewSet):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer

class EmployeeTestimonialViewSet(viewsets.ModelViewSet):
    queryset = EmployeeTestimonial.objects.all()
    serializer_class = EmployeeTestimonialSerializer

class JobOpeningViewSet(viewsets.ModelViewSet):
    """
    Changed to ModelViewSet so Admin can Create/Update/Delete jobs.
    Admin sees ALL jobs (Active & Inactive).
    """
    queryset = JobOpening.objects.all().order_by('-created_at')
    serializer_class = JobOpeningSerializer

class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer