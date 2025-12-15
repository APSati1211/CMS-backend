from django.db import models
from django.utils.text import slugify

class Stakeholder(models.Model):
    title = models.CharField(max_length=100)
    
    # 🔥 CHANGE: added null=True to fix the unique constraint error
    slug = models.SlugField(
        unique=True, 
        blank=True, 
        null=True,  # <--- Ye zaroori hai abhi ke liye
        help_text="Unique URL identifier (auto-generated from title)"
    )
    
    description = models.TextField(help_text="Short description for the card")
    long_description = models.TextField(blank=True, help_text="Detailed content for the new page") 
    icon_name = models.CharField(max_length=50, default="Users", help_text="Lucide Icon Name")
    image = models.ImageField(upload_to="stakeholders/", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Solution Card"
        verbose_name_plural = "Solution Cards"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# SolutionsPage model same rahega...
class SolutionsPage(models.Model):
    # ... (No changes needed here)
    hero_title = models.CharField(max_length=200, default="Our Solutions")
    hero_subtitle = models.TextField(default="Tailored ecosystems for every stakeholder in the financial world.")
    cta_title = models.CharField(max_length=200, default="Ready to join the ecosystem?")
    cta_text = models.TextField(default="Whether you are a client looking for experts or a professional seeking work, XpertAI has a place for you.")
    cta_btn_primary = models.CharField(max_length=50, default="Sign Up Now")
    cta_btn_secondary = models.CharField(max_length=50, default="Contact Sales")
    
    class Meta:
        verbose_name = "Solutions Page Content"
        verbose_name_plural = "Solutions Page Content"

    def __str__(self):
        return "Solutions Page Settings"