def _card_sections(prefix, count, label_prefix):
    sections = []
    for idx in range(1, count + 1):
        sections.append(
            {
                "section": f"{prefix}_{idx}_title",
                "label": f"{label_prefix} {idx} • Title",
                "field": "title",
            }
        )
        sections.append(
            {
                "section": f"{prefix}_{idx}_desc",
                "label": f"{label_prefix} {idx} • Description",
                "field": "content",
            }
        )
    return sections


def _resource_sections(count):
    sections = []
    for idx in range(1, count + 1):
        sections.extend(
            [
                {
                    "section": f"resource_card_{idx}_title",
                    "label": f"Resource {idx} • Title",
                    "field": "title",
                },
                {
                    "section": f"resource_card_{idx}_desc",
                    "label": f"Resource {idx} • Description",
                    "field": "content",
                },
                {
                    "section": f"resource_card_{idx}_link",
                    "label": f"Resource {idx} • Link URL",
                    "field": "content",
                },
            ]
        )
    return sections


def _stakeholder_sections(count):
    sections = []
    for idx in range(1, count + 1):
        sections.extend(
            [
                {
                    "section": f"stakeholder_card_{idx}_title",
                    "label": f"Stakeholder Card {idx} • Title",
                    "field": "title",
                },
                {
                    "section": f"stakeholder_card_{idx}_desc",
                    "label": f"Stakeholder Card {idx} • Description",
                    "field": "content",
                },
                {
                    "section": f"stakeholder_card_{idx}_icon",
                    "label": f"Stakeholder Card {idx} • Icon/Emoji",
                    "field": "content",
                },
            ]
        )
    return sections


def _job_sections(count):
    sections = []
    for idx in range(1, count + 1):
        sections.extend(
            [
                {
                    "section": f"job_card_{idx}_title",
                    "label": f"Job Card {idx} • Role Title",
                    "field": "title",
                },
                {
                    "section": f"job_card_{idx}_dept",
                    "label": f"Job Card {idx} • Department",
                    "field": "content",
                },
                {
                    "section": f"job_card_{idx}_location",
                    "label": f"Job Card {idx} • Location",
                    "field": "content",
                },
                {
                    "section": f"job_card_{idx}_type",
                    "label": f"Job Card {idx} • Type",
                    "field": "content",
                },
            ]
        )
    return sections


