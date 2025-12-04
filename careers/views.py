from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import CareersPage, Benefit, JobOpening, JobApplication, EmployeeTestimonial
from .serializers import (
    CareersPageSerializer, BenefitSerializer, 
    JobOpeningSerializer, JobApplicationSerializer, EmployeeTestimonialSerializer
)

class CareersPageDataView(APIView):
    def get(self, request):
        content = CareersPage.objects.first()
        return Response({
            "content": CareersPageSerializer(content).data if content else None,
            "benefits": BenefitSerializer(Benefit.objects.all(), many=True).data,
            "testimonials": EmployeeTestimonialSerializer(EmployeeTestimonial.objects.all(), many=True).data, # <--- Added
            "jobs": JobOpeningSerializer(JobOpening.objects.filter(is_active=True).order_by('-created_at'), many=True).data
        })

class JobOpeningViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = JobOpening.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = JobOpeningSerializer

class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer