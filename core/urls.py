from django.urls import path
from . import views
from .views import RegisterView, CustomLoginView, UserProfileView # Import new view

urlpatterns = [
    path('', views.home, name='home'),
    
    # --- Authentication APIs ---
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', CustomLoginView.as_view(), name='login'),
    
    # --- NEW: Profile API ---
    path('api/profile/', UserProfileView.as_view(), name='user-profile'),
]