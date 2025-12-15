from django.db import models
from django.core.validators import FileExtensionValidator

class CareersPage(models.Model):
    # Singleton Model for Page Content
    hero_title = models.CharField(max_length=255, default="Build the Future of Finance")
    hero_subtitle = models.TextField(default="Join a team of visionaries, engineers, and financial experts redefining the global economy.")
    
    benefits_title = models.CharField(max_length=255, default="Why Join XpertAI?")
    benefits_subtitle = models.TextField(default="Perks that help you grow, learn, and thrive.")

    culture_title = models.CharField(max_length=255, default="Our Culture")
    culture_text = models.TextField(default="We believe in autonomy, mastery, and purpose.")
    culture_image = models.ImageField(upload_to="careers/", blank=True, null=True)

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

class EmployeeTestimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    quote = models.TextField()
    image = models.ImageField(upload_to="careers/testimonials/", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class JobOpening(models.Model):
    JOB_TYPES = [
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship')
    ]
    title = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100, default="Remote")
    type = models.CharField(max_length=50, choices=JOB_TYPES)
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
    
    # --- UPDATED FIELDS ---
    resume_link = models.URLField(blank=True, null=True, help_text="Optional Link to Resume (Google Drive/Dropbox)")
    resume_file = models.FileField(
        upload_to="resumes/",
        null=True,   # <--- Add this
        blank=True,  # <--- Add this
        help_text="Upload Resume (PDF Only)",
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
    )#----------------------

    cover_letter = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant_name} - {self.job.title}"