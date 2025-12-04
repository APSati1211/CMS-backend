from django.db import models

class Stakeholder(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # Adding icon_name for consistent UI with other pages
    icon_name = models.CharField(max_length=50, default="Users", help_text="Lucide Icon Name")
    image = models.ImageField(upload_to="stakeholders/", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Solution Category"
        verbose_name_plural = "Solution Categories"

    def __str__(self):
        return self.title