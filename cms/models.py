from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator 

from .sections import get_section_slugs, get_help_text

class SiteContent(models.Model):
    PAGE_CHOICES = [
        ("home", "Home"),
        ("about", "About"),
        ("services", "Services"),
        ("features", "Features"),
        ("stakeholders", "Stakeholders"),
        ("lead_system", "Lead System"),
        ("blog", "Blog"),
        ("resources", "Resources"),
        ("careers", "Careers"),
        ("contact", "Contact"),
        ("portfolio", "Portfolio"),
        ("footer", "Footer"),   
    ]

    page = models.CharField(max_length=50, choices=PAGE_CHOICES)
    section_name = models.CharField(max_length=100, help_text="A descriptive name for the content section (e.g., 'Hero Title').")
    section = models.CharField(
        max_length=100,
        help_text="The slug for this section, auto-generated from the section name.",
        editable=False,
    )
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="cms/", blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    content_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        unique_together = ("page", "section")
        ordering = ["content_order"]

    def __str__(self):
        name = self.title or self.section_name or self.section
        return f"{self.page.upper()} | {name}"

    def clean(self):
        super().clean()
        if self.section_name:
            self.section = slugify(self.section_name)


class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    
    # FIX: Removed 'editable=False' so it can be reordered in Admin
    page_order = models.PositiveIntegerField(default=0, db_index=True)
    
    # SEO FIELDS
    meta_title = models.CharField(max_length=255, blank=True, help_text="SEO Title (Browser Tab)")
    meta_description = models.TextField(blank=True, help_text="SEO Meta Description")
    keywords = models.CharField(max_length=255, blank=True, help_text="Comma separated keywords")

    class Meta:
        ordering = ['page_order']
        verbose_name_plural = "Pages"

    def __str__(self):
        return self.title


class CaseStudy(models.Model):
    title = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255)
    summary = models.TextField()
    result_stat = models.CharField(max_length=100, help_text="e.g. '40% ROI Increase'")
    image = models.ImageField(upload_to="casestudies/", blank=True, null=True)
    pdf_file = models.FileField(upload_to="casestudies/pdfs/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Resource(models.Model):
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=[
        ('Whitepaper', 'Whitepaper'), 
        ('E-Book', 'E-Book'), 
        ('Guide', 'Guide'),
        ('Report', 'Report'),
        ('Presentation', 'Presentation'),
        ('Dataset', 'Dataset')
    ])
    description = models.TextField(blank=True)
    file = models.FileField(
        upload_to="resources/",
        help_text="Upload your document here (PDF, Excel, CSV, PPT, Word, etc.)",
        validators=[FileExtensionValidator(allowed_extensions=[
            'pdf', 'csv', 'xlsx', 'xls', 'ppt', 'pptx', 'doc', 'docx', 'txt', 'zip'
        ])]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# --- PROXY MODELS ---

class HomeContent(SiteContent):
    class Meta:
        proxy = True
        verbose_name = "Page: Home"
        verbose_name_plural = "Page: Home Content"

class AboutContent(SiteContent):
    class Meta:
        proxy = True
        verbose_name = "Page: About"
        verbose_name_plural = "Page: About Content"

class ServicesContent(SiteContent):
    class Meta:
        proxy = True
        verbose_name = "Page: Services"
        verbose_name_plural = "Page: Services Content"

class ContactContent(SiteContent):
    class Meta:
        proxy = True
        verbose_name = "Page: Contact"
        verbose_name_plural = "Page: Contact Content"

class CareersContent(SiteContent):
    class Meta:
        proxy = True
        verbose_name = "Page: Careers"
        verbose_name_plural = "Page: Careers Content"

class ResourcesContent(SiteContent):
    class Meta:
        proxy = True
        verbose_name = "Page: Resources"
        verbose_name_plural = "Page: Resources Content"

class FooterContent(SiteContent):
    class Meta:
        proxy = True
        verbose_name = "Page: Footer"
        verbose_name_plural = "Page: Footer Content"

class Service(models.Model):
    title = models.CharField(max_length=200, help_text="e.g. Virtual CFO")
    slug = models.SlugField(unique=True, help_text="URL friendly name, e.g. virtual-cfo")
    short_description = models.TextField(help_text="Shown on the main Services page card")
    full_description = models.TextField(help_text="Shown on the detailed service page. HTML allowed.")
    icon = models.CharField(max_length=50, default="Briefcase", help_text="Icon name (e.g. Briefcase, BarChart)")
    image = models.ImageField(upload_to="services/", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title