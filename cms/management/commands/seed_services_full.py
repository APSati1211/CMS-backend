from django.core.management.base import BaseCommand
from cms.models import Service, ServiceSubService

class Command(BaseCommand):
    help = 'Seeds the Services with complete data from Document 2'

    def handle(self, *args, **kwargs):
        self.stdout.write('🚀 Seeding Full Services Data...')
        
        # Clear old data to prevent duplicates
        Service.objects.all().delete()

        # Data Structure matching Document 2 exactly
        services_data = [
            {
                "title": "Virtual CFO & Advisory",
                "slug": "virtual-cfo-advisory",
                "icon": "TrendingUp",
                "short_description": "Strategic financial guidance, risk management, and business restructuring for growth.",
                "sub_services": [
                    {"title": "1. Virtual CFO Services", "description": "High-level financial strategy without the cost of a full-time CFO. We handle budgeting, forecasting, financial planning, and board reporting."},
                    {"title": "2. Financial Advisory Services", "description": "Expert advice on capital structure, investment decisions, mergers & acquisitions, and optimizing financial health."},
                    {"title": "3. Treasury & Risk Management", "description": "Optimizing liquidity, managing cash flow, hedging currency risks, and mitigating financial exposure."},
                    {"title": "4. Business Restructuring & Turnaround", "description": "Strategic overhauls to revive distressed businesses, improve operational efficiency, and drive profitability."},
                    {"title": "5. ESG & Sustainable Finance Advisory", "description": "Guidance on Environmental, Social, and Governance (ESG) compliance, reporting, and sustainable investment strategies."}
                ]
            },
            {
                "title": "Audit & Assurance",
                "slug": "audit-assurance",
                "icon": "ShieldCheck",
                "short_description": "Comprehensive auditing services ensuring compliance, accuracy, and fraud prevention.",
                "sub_services": [
                    {"title": "1. Statutory & Tax Audits", "description": "Mandatory audits ensuring strict compliance with government regulations, accounting standards, and tax laws."},
                    {"title": "2. Internal & Management Audits", "description": "Evaluating internal controls, operational efficiency, and providing actionable insights to improve management processes."},
                    {"title": "3. Forensic & Fraud Audits", "description": "In-depth investigation of financial discrepancies, fraud detection, and evidence gathering for legal proceedings."},
                    {"title": "4. System and IT Audits", "description": "Reviewing IT infrastructure, data security protocols, and system integrity to prevent cyber risks."},
                    {"title": "5. Risk & Process Audits", "description": "Identifying operational risks, gaps in standard operating procedures (SOPs), and optimizing business processes."},
                    {"title": "6. Bank, Stock & Concurrent Audits", "description": "Specialized audits for banking sectors, real-time transaction verification, and physical stock inventory verification."},
                    {"title": "7. ESG & CSR Impact Audits", "description": "Auditing Corporate Social Responsibility initiatives and measuring the real-world impact of ESG programs."}
                ]
            },
            {
                "title": "Accounting & Outsourcing",
                "slug": "accounting-outsourcing",
                "icon": "Calculator",
                "short_description": "End-to-end bookkeeping, cloud accounting, and back-office support.",
                "sub_services": [
                    {"title": "1. End-to-End Bookkeeping & Accounting", "description": "Complete management of daily financial records, ledgers, journals, and bank reconciliations."},
                    {"title": "2. Cloud-Based Accounting", "description": "Setup and management of modern accounting software like Tally, Xero, Zoho, SAP, and QuickBooks for real-time access."},
                    {"title": "3. MIS & Financial Reporting", "description": "Customized Management Information System (MIS) reports for data-driven decision making and performance tracking."},
                    {"title": "4. Accounts Payable & Receivable Outsourcing", "description": "Managing vendor payments to optimize cash flow and handling client invoicing/collections efficiently."},
                    {"title": "5. Consolidation & Multi-Entity Reporting", "description": "Unified financial reporting for businesses with multiple branches, subsidiaries, or international entities."},
                    {"title": "6. Virtual Back-Office Support", "description": "Administrative and financial support services managed remotely to reduce overhead costs."}
                ]
            },
            {
                "title": "Payroll, HR & Recruitment",
                "slug": "payroll-hr-recruitment",
                "icon": "Users",
                "short_description": "Managing payroll compliance, talent recruitment, and HR structuring.",
                "sub_services": [
                    {"title": "1. Payroll Processing & Compliance", "description": "Accurate processing of monthly salaries, payslips, and compliance with PF, ESI, and Gratuity laws."},
                    {"title": "2. Recruitment & Talent Advisory", "description": "Sourcing the right talent, screening candidates, and advising on hiring strategies for diverse roles."},
                    {"title": "3. International Payroll & HR Structuring", "description": "Managing cross-border payroll complexities and setting up global HR policies for MNCs."},
                    {"title": "4. HR Outsourcing & Talent Recruitment", "description": "End-to-end management of the Human Resources lifecycle, from onboarding to exit formalities."},
                    {"title": "5. Compensation Structuring & Benefits Advisory", "description": "Designing competitive salary structures, incentive plans, and employee benefits packages."},
                    {"title": "6. HR Policies, Contracts & Documentation", "description": "Drafting legally sound employment contracts, employee handbooks, and internal policy documentation."}
                ]
            },
            {
                "title": "Taxation & Compliance",
                "slug": "taxation-compliance",
                "icon": "FileText",
                "short_description": "Expert handling of GST, Tax Returns, and International Taxation.",
                "sub_services": [
                    {"title": "1. Tax Advisory & Returns", "description": "Strategic tax planning and filing for Individuals and Corporates to ensure maximum tax efficiency."},
                    {"title": "2. GST Registration, Filing & Advisory", "description": "End-to-end Goods and Services Tax compliance, including registration, monthly filings, and audit support."},
                    {"title": "3. Transfer Pricing & Cross-Border Taxation", "description": "Managing complex transfer pricing documentation and compliance for related-party international transactions."},
                    {"title": "4. International Tax & DTAA Advisory", "description": "Advisory on Double Taxation Avoidance Agreements (DTAA) and navigating global tax jurisdictions."},
                    {"title": "5. FEMA, RBI, FDI, ODI Compliance", "description": "Regulatory compliance for Foreign Exchange Management Act, foreign direct investments, and outbound investments."},
                    {"title": "6. Global Minimum Tax (OECD) Compliance", "description": "Ensuring compliance with the latest OECD global tax frameworks (Pillar 1 & 2)."},
                    {"title": "7. Local Compliance", "description": "Handling all municipal and state-level statutory compliances efficiently."},
                    {"title": "8. International Compliance", "description": "Ensuring adherence to tax and legal norms in foreign jurisdictions where you operate."},
                    {"title": "9. Expatriate Taxation & NRI Services", "description": "Specialized tax services for NRIs and expatriates working across borders."}
                ]
            },
            {
                "title": "Corporate Legal & Secretarial",
                "slug": "corporate-legal",
                "icon": "Scale",
                "short_description": "Company incorporation, licensing, and legal advisory services.",
                "sub_services": [
                    {"title": "1. Registration & Company Incorporation", "description": "Formation of Pvt Ltd, LLP, OPC, Public companies, Trusts, Societies, Section 8 NGOs, and Producer Companies."},
                    {"title": "2. Other Licenses", "description": "Obtaining essential business licenses like IEC, FSSAI, RERA, Shops & Establishment, Trade License, and Startup India registration."},
                    {"title": "3. Corporate Governance & ROC Filings", "description": "Regular filings with the Registrar of Companies (ROC), maintaining minutes, and governance audits."},
                    {"title": "4. M&A, Corporate Restructuring & Valuations", "description": "Advisory on Mergers, Acquisitions, demergers, and providing certified business valuations."},
                    {"title": "5. Due Diligence & Legal Compliance", "description": "Comprehensive legal health checks and due diligence for investments or takeovers."},
                    {"title": "6. Insolvency & Bankruptcy Advisory", "description": "Strategic advisory under the IBC code for insolvency resolution and liquidation processes."},
                    {"title": "7. Contract Drafting & Legal Advisory", "description": "Drafting and vetting robust legal contracts, agreements, and providing general legal counsel."}
                ]
            },
            {
                "title": "Fundraising & Capital Advisory",
                "slug": "fundraising-capital",
                "icon": "Coins",
                "short_description": "Support for Seed, Angel, VC fundraising, and IPO advisory.",
                "sub_services": [
                    {"title": "1. Startup Fundraising", "description": "Connecting startups with the right Seed, Angel, Venture Capital (VC), and Private Equity (PE) investors."},
                    {"title": "2. Financial Modelling & Business Valuation", "description": "Creating detailed financial projections, DCF models, and valuation reports for fundraising."},
                    {"title": "3. Pitch Decks & Investor Readiness", "description": "Crafting compelling investor pitch decks and preparing founders for due diligence."},
                    {"title": "4. Debt Syndication & Project Finance", "description": "Arranging large-scale project finance, working capital loans, and debt syndication."},
                    {"title": "5. IPO & SME IPO Advisory", "description": "Guiding companies through the complex process of listing on Mainboard or SME exchanges."},
                    {"title": "6. Incubation Services", "description": "Providing infrastructure and mentoring support for early-stage startups."},
                    {"title": "7. Retail Loans", "description": "Assistance with securing home, business, vehicle, and personal loans."}
                ]
            },
            {
                "title": "Wealth & Investment Advisory",
                "slug": "wealth-investment",
                "icon": "PieChart",
                "short_description": "Portfolio management, estate planning, and risk advisory.",
                "sub_services": [
                    {"title": "1. Wealth & Portfolio Management", "description": "Tailored investment strategies for High Net Worth Individuals (HNIs) to preserve and grow wealth."},
                    {"title": "2. Mutual Funds, Equities & Alternative Investments", "description": "Advisory on a diverse mix of assets including stocks, mutual funds, AIFs, and commodities."},
                    {"title": "3. Real Estate Advisory & Transaction Support", "description": "End-to-end support for buying, selling, managing, and valuing real estate assets."},
                    {"title": "4. Retail Loans", "description": "Facilitating quick approvals for personal and business financing needs."},
                    {"title": "5. Insurance & Risk Advisory", "description": "Comprehensive risk assessment and planning for life, health, and general insurance coverage."},
                    {"title": "6. Succession & Estate Planning", "description": "Structuring wills, trusts, and family constitutions to ensure smooth transfer of intergenerational wealth."}
                ]
            },
            {
                "title": "Startup & Incubation Support",
                "slug": "startup-incubation",
                "icon": "Rocket",
                "short_description": "End-to-end support for startups from incorporation to exit.",
                "sub_services": [
                    {"title": "1. Startup Incorporation & Compliance", "description": "Setting up the legal entity, obtaining DIPP recognition, and managing initial compliances."},
                    {"title": "2. Virtual CFO for Startups", "description": "Fractional financial leadership to manage burn rate, runway, and unit economics for early-stage companies."},
                    {"title": "3. Growth Strategy & Business Planning", "description": "Developing go-to-market strategies, business models, and scaling roadmaps."},
                    {"title": "4. Pitch Preparation & Investor Access", "description": "Refining the startup narrative and providing access to a network of potential investors."},
                    {"title": "5. Mentorship & Networking", "description": "Connecting founders with industry veterans, mentors, and peer networks."},
                    {"title": "6. Technology & Automation Support", "description": "Advising on the right tech stack and automation tools to streamline startup operations."}
                ]
            },
            {
                "title": "Tech-Enabled Solutions",
                "slug": "tech-solutions",
                "icon": "Cpu",
                "short_description": "AI, Blockchain, and RPA tools for financial automation.",
                "sub_services": [
                    {"title": "1. AI-Powered Accounting Tools", "description": "Implementing automated categorization, invoice processing, and reconciliation using Artificial Intelligence."},
                    {"title": "2. Blockchain based Audit & Compliance", "description": "Utilizing immutable ledger technology for transparent and tamper-proof audit trails."},
                    {"title": "3. RPA-Driven Automation in Finance", "description": "Deploying Robotic Process Automation bots for repetitive tasks like data entry and report generation."},
                    {"title": "4. Data Analytics, Forecasting & BI Dashboard", "description": "Building interactive Business Intelligence dashboards for real-time financial insights."},
                    {"title": "5. ERP / FinTech Integration", "description": "Seamless integration services for SAP, Zoho, Tally, Oracle, and Microsoft Dynamics."},
                    {"title": "6. Digital Transformation Advisory", "description": "Guiding traditional finance teams through the adoption of modern digital tools and workflows."}
                ]
            }
        ]

        for service_data in services_data:
            # Create Main Service
            service = Service.objects.create(
                title=service_data['title'],
                slug=service_data['slug'],
                icon=service_data['icon'],
                short_description=service_data['short_description'],
                full_description="Detailed breakdown of our specialized offerings in this domain." # Generic intro
            )
            
            # Create Sub-Services
            for index, sub in enumerate(service_data['sub_services']):
                ServiceSubService.objects.create(
                    service=service,
                    title=sub['title'],
                    description=sub['description'],
                    order=index
                )
            
            self.stdout.write(f"   ✅ Created Service: {service.title} with {len(service_data['sub_services'])} sub-points")

        self.stdout.write(self.style.SUCCESS('\n🎉 All Services & Detailed Sub-points Seeded Successfully!'))