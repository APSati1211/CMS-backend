from django.db import models

class Stakeholder(models.Model):
    title = models.CharField(max_length=200, help_text="e.g. Clients, Investors")
    description = models.TextField(help_text="Short description about this stakeholder group.")
    # Icon ke liye hum ImageField use karenge taki tum custom icon upload kar sako
    icon = models.ImageField(upload_to="stakeholders/", blank=True, null=True)
    order = models.PositiveIntegerField(default=0, help_text="Order on the website")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title