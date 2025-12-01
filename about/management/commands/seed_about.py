from django.core.management.base import BaseCommand
from about.models import AboutPage, TeamMember, Award

class Command(BaseCommand):
    help = 'Seeds the About Page with rich dummy data (Hero, Story, Team, Awards)'

    def handle(self, *args, **kwargs):
        self.stdout.write('🚀 Seeding About Page Data...')

        # --- 1. ABOUT PAGE CONTENT (Singleton) ---
        about_data = {
            "hero_title": "About XpertAI Global",
            "hero_subtitle": "Pioneering the future of financial intelligence with AI-driven precision.",
            
            "mission_title": "Our Mission",
            "mission_text": "To democratize high-end financial analytics for businesses of all sizes, ensuring transparency and growth.",
            
            "vision_title": "Our Vision",
            "vision_text": "A world where financial decisions are automated, accurate, and strategic, freeing humans to innovate.",
            
            "values_title": "Our Values",
            "values_text": "Integrity, Innovation, and Impact - the core pillars driving every solution we build.",
            
            "story_title": "Our Story",
            "story_text": "Founded in 2020 by a group of financial experts and AI engineers, XpertAI started with a simple idea: Remove the manual drudgery from finance. \n\nWhat began in a small garage in Bangalore has now grown into a global consultancy serving Fortune 500 companies. We believe that technology should serve people, not the other way around.",
            
            "global_title": "Global Presence",
            "global_stats": "Trusted by 500+ Clients in 20+ Countries",
            
            "awards_title": "Awards & Recognition",
            
            "csr_title": "Sustainability & CSR",
            "csr_text": "We are committed to a net-zero carbon footprint. Our data centers run on 100% renewable energy, and we actively support digital literacy programs in rural India.",
            
            "cta_title": "Ready to Transform Your Finance?",
            "cta_text": "Join the revolution of automated financial intelligence today."
        }

        # Create or Update the single AboutPage record
        obj, created = AboutPage.objects.update_or_create(id=1, defaults=about_data)
        if created:
            self.stdout.write("   ✅ Created About Page Content")
        else:
            self.stdout.write("   ✅ Updated About Page Content")

        # --- 2. TEAM MEMBERS ---
        team_data = [
            {"name": "Aditi Rao", "role": "Chief Executive Officer", "order": 1},
            {"name": "Rajesh Kumar", "role": "Chief Technology Officer", "order": 2},
            {"name": "Sarah Jenkins", "role": "Head of Finance", "order": 3},
            {"name": "Michael Chen", "role": "VP of AI Research", "order": 4},
        ]

        for member in team_data:
            TeamMember.objects.update_or_create(
                name=member['name'],
                defaults={
                    "role": member['role'],
                    "order": member['order'],
                    "bio": f"{member['name']} leads our team with over 15 years of experience in the industry.",
                    # "image": You can upload images via admin later
                }
            )
            self.stdout.write(f"   ✅ Team Member: {member['name']}")

        # --- 3. AWARDS ---
        awards_data = [
            {"title": "Best Fintech Startup", "year": "2024", "description": "Awarded by Global Finance Forum for excellence in automation."},
            {"title": "AI Innovation Award", "year": "2023", "description": "Recognized for our breakthrough predictive tax algorithms."},
            {"title": "Great Place to Work", "year": "2022", "description": "Certified for our outstanding company culture and employee growth."},
        ]

        for award in awards_data:
            Award.objects.update_or_create(
                title=award['title'],
                defaults={
                    "year": award['year'],
                    "description": award['description']
                }
            )
            self.stdout.write(f"   ✅ Award: {award['title']}")

        self.stdout.write(self.style.SUCCESS('\n🎉 About Page Seeded Successfully!'))