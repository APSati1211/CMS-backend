from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

# Existing imports
from cms.views import SiteContentViewSet, home_page_content, CaseStudyViewSet, ResourceViewSet, ServiceViewSet, PageViewSet # <--- Added PageViewSet
from blog.views import BlogPostViewSet
from leads.views import LeadViewSet, NewsletterSubscriberViewSet, chat_with_ai
from contact.views import ContactViewSet
from careers.views import JobOpeningViewSet, JobApplicationViewSet

# Router Setup
router = DefaultRouter()
router.register(r"sitecontent", SiteContentViewSet, basename="sitecontent")
router.register(r"blogs", BlogPostViewSet, basename="blog")
router.register(r"leads", LeadViewSet, basename="lead")
router.register(r"contact", ContactViewSet, basename="contact")

# New Routes for Proposal Features
router.register(r"jobs", JobOpeningViewSet, basename="jobs")
router.register(r"apply", JobApplicationViewSet, basename="apply")
router.register(r"case-studies", CaseStudyViewSet, basename="casestudies")
router.register(r"resources", ResourceViewSet, basename="resources")
router.register(r"services", ServiceViewSet, basename="services")
router.register(r"newsletter", NewsletterSubscriberViewSet, basename="newsletter")
router.register(r"pages", PageViewSet, basename="pages") # <--- NEW ROUTE ADDED

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/chat-ai/", chat_with_ai),
    path("api/", include("theme.urls")),
    path("api/home-page-content/", home_page_content),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)