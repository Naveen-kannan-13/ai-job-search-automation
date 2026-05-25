#!/usr/bin/env python3
"""
Analyst Demo - See how the system works with sample analyst jobs.
Run this: python analyst_demo.py
"""

from analyst_scraper import AnalystJobScraper, AnalystProfileBuilder
from application_tracker import ApplicationTracker


def demo_analyst_matching():
    """Demonstrate analyst job matching with sample jobs."""
    
    print("\n" + "="*100)
    print("🔍 ANALYST JOB MATCHING DEMO")
    print("="*100)
    
    # Show the analyst profile
    print("\n📋 YOUR ANALYST PROFILE:")
    print("-" * 100)
    profile = AnalystProfileBuilder.create_hybrid_analyst_profile()
    print(f"Role: {profile['name']}")
    print(f"Experience: {profile['experience_level']}")
    print(f"Target Positions: {', '.join(profile['job_titles'][:5])}")
    print(f"Key Skills ({len(profile['skills'])} total): {', '.join(profile['skills'][:10])}...")
    print("-" * 100)
    
    # Create scraper
    scraper = AnalystJobScraper(min_match_score=40)
    scraper.scraped_jobs = [
        {
            'title': 'Senior Data Analyst - SQL & Python',
            'description': 'Looking for data analyst with SQL, Python, Tableau, and statistics background',
            'company': 'Google',
            'link': 'https://google.com/careers/analyst1'
        },
        {
            'title': 'Business Analyst - JIRA & Requirements',
            'description': 'Business analyst needed for requirements gathering, JIRA, process improvement',
            'company': 'Microsoft',
            'link': 'https://microsoft.com/jobs/analyst2'
        },
        {
            'title': 'Analytics Engineer - Data Pipeline',
            'description': 'Build data pipelines using SQL, Python, Kafka, BigQuery, and dashboards',
            'company': 'Stripe',
            'link': 'https://stripe.com/jobs/analyst3'
        },
        {
            'title': 'Product Analyst - A/B Testing',
            'description': 'Product analyst for A/B testing, SQL queries, and Power BI dashboards',
            'company': 'Amazon',
            'link': 'https://amazon.com/jobs/analyst4'
        },
        {
            'title': 'Financial Analyst - Excel & Forecasting',
            'description': 'Financial analyst role requiring Excel, VBA, forecasting, and reporting',
            'company': 'Goldman Sachs',
            'link': 'https://gs.com/jobs/analyst5'
        },
        {
            'title': 'Client Success Analyst - CRM',
            'description': 'Analyst role working with Salesforce, customer data, and reporting',
            'company': 'Salesforce',
            'link': 'https://salesforce.com/jobs/analyst6'
        },
        {
            'title': 'Marketing Analyst - Google Analytics',
            'description': 'Marketing analyst with Google Analytics, SQL, and dashboard creation',
            'company': 'Meta',
            'link': 'https://meta.com/jobs/analyst7'
        },
        {
            'title': 'Operations Analyst - Process Improvement',
            'description': 'Operations analyst for process improvement, workflow analysis, Excel',
            'company': 'UPS',
            'link': 'https://ups.com/jobs/analyst8'
        }
    ]
    
    # Match jobs
    print("\n🎯 MATCHING JOBS...\n")
    matched_jobs = scraper.match_and_filter_jobs()
    
    # Show detailed results
    print("\n📊 DETAILED MATCH BREAKDOWN:")
    print("-" * 100)
    
    for i, job in enumerate(matched_jobs, 1):
        print(f"\n{i}. {job['title']}")
        print(f"   Company: {job['company']}")
        print(f"   Match Score: {job['score']}% ({job['match_level']})")
        
        # Show matched skills
        if job['matched_skills']:
            print(f"   ✅ Your Skills Found: {', '.join(job['matched_skills'][:6])}")
        
        # Show missing skills
        if job['unmatched_skills']:
            print(f"   ⚠️  Skills to Develop: {', '.join(job['unmatched_skills'][:3])}")
        
        # Show match details
        details = []
        if job['title_match']:
            details.append("Title Match ✓")
        if job['experience_match']:
            details.append("Experience Match ✓")
        if details:
            print(f"   Factors: {', '.join(details)}")


def demo_tracking():
    """Demonstrate application tracking."""
    
    print("\n\n" + "="*100)
    print("📊 APPLICATION TRACKING DEMO")
    print("="*100)
    
    tracker = ApplicationTracker("demo_analyst_applications.xlsx")
    
    sample_applications = [
        {
            'company': 'Google',
            'position': 'Senior Data Analyst',
            'link': 'https://google.com/careers/analyst1',
            'score': 88,
            'status': 'Applied',
            'notes': 'Strong match: SQL, Python, Tableau all listed'
        },
        {
            'company': 'Microsoft',
            'position': 'Business Analyst',
            'link': 'https://microsoft.com/jobs/analyst2',
            'score': 82,
            'status': 'Interview Scheduled',
            'notes': 'Excellent match: JIRA, requirements gathering experience'
        },
        {
            'company': 'Stripe',
            'position': 'Analytics Engineer',
            'link': 'https://stripe.com/jobs/analyst3',
            'score': 91,
            'status': 'Applied',
            'notes': 'Outstanding match: Data pipeline skills'
        },
        {
            'company': 'Amazon',
            'position': 'Product Analyst',
            'link': 'https://amazon.com/jobs/analyst4',
            'score': 75,
            'status': 'Applied',
            'notes': 'Good match: A/B testing and SQL'
        },
        {
            'company': 'Goldman Sachs',
            'position': 'Financial Analyst',
            'link': 'https://gs.com/jobs/analyst5',
            'score': 68,
            'status': 'Pending Review',
            'notes': 'Fair match: Excel and forecasting'
        }
    ]
    
    print("\n📝 Adding sample applications...")
    for app in sample_applications:
        tracker.add_application(
            company=app['company'],
            position=app['position'],
            link=app['link'],
            match_score=app['score'],
            status=app['status'],
            notes=app['notes']
        )
        print(f"  ✓ {app['company']}: {app['position']} ({app['score']}%)")
    
    print("\n💾 Saving to Excel...")
    tracker.save_to_excel()
    
    print("\n📊 Summary Statistics:")
    tracker.print_summary()
    
    print("-" * 100)
    print("✅ Demo application tracking saved to: demo_analyst_applications.xlsx")
    print("-" * 100)


def main():
    """Run both demos."""
    
    print("\n")
    print("╔" + "="*98 + "╗")
    print("║" + " "*25 + "ANALYST JOB SEARCH - LIVE DEMO" + " "*43 + "║")
    print("║" + " "*20 + "See how the system matches analyst jobs" + " "*39 + "║")
    print("╚" + "="*98 + "╝")
    
    # Run demos
    demo_analyst_matching()
    demo_tracking()
    
    print("\n" + "="*100)
    print("✅ DEMO COMPLETE!")
    print("="*100)
    print("\n🚀 NEXT STEPS:")
    print("1. Review demo output above")
    print("2. Check demo_analyst_applications.xlsx to see tracking format")
    print("3. Ready? Run: python run_analyst_search.py")
    print("4. Provide your own analyst jobs in analyst_scraper.py")
    print("\n📖 More info: Read ANALYST_GUIDE.md for detailed instructions")
    print("="*100 + "\n")


if __name__ == "__main__":
    demo_analyst_matching()
    demo_tracking()
