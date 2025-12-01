from django.db import models

class CareersPage(models.Model):
    """
    Singleton model to manage the static content of the Careers Page.
    """
    # Hero Section
    hero_title = models.CharField(max_length=255, default="Build the Future of Finance")
    hero_subtitle = models.TextField(default="Join a team of visionaries, engineers, and financial experts redefining the global economy.")
    
    # Benefits Section Header
    benefits_title = models.CharField(max_length=255, default="Why Join XpertAI?")
    benefits_subtitle = models.TextField(default="Perks that help you grow, learn, and thrive.")

    # Culture Section
    culture_title = models.CharField(max_length=255, default="Our Culture")
    culture_text = models.TextField(default="We believe in autonomy, mastery, and purpose. Work from anywhere, own your projects, and make a dent in the universe.")
    culture_image = models.ImageField(upload_to="careers/", blank=True, null=True)

    # Job Listings Header
    openings_title = models.CharField(max_length=255, default="Current Openings")

    def __str__(self):
        return "Careers Page Setup"

    class Meta:
        verbose_name = "Careers Page Setup"
        verbose_name_plural = "Careers Page Setup"

class Benefit(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_name = models.CharField(max_length=50, default="Zap", help_text="Lucide Icon Name")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class JobOpening(models.Model):
    title = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100, default="Remote")
    type = models.CharField(max_length=50, choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time'), ('Contract', 'Contract'), ('Internship', 'Internship')])
    description = models.TextField(help_text="HTML Allowed")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    job = models.ForeignKey(JobOpening, on_delete=models.CASCADE, related_name="applications")
    applicant_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    linkedin_url = models.URLField(blank=True)
    resume_link = models.URLField(help_text="Link to Google Drive/Dropbox file")
    cover_letter = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant_name} - {self.job.title}"