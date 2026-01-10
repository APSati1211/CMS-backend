from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ContactViewSet, 
    ContactPageDataView, 
    ContactPageViewSet, 
    OfficeAddressViewSet, 
    ContactMessageViewSet, 
    TicketViewSet
)

router = DefaultRouter()

# Admin Endpoints (prefixed by api/contact/)
router.register(r'contact-content', ContactPageViewSet)   # api/contact/contact-content/
router.register(r'office-addresses', OfficeAddressViewSet) # api/contact/office-addresses/
router.register(r'messages', ContactMessageViewSet)       # api/contact/messages/
router.register(r'tickets', TicketViewSet)                # api/contact/tickets/

# Public Form Endpoint (must be last to avoid overriding others if using regex)
# This maps 'api/contact/' (POST) to the ContactViewSet
router.register(r'', ContactViewSet, basename="public-contact")

urlpatterns = [
    # Public Page Data
    path('page-data/', ContactPageDataView.as_view(), name='contact-page-data'),
    
    # Router URLs
    path('', include(router.urls)),
]