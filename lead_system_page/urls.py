from django.urls import path
from .views import LeadSystemPageDataView

urlpatterns = [
    path('lead-system-data/', LeadSystemPageDataView.as_view(), name='lead-system-data'),
]