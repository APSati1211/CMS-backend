from django.core.management.base import BaseCommand
from stakeholders.models import Stakeholder, SolutionsPage

class Command(BaseCommand):
    help = 'Seeds the Solutions Page & Categories'

    def handle(self, *args, **kwargs):
        self.stdout.write('🚀 Seeding Solutions Data...')

        # 1. Page Content
        SolutionsPage.objects.update_or_create(id=1, defaults={
            "hero_title": "Our Solutions",
            "hero_subtitle": "Tailored ecosystems for every stakeholder in the financial world.",
            "cta_title": "Ready to join the ecosystem?",
            "cta_text": "Whether you are a client looking for experts or a professional seeking work, XpertAI has a place for you.",
            "cta_btn_primary": "Sign Up Now",
            "cta_btn_secondary": "Contact Sales"
        })
        self.stdout.write("   ✅ Page Content Updated")

        # 2. Categories (Old logic maintained)
        solutions_data = [
            {"title": "Clients", "description": "Businesses looking to outsource financial processes, reduce costs, and access global talent pools.", "icon_name": "Briefcase", "order": 1},
            {"title": "Professionals", "description": "Experienced CAs, CPAs, and financial experts seeking high-value projects.", "icon_name": "UserCheck", "order": 2},
            {"title": "Freelancers / Freshers", "description": "Individuals seeking gig-based work, entry-level opportunities, and career kick-starts.", "icon_name": "Laptop", "order": 3},
            {"title": "Trainers", "description": "Industry experts and mentors providing specialized training and certification.", "icon_name": "Presentation", "order": 4},
            {"title": "Training Institutes", "description": "Organizations partnering to offer structured courses and campus placements.", "icon_name": "School", "order": 5}
        ]

        Stakeholder.objects.all().delete()
        for item in solutions_data:
            Stakeholder.objects.create(**item)
            self.stdout.write(f"   ✅ Created Solution: {item['title']}")

        self.stdout.write(self.style.SUCCESS('🎉 Solutions Page Fully Seeded!'))