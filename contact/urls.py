from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, ContactPageDataView

router = DefaultRouter()
router.register(r"contact", ContactViewSet, basename="contact")

urlpatterns = [
    path('contact-page-data/', ContactPageDataView.as_view(), name='contact-page-data'),
] + router.urls