from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import CareersPage, Benefit, JobOpening, JobApplication
from .serializers import (
    CareersPageSerializer, BenefitSerializer, 
    JobOpeningSerializer, JobApplicationSerializer
)

class CareersPageDataView(APIView):
    def get(self, request):
        content = CareersPage.objects.first()
        return Response({
            "content": CareersPageSerializer(content).data if content else None,
            "benefits": BenefitSerializer(Benefit.objects.all(), many=True).data,
            "jobs": JobOpeningSerializer(JobOpening.objects.filter(is_active=True).order_by('-created_at'), many=True).data
        })

# --- ViewSets for CRUD Operations (Used by Admin/Forms) ---

class JobOpeningViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only endpoint for fetching job listings.
    """
    queryset = JobOpening.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = JobOpeningSerializer

class JobApplicationViewSet(viewsets.ModelViewSet):
    """
    Endpoint for submitting job applications.
    """
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer