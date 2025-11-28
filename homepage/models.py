from django.db import models

# 1. Hero Section
class HeroSection(models.Model):
    title = models.CharField(max_length=255, default="Transforming Finance...")
    subtitle = models.TextField(default="Automate accounting, audits...")
    image = models.ImageField(upload_to="homepage/", blank=True, null=True)
    cta_text = models.CharField(max_length=50, default="Get Started")
    
    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Section"

    def __str__(self):
        return "Hero Section Content"

# 2. Stats Strip
class Stat(models.Model):
    value = models.CharField(max_length=50, help_text="e.g. 500+")
    label = models.CharField(max_length=100, help_text="e.g. Clients Served")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.label

# 3. Features
class Feature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # Icon ka naam text mein store karenge (Frontend par map hoga)
    icon_name = models.CharField(max_length=50, default="TrendingUp", help_text="Icon Name from Lucide (e.g. TrendingUp, Shield, Users)")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

# 4. Bottom CTA
class BottomCTA(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    button_text = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Bottom CTA"
        verbose_name_plural = "Bottom CTA"

    def __str__(self):
        return "Bottom CTA Content"