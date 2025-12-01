from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CareersPageDataView, JobApplicationViewSet

router = DefaultRouter()
# Ideally, apply route is registered in the main backend/urls.py router, 
# but if you want it app-specific, you can keep it here.
# router.register(r'apply', JobApplicationViewSet) 

urlpatterns = [
    path('careers-page-data/', CareersPageDataView.as_view(), name='careers-page-data'),
] 
# + router.urls  <-- If you registered routes above