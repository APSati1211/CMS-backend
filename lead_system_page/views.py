from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LSHero, LSFeature, LSBottomCTA, LSDashboard
from .serializers import LSHeroSerializer, LSFeatureSerializer, LSBottomCTASerializer, LSDashboardSerializer

class LeadSystemPageDataView(APIView):
    def get(self, request):
        return Response({
            "hero": LSHeroSerializer(LSHero.objects.first()).data if LSHero.objects.exists() else None,
            "features": LSFeatureSerializer(LSFeature.objects.all(), many=True).data,
            # --- NEW DATA FIELD ---
            "dashboard": LSDashboardSerializer(LSDashboard.objects.first()).data if LSDashboard.objects.exists() else None,
            "cta": LSBottomCTASerializer(LSBottomCTA.objects.first()).data if LSBottomCTA.objects.exists() else None,
        })