from django.db import models
from django.core.exceptions import ValidationError

class Theme(models.Model):
    name = models.CharField(max_length=100, default="Default Theme")
    primary_color = models.CharField(max_length=7, default='#1c1c1c')
    secondary_color = models.CharField(max_length=7, default='#f8f9fa')
    accent_color = models.CharField(max_length=7, default='#007bff')
    background_color = models.CharField(max_length=7, default='#ffffff')
    text_color = models.CharField(max_length=7, default='#343a40')
    heading_color = models.CharField(max_length=7, default='#000000')
    link_color = models.CharField(max_length=7, default='#007bff')
    footer_background_color = models.CharField(max_length=7, default='#1c1c1c')
    footer_text_color = models.CharField(max_length=7, default='#ffffff')
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk and Theme.objects.exists():
            raise ValidationError('There can be only one Theme instance')
        return super(Theme, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Theme"