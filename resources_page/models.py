from django.db import models
from django.core.validators import FileExtensionValidator

# 1. Hero Section (Singleton)
class ResourcesHero(models.Model):
    title = models.CharField(max_length=255, default="Knowledge Center")
    subtitle = models.TextField(default="Insights, downloads, and success stories.")
    
    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Section"

    def __str__(self):
        return "Resources Hero Content"

# 2. Section Titles (Singleton - To manage headings like 'Success Stories')
class SectionTitles(models.Model):
    case_studies_title = models.CharField(max_length=100, default="Success Stories")
    downloads_title = models.CharField(max_length=100, default="Downloads")
    
    class Meta:
        verbose_name = "Section Titles"
        verbose_name_plural = "Section Titles"

    def __str__(self):
        return "Page Section Titles"

# 3. Case Studies (List Item)
class CaseStudy(models.Model):
    title = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255, blank=True)
    summary = models.TextField()
    result_stat = models.CharField(max_length=100, help_text="e.g. '40% ROI Increase'")
    pdf_file = models.FileField(upload_to="case_studies/", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Case Study"
        verbose_name_plural = "Case Studies"

    def __str__(self):
        return self.title

# 4. Downloadable Resources (List Item)
class DownloadableResource(models.Model):
    TYPE_CHOICES = [
        ('Whitepaper', 'Whitepaper'), 
        ('E-Book', 'E-Book'), 
        ('Guide', 'Guide'),
        ('Report', 'Report'),
        ('Dataset', 'Dataset')
    ]
    
    title = models.CharField(max_length=255)
    resource_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='Guide')
    description = models.TextField()
    file = models.FileField(
        upload_to="downloads/",
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'csv', 'xlsx', 'ppt', 'docx', 'zip'])]
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Download Item"
        verbose_name_plural = "Download Items"

    def __str__(self):
        return self.title