from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ResourcesHero, SectionTitles, CaseStudy, DownloadableResource
from .serializers import (
    ResourcesHeroSerializer, SectionTitlesSerializer, 
    CaseStudySerializer, DownloadableResourceSerializer
)

class ResourcesPageDataView(APIView):
    def get(self, request):
        return Response({
            "hero": ResourcesHeroSerializer(ResourcesHero.objects.first()).data if ResourcesHero.objects.exists() else None,
            "titles": SectionTitlesSerializer(SectionTitles.objects.first()).data if SectionTitles.objects.exists() else None,
            "case_studies": CaseStudySerializer(CaseStudy.objects.all(), many=True).data,
            "downloads": DownloadableResourceSerializer(DownloadableResource.objects.all(), many=True).data,
        })