from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AboutPage, TeamMember, Award, TechStack
from .serializers import AboutPageSerializer, TeamMemberSerializer, AwardSerializer, TechStackSerializer

class AboutPageDataView(APIView):
    def get(self, request):
        about_content = AboutPage.objects.first()
        team_members = TeamMember.objects.all()
        awards = Award.objects.all()
        tech_stack = TechStack.objects.all() # <--- Fetch Data

        return Response({
            "content": AboutPageSerializer(about_content).data if about_content else None,
            "team": TeamMemberSerializer(team_members, many=True).data,
            "awards": AwardSerializer(awards, many=True).data,
            "tech_stack": TechStackSerializer(tech_stack, many=True).data # <--- Add to Response
        })