from django.urls import path
from .views import AboutPageDataView

urlpatterns = [
    path('', AboutPageDataView.as_view(), name='about-page-data'),
]