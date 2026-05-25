#!/usr/bin/env python3
"""
Add Sample Analyst Jobs to the Scraper
Run this to populate jobs from popular companies
"""

from analyst_scraper import AnalystJobScraper

def add_sample_analyst_jobs():
    """Add popular analyst job listings."""
    
    scraper = AnalystJobScraper(min_match_score=50)
    
    # Real analyst job examples (these would come from LinkedIn, Indeed, etc.)
    analyst_jobs = [
        {
            'title': 'Senior Data Analyst - SQL & Tableau',
            'link': 'https://linkedin.com/jobs/data-analyst-1',
            'description': 'Senior data analyst with SQL, Tableau, and dashboard development',
            'company': 'Google'
        },
        {
            'title': 'Business Analyst - Operations',
            'link': 'https://linkedin.com/jobs/business-analyst-1',
            'description': 'Operations analyst for process improvement and JIRA',
            'company': 'Microsoft'
        },
        {
            'title': 'Data Analyst - Python & Power BI',
            'link': 'https://linkedin.com/jobs/data-analyst-2',
            'description': 'Data analyst using Python, SQL, and Power BI dashboards',
            'company': 'Amazon'
        },
        {
            'title': 'Analytics Engineer - Data Pipeline',
            'link': 'https://linkedin.com/jobs/analytics-1',
            'description': 'Analytics engineer with SQL, Python, and BigQuery experience',
            'company': 'Stripe'
        },
        {
            'title': 'Business Intelligence Analyst',
            'link': 'https://linkedin.com/jobs/bi-analyst-1',
            'description': 'BI analyst with Tableau, SQL, and reporting expertise',
            'company': 'Apple'
        },
        {
            'title': 'Product Analyst - A/B Testing',
            'link': 'https://linkedin.com/jobs/product-analyst-1',
            'description': 'Product analyst for A/B testing and data-driven decisions',
            'company': 'Meta'
        },
        {
            'title': 'Financial Analyst - Excel & Reporting',
            'link': 'https://linkedin.com/jobs/financial-analyst-1',
            'description': 'Financial analyst with Excel, VBA, and forecasting',
            'company': 'Goldman Sachs'
        },
        {
            'title': 'Marketing Analyst - Google Analytics',
            'link': 'https://linkedin.com/jobs/marketing-analyst-1',
            'description': 'Marketing analyst with SQL and Google Analytics',
            'company': 'Netflix'
        },
        {
            'title': 'Operations Analyst - Process Improvement',
            'link': 'https://linkedin.com/jobs/ops-analyst-1',
            'description': 'Ops analyst for workflow optimization and reporting',
            'company': 'Tesla'
        },
        {
            'title': 'Data Analyst - Healthcare',
            'link': 'https://linkedin.com/jobs/healthcare-analyst-1',
            'description': 'Data analyst for healthcare KPI tracking and dashboards',
            'company': 'CVS Health'
        },
        {
            'title': 'Senior Business Analyst - Requirements',
            'link': 'https://linkedin.com/jobs/ba-senior-1',
            'description': 'Senior BA for requirements gathering and JIRA management',
            'company': 'Salesforce'
        },
        {
            'title': 'Data Analyst - E-commerce',
            'link': 'https://linkedin.com/jobs/ecom-analyst-1',
            'description': 'E-commerce analyst with SQL, Python, and Tableau',
            'company': 'Shopify'
        }
    ]
    
    print("\n" + "="*100)
    print("📊 ADDING SAMPLE ANALYST JOBS")
    print("="*100)
    print(f"\nAdding {len(analyst_jobs)} analyst jobs...\n")
    
    # Add all jobs
    scraper.add_custom_job_sources(analyst_jobs)
    
    # Match and display
    print("\n🔍 MATCHING JOBS TO YOUR PROFILE...\n")
    matched_jobs = scraper.match_and_filter_jobs()
    
    # Apply to matches
    if matched_jobs:
        print(f"\n✅ Found {len(matched_jobs)} matching jobs!")
        scraper.apply_to_matches(matched_jobs)
    else:
        print("\n⚠️  No jobs matched. Try lowering the match threshold.")
    
    print("\n" + "="*100)
    print("✓ Complete! Check analyst_applications.xlsx for results")
    print("="*100 + "\n")


if __name__ == "__main__":
    add_sample_analyst_jobs()
