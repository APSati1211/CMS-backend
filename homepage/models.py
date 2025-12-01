from django.db import models

class HomePageContent(models.Model):
    """
    Singleton model to manage all text content, titles, and single sections on the Home Page.
    """
    # --- 1. HERO SECTION ---
    hero_title = models.CharField(max_length=255, default="Next-Gen Financial Intelligence")
    hero_subtitle = models.TextField(default="Automate audits, tax compliance, and forecasting with AI precision.")
    hero_image = models.ImageField(upload_to="homepage/", blank=True, null=True)
    hero_cta_text = models.CharField(max_length=50, default="Start Free Trial")

    # --- 2. TRUSTED CLIENTS HEADER ---
    clients_title = models.CharField(max_length=255, default="Trusted by Industry Leaders", blank=True)

    # --- 3. PROCESS SECTION HEADER ---
    process_title = models.CharField(max_length=255, default="How It Works", blank=True)
    process_subtitle = models.TextField(default="Seamless integration in 3 simple steps.", blank=True)

    # --- 4. FEATURES HEADER ---
    features_title = models.CharField(max_length=255, default="Why Choose XpertAI?", blank=True)

    # --- 5. TESTIMONIALS HEADER ---
    reviews_title = models.CharField(max_length=255, default="Client Success Stories", blank=True)

    # --- 6. FAQ HEADER ---
    faq_title = models.CharField(max_length=255, default="Frequently Asked Questions", blank=True)

    # --- 7. BOTTOM CTA SECTION ---
    cta_title = models.CharField(max_length=255, default="Ready to Transform?")
    cta_text = models.TextField(default="Join 500+ companies streamlining their finance today.")
    cta_btn_text = models.CharField(max_length=50, default="Get Started")

    def __str__(self):
        return "Home Page Main Content"

    class Meta:
        verbose_name = "Home Page Setup"
        verbose_name_plural = "Home Page Setup"


# --- LIST MODELS (Multiple Items) ---

class TrustedClient(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="clients/")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class Stat(models.Model):
    value = models.CharField(max_length=50, help_text="e.g. 500+")
    label = models.CharField(max_length=100, help_text="e.g. Clients Served")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.label

class ProcessStep(models.Model):
    step_number = models.CharField(max_length=10, default="01")
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_name = models.CharField(max_length=50, default="Settings", help_text="Lucide Icon Name")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.step_number} - {self.title}"

class Feature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_name = models.CharField(max_length=50, default="TrendingUp")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    author_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    quote = models.TextField()
    image = models.ImageField(upload_to="testimonials/", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.author_name

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "FAQ"

    def __str__(self):
        return self.question