from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AboutPage, TeamMember, Award
from .serializers import AboutPageSerializer, TeamMemberSerializer, AwardSerializer

class AboutPageDataView(APIView):
    def get(self, request):
        about_content = AboutPage.objects.first()
        team_members = TeamMember.objects.all()
        awards = Award.objects.all()

        return Response({
            "content": AboutPageSerializer(about_content).data if about_content else None,
            "team": TeamMemberSerializer(team_members, many=True).data,
            "awards": AwardSerializer(awards, many=True).data
        })