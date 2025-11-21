from django.core.exceptions import ValidationError
from django.db import models

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
    ]

    page = models.CharField(max_length=50, choices=PAGE_CHOICES)
    section = models.CharField(
        max_length=100,
        help_text=get_help_text(),
    )   # e.g. hero_title, hero_text, service1_title
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="cms/", blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("page", "section")
        ordering = ["page", "section"]

    def __str__(self):
        return f"{self.page} - {self.section}"

    def clean(self):
        super().clean()
        allowed = get_section_slugs(self.page)
        if allowed and self.section not in allowed:
            allowed_display = ", ".join(allowed)
            raise ValidationError(
                {
                    "section": f"'{self.section}' is not valid for {self.page}. "
                    f"Allowed sections: {allowed_display}"
                }
            )

class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    page_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['page_order']
        verbose_name_plural = "Pages"

    def __str__(self):
        return self.title
