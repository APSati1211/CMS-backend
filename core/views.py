from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.parsers import MultiPartParser, FormParser 
from .serializers import UserRegistrationSerializer, UserProfileSerializer
from .models import UserProfile

@api_view(['GET'])
@permission_classes([AllowAny])
def home(request):
    return Response({"message": "Welcome to XpertAI API System", "status": "Running"})

class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "User registered successfully!",
                "user_id": user.id,
                "username": user.username,
                "role": request.data.get('role', 'client')
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        
        role = "client"
        if hasattr(user, 'profile'):
            role = user.profile.role
        elif hasattr(user, 'client_profile'):
            role = 'client'
        elif hasattr(user, 'professional_profile'):
            role = 'professional'

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'role': role
        })

class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    Standard Profile View (Stats Removed)
    """
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_object(self):
        # Automatically get profile for current user
        profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        return profile