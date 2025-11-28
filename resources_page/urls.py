from django.urls import path
from .views import ResourcesPageDataView

urlpatterns = [
    path('resources-page-data/', ResourcesPageDataView.as_view(), name='resources-page-data'),
]