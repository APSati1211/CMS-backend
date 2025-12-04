from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (
    ResourcesHero, SectionTitles, CaseStudy, 
    DownloadableResource, UsefulLink
)
from .serializers import (
    ResourcesHeroSerializer, SectionTitlesSerializer, CaseStudySerializer,
    DownloadableResourceSerializer, UsefulLinkSerializer
)
# --- Import Blog Models & Serializers ---
from blog.models import BlogPost
from blog.serializers import BlogPostSerializer

class ResourcesPageDataView(APIView):
    def get(self, request):
        # Fetch latest 4 published blogs
        latest_blogs = BlogPost.objects.filter(published=True).order_by('-created_at')[:4]

        return Response({
            "hero": ResourcesHeroSerializer(ResourcesHero.objects.first()).data if ResourcesHero.objects.exists() else None,
            "titles": SectionTitlesSerializer(SectionTitles.objects.first()).data if SectionTitles.objects.exists() else None,
            
            # --- 1. BLOGS (Latest 4) ---
            "latest_blogs": BlogPostSerializer(latest_blogs, many=True).data,

            # --- 2. CASE STUDIES ---
            "case_studies": CaseStudySerializer(CaseStudy.objects.all(), many=True).data,
            
            # --- 3. TEMPLATES (Downloads) ---
            "downloads": DownloadableResourceSerializer(DownloadableResource.objects.all(), many=True).data,
            
            # --- 4. USEFUL LINKS ---
            "useful_links": UsefulLinkSerializer(UsefulLink.objects.all(), many=True).data 
        })