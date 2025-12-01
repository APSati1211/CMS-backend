from rest_framework import serializers
from .models import BlogPost, BlogCategory

# --- 1. NEW: BlogCategory Serializer ---
class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['id', 'name', 'slug']

# --- 2. UPDATED: BlogPost Serializer ---
class BlogPostSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    # This will show the full category object (id, name, slug) instead of just the ID
    category = BlogCategorySerializer(read_only=True)
    
    # If you need to write to the category field using an ID, you might need a separate field or logic, 
    # but for reading/displaying, this is best.

    class Meta:
        model = BlogPost
        # Added 'category' to fields
        fields = ["id", "title", "slug", "short_description", "body", "image", "published", "created_at", "category"]