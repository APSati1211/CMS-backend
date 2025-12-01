from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ResourcesHero, SectionTitles, CaseStudy, DownloadableResource
from .serializers import (
    ResourcesHeroSerializer, SectionTitlesSerializer, 
    CaseStudySerializer, DownloadableResourceSerializer
)

class ResourcesPageDataView(APIView):
    def get(self, request):
        hero = ResourcesHero.objects.first()
        titles = SectionTitles.objects.first()
        
        return Response({
            "hero": ResourcesHeroSerializer(hero).data if hero else None,
            "titles": SectionTitlesSerializer(titles).data if titles else None,
            "case_studies": CaseStudySerializer(CaseStudy.objects.all(), many=True).data,
            "downloads": DownloadableResourceSerializer(DownloadableResource.objects.all(), many=True).data,
        })