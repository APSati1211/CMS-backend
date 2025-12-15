from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Stakeholder, SolutionsPage
from .serializers import StakeholderSerializer, SolutionsPageSerializer

class StakeholderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stakeholder.objects.all()
    serializer_class = StakeholderSerializer

class SolutionsPageDataView(APIView):
    def get(self, request):
        # Fetch or create default page content
        page_content, created = SolutionsPage.objects.get_or_create(id=1)
        page_serializer = SolutionsPageSerializer(page_content)
        
        # Fetch all solution cards
        cards = Stakeholder.objects.all()
        cards_serializer = StakeholderSerializer(cards, many=True)

        return Response({
            "content": page_serializer.data,
            "solutions": cards_serializer.data
        })

# --- NEW VIEW FOR DETAIL PAGE ---
class SolutionDetailView(generics.RetrieveAPIView):
    queryset = Stakeholder.objects.all()
    serializer_class = StakeholderSerializer
    lookup_field = 'slug'  # We will find the solution by its slug, not ID