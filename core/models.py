from django.db import models

# Example model
class ExampleModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Theme(models.Model):
    primary_color = models.CharField(max_length=7, default='#000000')
    secondary_color = models.CharField(max_length=7, default='#FFFFFF')

    def __str__(self):
        return "Website Theme"
