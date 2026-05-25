#!/usr/bin/env python3
"""
Analyst Job Search Runner
Simple script to search for Data Analyst and Business Analyst roles.
Run this: python run_analyst_search.py
"""

from analyst_scraper import AnalystJobScraper, AnalystProfileBuilder
import sys


def main():
    """Run the analyst job search."""
    
    print("\n" + "="*100)
    print("📊 DATA ANALYST & BUSINESS ANALYST JOB SEARCH")
    print("="*100)
    
    # You can choose which profile to use:
    print("\nProfile: Hybrid Data + Business Analyst")
    print("Skills: SQL, Python, Tableau, Power BI, Excel, Statistics, Excel, JIRA, CRM")
    print("Experience: Mid-level (2-5 years)")
    print("Target: Data Analyst, Business Analyst, Analytics roles")
    
    try:
        # Initialize scraper
        scraper = AnalystJobScraper(min_match_score=50)
        
        # Run the search
        scraper.run_analyst_search()
        
        # Print results summary
        if scraper.scraped_jobs:
            print("\n" + "="*100)
            print("✅ SEARCH COMPLETE!")
            print("="*100)
            print(f"Searched: {len(scraper.scraped_jobs)} analyst positions")
            print(f"Matches: {len(scraper.tracker.applications)} positions matched")
            print(f"Output: analyst_applications.xlsx")
            print("\n📂 Next: Open analyst_applications.xlsx to review matches")
            print("="*100 + "\n")
        else:
            print("\n⚠️  No analyst positions found in current search sources.")
            print("Try again later or add more job sources in analyst_scraper.py")
            
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Check that all dependencies are installed: pip install -r requirements.txt")
        sys.exit(1)


if __name__ == "__main__":
    main()
