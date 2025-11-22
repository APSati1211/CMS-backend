from pathlib import Path
import os
from decouple import config # <-- NEW: Import config

BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# CORE SETTINGS
# -----------------------------
# Load SECRET_KEY from .env file, with a secure fallback
SECRET_KEY = config(
    "DJANGO_SECRET_KEY", 
    default="django-insecure-1234567890-your-secret-key"
)

# Load DEBUG from .env file
DEBUG = config("DEBUG", default=False, cast=bool) 

# --- OPENAI API KEY (ADDED HERE) ---
OPENAI_API_KEY = config("OPENAI_API_KEY", default=None) 

ALLOWED_HOSTS = ["*"]  # allow all for development

# -----------------------------
# INSTALLED APPS
# -----------------------------
INSTALLED_APPS = [
    'jazzmin',  # <--- JAZZMIN Added at the TOP

    # 'admin_interface', # <--- Commented out to avoid conflict
    # 'colorfield',      # <--- Commented out to avoid conflict

    'django.contrib.admin',
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # third-party
    "rest_framework",
    "corsheaders",
    "adminsortable2",

    # custom apps
    "core",
    "blog",
    "cms",
    "contact",
    "leads",
    "theme",
    "pages",
    "careers",
]

# -----------------------------
# MIDDLEWARE
# -----------------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # must be at the top
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ROOT_URLCONF = "backend.urls"

# -----------------------------
# TEMPLATES
# -----------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"

# -----------------------------
# DATABASE (SQLite)
# -----------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# -----------------------------
# PASSWORD VALIDATION
# -----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -----------------------------
# INTERNATIONALIZATION
# -----------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# -----------------------------
# STATIC & MEDIA FILES
# -----------------------------
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles") 
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# -----------------------------
# DJANGO REST FRAMEWORK
# -----------------------------
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ]
}

# -----------------------------
# CORS SETTINGS
# -----------------------------
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
CORS_ALLOW_CREDENTIALS = True

# -----------------------------
# DEFAULT PRIMARY KEY
# -----------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ==========================================
#  JAZZMIN SETTINGS (Modern Admin UI)
# ==========================================

JAZZMIN_SETTINGS = {
    # Branding
    "site_title": "XpertAI Admin",
    "site_header": "XpertAI Global",
    "site_brand": "XpertAI CMS",
    "welcome_sign": "Welcome to XpertAI Global Headquarters",
    "copyright": "XpertAI Global Ltd",
    "search_model": ["auth.User", "cms.Service"],

    # UI Customization
    "topmenu_links": [
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "View Website", "url": "http://localhost:3000", "new_window": True},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],

    # Icons
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "cms.HomeContent": "fas fa-home",
        "cms.AboutContent": "fas fa-info-circle",
        "cms.ServicesContent": "fas fa-briefcase",
        "cms.ContactContent": "fas fa-envelope",
        "cms.CareersContent": "fas fa-user-tie",
        "cms.ResourcesContent": "fas fa-book",
        "cms.Page": "fas fa-file-alt",
        "cms.Service": "fas fa-cogs",
        "cms.CaseStudy": "fas fa-chart-line",
        "cms.Resource": "fas fa-download",
        "careers.JobOpening": "fas fa-briefcase",
        "careers.JobApplication": "fas fa-file-signature",
        "leads.Lead": "fas fa-bullhorn",
        "leads.WebsiteLead": "fas fa-globe",
        "leads.ChatbotLead": "fas fa-robot",
        "contact.ContactMessage": "fas fa-paper-plane",
        "blog.BlogPost": "fas fa-newspaper",
    },
    
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": True,
    "use_google_fonts_cdn": True,
    "show_ui_builder": True,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-primary",
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    
    # --- THEME SETTINGS ---
    "theme": "flatly", 
     "dark_mode_theme": "darkly", # <--- Commented this to prevent auto dark mode

    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}