PAGE_SECTIONS = {
    "home": [
        {"section": "hero_title", "label": "Hero • Title", "field": "title"},
        {"section": "hero_text", "label": "Hero • Subtitle", "field": "content"},
        {"section": "hero_image", "label": "Hero • Image", "field": "image"},
        {"section": "services_title", "label": "Services • Title", "field": "title"},
        {"section": "service1_title", "label": "Service Card 1 • Title", "field": "title"},
        {"section": "service1_desc", "label": "Service Card 1 • Description", "field": "content"},
        {"section": "service2_title", "label": "Service Card 2 • Title", "field": "title"},
        {"section": "service2_desc", "label": "Service Card 2 • Description", "field": "content"},
        {"section": "service3_title", "label": "Service Card 3 • Title", "field": "title"},
        {"section": "service3_desc", "label": "Service Card 3 • Description", "field": "content"},
        {"section": "cta_button", "label": "CTA • Button Text", "field": "content"},
        {"section": "our_values_title", "label": "Our Values • Title", "field": "title"},
        {"section": "value1_title", "label": "Value 1 • Title", "field": "title"},
        {"section": "value1_desc", "label": "Value 1 • Description", "field": "content"},
        {"section": "value2_title", "label": "Value 2 • Title", "field": "title"},
        {"section": "value2_desc", "label": "Value 2 • Description", "field": "content"},
        {"section": "value3_title", "label": "Value 3 • Title", "field": "title"},
        {"section": "value3_desc", "label": "Value 3 • Description", "field": "content"},
        {"section": "technology_stack_title", "label": "Technology Stack • Title", "field": "title"},
        {"section": "tech1_logo", "label": "Tech 1 • Logo", "field": "image"},
        {"section": "tech2_logo", "label": "Tech 2 • Logo", "field": "image"},
        {"section": "tech3_logo", "label": "Tech 3 • Logo", "field": "image"},
        {"section": "tech4_logo", "label": "Tech 4 • Logo", "field": "image"},
        {"section": "clientele_title", "label": "Clientele • Title", "field": "title"},
        {"section": "client1_logo", "label": "Client 1 • Logo", "field": "image"},
        {"section": "client2_logo", "label": "Client 2 • Logo", "field": "image"},
        {"section": "client3_logo", "label": "Client 3 • Logo", "field": "image"},
        {"section": "client4_logo", "label": "Client 4 • Logo", "field": "image"},
        {"section": "additional_info_title", "label": "Additional Info • Title", "field": "title"},
        {"section": "additional_info_paragraph1", "label": "Additional Info • Paragraph 1", "field": "content"},
        {"section": "additional_info_paragraph2", "label": "Additional Info • Paragraph 2", "field": "content"},
        {"section": "additional_info_header", "label": "Additional Info • Header", "field": "title"},
        {"section": "award1_desc", "label": "Award 1 • Desc", "field": "content"},
        {"section": "award1_year", "label": "Award 1 • Year", "field": "title"},
        {"section": "award2_desc", "label": "Award 2 • Desc", "field": "content"},
        {"section": "award2_year", "label": "Award 2 • Year", "field": "title"},
        {"section": "award3_desc", "label": "Award 3 • Desc", "field": "content"},
        {"section": "award3_year", "label": "Award 3 • Year", "field": "title"},
        {"section": "awards_title", "label": "Awards • Title", "field": "title"},
        {"section": "blog_posts_title", "label": "Blog Posts • Title", "field": "title"},
        {"section": "case_studies_title", "label": "Case Studies • Title", "field": "title"},
        {"section": "client_success_stories_intro", "label": "Client Success Stories • Intro", "field": "title"},
        {"section": "client_success_stories_text", "label": "Client Success Stories • Text", "field": "content"},
        {"section": "core_values_description", "label": "Core Values • Description", "field": "content"},
        {"section": "core_values_statement", "label": "Core Values • Statement", "field": "title"},
        {"section": "cta_title", "label": "CTA • Title", "field": "title"},
        {"section": "feature1_desc", "label": "Feature 1 • Desc", "field": "content"},
        {"section": "feature1_title", "label": "Feature 1 • Title", "field": "title"},
        {"section": "feature2_desc", "label": "Feature 2 • Desc", "field": "content"},
        {"section": "feature2_title", "label": "Feature 2 • Title", "field": "title"},
        {"section": "feature3_desc", "label": "Feature 3 • Desc", "field": "content"},
        {"section": "feature3_title", "label": "Feature 3 • Title", "field": "title"},
        {"section": "features_title", "label": "Features • Title", "field": "title"},
        {"section": "how_it_works_title", "label": "How It Works • Title", "field": "title"},
        {"section": "our_commitment_text", "label": "Our Commitment • Text", "field": "content"},
        {"section": "our_commitment_title", "label": "Our Commitment • Title", "field": "title"},
        {"section": "our_mission_text", "label": "Our Mission • Text", "field": "content"},
        {"section": "our_mission_title", "label": "Our Mission • Title", "field": "title"},
        {"section": "our_philosophy_innovation", "label": "Our Philosophy Innovation • Title", "field": "title"},
        {"section": "our_philosophy_innovation_desc", "label": "Our Philosophy Innovation • Desc", "field": "content"},
        {"section": "our_philosophy_intro", "label": "Our Philosophy • Intro", "field": "content"},
        {"section": "our_philosophy_title", "label": "Our Philosophy • Title", "field": "title"},
        {"section": "our_philosophy_transparency", "label": "Our Philosophy Transparency • Title", "field": "title"},
        {"section": "our_philosophy_transparency_desc", "label": "Our Philosophy Transparency • Desc", "field": "content"},
        {"section": "our_process_title", "label": "Our Process • Title", "field": "title"},
        {"section": "our_vision_text", "label": "Our Vision • Text", "field": "content"},
        {"section": "our_vision_title", "label": "Our Vision • Title", "field": "title"},
        {"section": "partnership1_desc", "label": "Partnership 1 • Desc", "field": "content"},
        {"section": "partnership1_name", "label": "Partnership 1 • Name", "field": "title"},
        {"section": "partnership2_desc", "label": "Partnership 2 • Desc", "field": "content"},
        {"section": "partnership2_name", "label": "Partnership 2 • Name", "field": "title"},
        {"section": "partnerships_title", "label": "Partnerships • Title", "field": "title"},
        {"section": "portfolio_title", "label": "Portfolio • Title", "field": "title"},
        {"section": "step1_desc", "label": "Step 1 • Desc", "field": "content"},
        {"section": "step1_title", "label": "Step 1 • Title", "field": "title"},
        {"section": "step2_desc", "label": "Step 2 • Desc", "field": "content"},
        {"section": "step2_title", "label": "Step 2 • Title", "field": "title"},
        {"section": "step3_desc", "label": "Step 3 • Desc", "field": "content"},
        {"section": "step3_title", "label": "Step 3 • Title", "field": "title"},
        {"section": "testimonial1_author", "label": "Testimonial 1 • Author", "field": "title"},
        {"section": "testimonial1_text", "label": "Testimonial 1 • Text", "field": "content"},
        {"section": "testimonial2_author", "label": "Testimonial 2 • Author", "field": "title"},
        {"section": "testimonial2_text", "label": "Testimonial 2 • Text", "field": "content"},
        {"section": "testimonial3_author", "label": "Testimonial 3 • Author", "field": "title"},
        {"section": "testimonial3_text", "label": "Testimonial 3 • Text", "field": "content"},
        {"section": "testimonials_title", "label": "Testimonials • Title", "field": "title"},
        {"section": "why_choose_us_feature1_desc", "label": "Why Choose Us Feature 1 • Desc", "field": "content"},
        {"section": "why_choose_us_feature1_title", "label": "Why Choose Us Feature 1 • Title", "field": "title"},
        {"section": "why_choose_us_feature2_desc", "label": "Why Choose Us Feature 2 • Desc", "field": "content"},
        {"section": "why_choose_us_feature2_title", "label": "Why Choose Us Feature 2 • Title", "field": "title"},
        {"section": "why_choose_us_feature3_desc", "label": "Why Choose Us Feature 3 • Desc", "field": "content"},
        {"section": "why_choose_us_feature3_title", "label": "Why Choose Us Feature 3 • Title", "field": "title"},
        {"section": "why_choose_us_title", "label": "Why Choose Us • Title", "field": "title"},
        {"section": "blog_post1_title", "label": "Blog Post 1 • Title", "field": "title"},
        {"section": "blog_post1_desc", "label": "Blog Post 1 • Desc", "field": "content"},
        {"section": "blog_post2_title", "label": "Blog Post 2 • Title", "field": "title"},
        {"section": "blog_post2_desc", "label": "Blog Post 2 • Desc", "field": "content"},
        {"section": "blog_post3_title", "label": "Blog Post 3 • Title", "field": "title"},
        {"section": "blog_post3_desc", "label": "Blog Post 3 • Desc", "field": "content"},
        {"section": "case_study1_title", "label": "Case Study 1 • Title", "field": "title"},
        {"section": "case_study1_desc", "label": "Case Study 1 • Desc", "field": "content"},
        {"section": "case_study2_title", "label": "Case Study 2 • Title", "field": "title"},
        {"section": "case_study2_desc", "label": "Case Study 2 • Desc", "field": "content"},
        {"section": "a1", "label": "A1 (temporary)", "field": "content"},
    ],
    "contact": [
        {"section": "contact_header", "label": "Hero • Title", "field": "title"},
        {"section": "contact_subtext", "label": "Hero • Subtitle", "field": "content"},
        {"section": "form_title", "label": "Form • Title", "field": "title"},
        {"section": "info_title", "label": "Info Panel • Title", "field": "title"},
        {"section": "info_text", "label": "Info Panel • Description", "field": "content"},
        {"section": "address", "label": "Info Panel • Address", "field": "content"},
        {"section": "email", "label": "Info Panel • Email", "field": "content"},
        {"section": "phone", "label": "Info Panel • Phone", "field": "content"},
        {"section": "map_link", "label": "Info Panel • Map Link", "field": "content"},
        {"section": "map_button", "label": "Info Panel • Map Button Label", "field": "title"},
        {"section": "cta_title", "label": "CTA • Title", "field": "title"},
        {"section": "cta_button", "label": "CTA • Button Text", "field": "content"},
    ],
    "about": [
        {"section": "hero_title", "label": "Hero • Title", "field": "title"},
        {"section": "hero_text", "label": "Hero • Subtitle", "field": "content"},
        {"section": "mission_title", "label": "Mission • Title", "field": "title"},
        {"section": "mission_text", "label": "Mission • Description", "field": "content"},
        {"section": "vision_title", "label": "Vision • Title", "field": "title"},
        {"section": "vision_text", "label": "Vision • Description", "field": "content"},
        {"section": "values_title", "label": "Values • Title", "field": "title"},
        {"section": "values_text", "label": "Values • Description", "field": "content"},
        {"section": "cta_title", "label": "CTA • Title", "field": "title"},
        {"section": "cta_text", "label": "CTA • Description", "field": "content"},
    ],
    "services": [
        {"section": "hero_title", "label": "Hero • Title", "field": "title"},
        {"section": "hero_text", "label": "Hero • Subtitle", "field": "content"},
        *_card_sections("service_card", 6, "Service Card"),
        {"section": "cta_title", "label": "CTA • Title", "field": "title"},
        {"section": "cta_text", "label": "CTA • Description", "field": "content"},
        {"section": "cta_button", "label": "CTA • Button Text", "field": "content"},
    ],
    "features": [
        {"section": "hero_title", "label": "Hero • Title", "field": "title"},
        {"section": "hero_text", "label": "Hero • Subtitle", "field": "content"},
        *_card_sections("feature_card", 6, "Feature Card"),
    ],
    "stakeholders": [
        {"section": "hero_title", "label": "Hero • Title", "field": "title"},
        {"section": "hero_text", "label": "Hero • Subtitle", "field": "content"},
        *_stakeholder_sections(6),
    ],
    "resources": [
        {"section": "hero_title", "label": "Hero • Title", "field": "title"},
        {"section": "hero_text", "label": "Hero • Subtitle", "field": "content"},
        {"section": "downloads_title", "label": "Downloads • Section Title", "field": "title"},
        *_resource_sections(3),
        {"section": "blog_highlight_title", "label": "Blog Highlight • Title", "field": "title"},
    ],
    "lead_system": [
        {"section": "hero_title", "label": "Hero • Title", "field": "title"},
        {"section": "hero_text", "label": "Hero • Subtitle", "field": "content"},
        {"section": "cta_title", "label": "CTA • Title", "field": "title"},
        {"section": "cta_text", "label": "CTA • Description", "field": "content"},
    ],
    "careers": [
        {"section": "hero_title", "label": "Hero • Title", "field": "title"},
        {"section": "hero_text", "label": "Hero • Subtitle", "field": "content"},
        {"section": "openings_title", "label": "Openings • Section Title", "field": "title"},
        *_job_sections(3),
        {"section": "form_title", "label": "Form • Title", "field": "title"},
        {"section": "form_subtext", "label": "Form • Description", "field": "content"},
    ],
    "blog": [
        {"section": "hero_title", "label": "Hero • Title", "field": "title"},
        {"section": "hero_text", "label": "Hero • Subtitle", "field": "content"},
    ],
}


def get_section_slugs(page):
    """Return the list of allowed section identifiers for a page."""
    return [entry["section"] for entry in PAGE_SECTIONS.get(page, [])]


def get_help_text():
    """Return a readable help string for the admin form."""
    lines = []
    for page, entries in PAGE_SECTIONS.items():
        sections = ", ".join(entry["section"] for entry in entries)
        lines.append(f"{page.capitalize()}: {sections}")
    return "Available sections per page → " + " | ".join(lines)

