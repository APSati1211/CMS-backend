from rest_framework.views import APIView
from rest_framework.response import Response
from .models import HeroSection, Stat, Feature, BottomCTA
from .serializers import HeroSerializer, StatSerializer, FeatureSerializer, BottomCTASerializer

class HomePageDataView(APIView):
    def get(self, request):
        return Response({
            "hero": HeroSerializer(HeroSection.objects.first()).data if HeroSection.objects.exists() else None,
            "stats": StatSerializer(Stat.objects.all(), many=True).data,
            "features": FeatureSerializer(Feature.objects.all(), many=True).data,
            "cta": BottomCTASerializer(BottomCTA.objects.first()).data if BottomCTA.objects.exists() else None,
        })