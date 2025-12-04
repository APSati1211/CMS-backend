from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserRegistrationSerializer

# --- MISSING VIEW ADDED HERE ---
@api_view(['GET'])
@permission_classes([AllowAny])
def home(request):
    """
    Basic API Root view to prevent 404 on localhost:8000/
    """
    return Response({
        "message": "Welcome to XpertAI API System",
        "status": "Running"
    })

# --- EXISTING VIEWS ---
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
        
        # Determine User Role
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