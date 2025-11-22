from django.core.management.base import BaseCommand
from cms.models import SiteContent

class Command(BaseCommand):
    help = 'Seeds the database with initial data for the home page.'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding home page data...')

        home_page_content = [
            {'section': 'hero_title', 'title': 'Empowering Global Businesses with Smart Financial Solutions'},
            {'section': 'hero_text', 'content': 'XpertAI Global helps companies simplify accounting, auditing, taxation, and financial automation — backed by powerful AI-ready systems.'},
            {'section': 'services_title', 'title': 'Our Key Offerings'},
            {'section': 'service1_title', 'title': 'Virtual CFO'},
            {'section': 'service1_desc', 'content': 'End-to-end financial management and strategy.'},
            {'section': 'service2_title', 'title': 'Audit & Assurance'},
            {'section': 'service2_desc', 'content': 'Accurate reports, compliance, and transparency.'},
            {'section': 'service3_title', 'title': 'Taxation Services'},
            {'section': 'service3_desc', 'content': 'Smart GST, TDS, and ITR management systems.'},
            {'section': 'features_title', 'title': 'Why Choose XpertAI Global?'},
            {'section': 'feature1_title', 'title': 'AI-Powered Automation'},
            {'section': 'feature1_desc', 'content': 'Streamline your financial processes with intelligent automation, reducing manual effort and errors.'},
            {'section': 'feature2_title', 'title': 'Integrated Dashboards'},
            {'section': 'feature2_desc', 'content': 'Gain real-time insights into your financial health with customizable and intuitive dashboards.'},
            {'section': 'feature3_title', 'title': 'Secure Document Control'},
            {'section': 'feature3_desc', 'content': 'Manage and secure all your critical financial documents with advanced access controls and encryption.'},
            {'section': 'how_it_works_title', 'title': 'How It Works'},
            {'section': 'step1_title', 'title': 'Consultation'},
            {'section': 'step1_desc', 'content': 'We start with a detailed consultation to understand your business needs and financial challenges.'},
            {'section': 'step2_title', 'title': 'Implementation'},
            {'section': 'step2_desc', 'content': 'Our experts implement tailored AI-driven solutions to automate and streamline your financial workflows.'},
            {'section': 'step3_title', 'title': 'Support & Growth'},
            {'section': 'step3_desc', 'content': 'We provide ongoing support and insights to help you scale your business and achieve financial excellence.'},
            {'section': 'our_mission_title', 'title': 'Our Mission'},
            {'section': 'our_mission_text', 'content': 'Our mission is to empower businesses with intelligent financial solutions that drive growth, efficiency, and compliance. We are committed to delivering innovative and reliable services that exceed our clients\' expectations.'},
            {'section': 'our_vision_title', 'title': 'Our Vision'},
            {'section': 'our_vision_text', 'content': 'Our vision is to be a global leader in financial technology, renowned for our cutting-edge solutions and unwavering commitment to client success. We aspire to create a future where businesses of all sizes can thrive with the power of AI-driven financial management.'},
            {'section': 'our_team_title', 'title': 'Our Team'},
            {'section': 'team_member1_name', 'title': 'John Doe'},
            {'section': 'team_member1_role', 'content': 'Founder & CEO'},
            {'section': 'team_member2_name', 'title': 'Jane Smith'},
            {'section': 'team_member2_role', 'content': 'Head of Technology'},
            {'section': 'team_member3_name', 'title': 'Peter Jones'},
            {'section': 'team_member3_role', 'content': 'Lead Financial Analyst'},
            {'section': 'testimonials_title', 'title': 'What Our Clients Say'},
            {'section': 'testimonial1_text', 'content': 'XpertAI Global has transformed our financial operations. Their AI-powered solutions have saved us countless hours and provided invaluable insights.'},
            {'section': 'testimonial1_author', 'title': '- John Doe, CEO of InnoTech'},
            {'section': 'our_commitment_title', 'title': 'Our Commitment'},
            {'section': 'our_commitment_text', 'content': 'We are dedicated to providing our clients with the highest level of service and support. Our team is committed to helping you achieve your financial goals and grow your business. We believe in building long-term relationships based on trust, integrity, and mutual success.'},
            {'section': 'case_studies_title', 'title': 'Case Studies'},
            {'section': 'case_study1_title', 'title': 'Streamlining Financial Operations for a Growing Startup'},
            {'section': 'case_study1_desc', 'content': 'Learn how we helped a fast-growing tech startup automate their financial processes, reduce costs, and improve accuracy with our AI-powered solutions.'},
            {'section': 'case_study2_title', 'title': 'Enhancing Financial Reporting for a Global Corporation'},
            {'section': 'case_study2_desc', 'content': 'Discover how we implemented a comprehensive financial reporting system for a multinational corporation, providing real-time insights and improving decision-making.'},
            {'section': 'latest_blog_posts_title', 'title': 'Latest Blog Posts'},
            {'section': 'blog_post1_title', 'title': 'The Future of AI in Financial Management'},
            {'section': 'blog_post1_desc', 'content': 'Explore the latest trends and predictions for the role of artificial intelligence in shaping the future of finance.'},
            {'section': 'blog_post2_title', 'title': 'Top 5 Challenges in Financial Automation'},
            {'section': 'blog_post2_desc', 'content': 'Learn about the most common challenges businesses face when implementing financial automation and how to overcome them.'},
            {'section': 'blog_post3_title', 'title': 'How to Choose the Right Financial Software'},
            {'section': 'blog_post3_desc', 'content': 'A comprehensive guide to selecting the best financial software for your business needs, from features to pricing.'},
            {'section': 'our_values_title', 'title': 'Our Values'},
            {'section': 'value1_title', 'title': 'Integrity'},
            {'section': 'value1_desc', 'content': 'We uphold the highest standards of integrity in all of our actions.'},
            {'section': 'value2_title', 'title': 'Commitment'},
            {'section': 'value2_desc', 'content': 'We are committed to delivering the best possible service to our clients.'},
            {'section': 'value3_title', 'title': 'Innovation'},
            {'section': 'value3_desc', 'content': 'We are constantly innovating to find new and better ways to serve our clients.'},
            {'section': 'technology_stack_title', 'title': 'Technology Stack'},
            {'section': 'clientele_title', 'title': 'Our Clientele'},
            {'section': 'cta_title', 'title': 'Ready to Transform Your Financial Operations?'},
            {'section': 'cta_button', 'content': 'Get in Touch'},
        ]

        for item in home_page_content:
            SiteContent.objects.update_or_create(
                page='home',
                section=item['section'],
                defaults={
                    'title': item.get('title', ''),
                    'content': item.get('content', '')
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded home page data.'))
