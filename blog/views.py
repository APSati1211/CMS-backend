from rest_framework import viewsets
from rest_framework import filters
from .models import BlogPost, BlogCategory
from .serializers import BlogPostSerializer, BlogCategorySerializer

# --- 1. CATEGORY VIEWSET ---
class BlogCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogCategory.objects.all().order_by('name')
    serializer_class = BlogCategorySerializer

# --- 2. BLOG POST VIEWSET ---
class BlogPostViewSet(viewsets.ModelViewSet):
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'  # <--- NEW: Allows fetching single post by slug
    
    # --- Enable Search ---
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'short_description', 'body'] 

    def get_queryset(self):
        # Base queryset to fetch all published blogs, ordered by date
        queryset = BlogPost.objects.filter(published=True).order_by("-created_at")
        
        # Filtering
        category_slug = self.request.query_params.get('category')
        
        if category_slug and category_slug != 'all':
            queryset = queryset.filter(category__slug=category_slug)
        
        return queryset