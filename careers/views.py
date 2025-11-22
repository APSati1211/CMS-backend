from rest_framework import viewsets
from .models import JobOpening, JobApplication
from .serializers import JobOpeningSerializer, JobApplicationSerializer

class JobOpeningViewSet(viewsets.ReadOnlyModelViewSet): # Sirf read kar sakte hain frontend se
    queryset = JobOpening.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = JobOpeningSerializer

class JobApplicationViewSet(viewsets.ModelViewSet): # Apply kar sakte hain
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer