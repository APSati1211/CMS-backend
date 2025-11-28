from rest_framework import viewsets
from .models import Stakeholder
from .serializers import StakeholderSerializer

class StakeholderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stakeholder.objects.all()
    serializer_class = StakeholderSerializer