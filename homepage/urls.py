from django.urls import path
from .views import HomePageDataView

urlpatterns = [
    path('homepage-data/', HomePageDataView.as_view(), name='homepage-data'),
]