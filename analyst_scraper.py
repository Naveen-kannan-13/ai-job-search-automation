"""
Analyst-specific job scraper and matcher for Data Analyst and Business Analyst roles.
"""
import requests
from bs4 import BeautifulSoup
from job_matcher import JobMatcher
from application_tracker import ApplicationTracker


class AnalystJobScraper:
    """Specialized scraper for Data Analyst and Business Analyst positions."""
    
    # Skills specific to analyst roles
    ANALYST_SKILLS = {
        # Data Analysis & SQL
        'sql', 'python', 'r', 'tableau', 'power bi', 'looker',
        
        # Excel & Spreadsheets
        'excel', 'vba', 'spreadsheet', 'pivot tables',
        
        # Statistics & Analytics
        'statistics', 'statistical analysis', 'a/b testing', 'ab testing',
        'data analysis', 'data analytics', 'forecasting', 'regression',
        'hypothesis testing', 'quantitative analysis',
        
        # Business Skills
        'business analysis', 'requirements gathering', 'process improvement',
        'stakeholder management', 'workflow analysis', 'business process',
        'business intelligence', 'bi', 'etl', 'data warehouse',
        
        # CRM & Tools
        'salesforce', 'hubspot', 'crm', 'google analytics', 'analytics',
        'jira', 'sql server', 'postgres', 'postgresql', 'mysql',
        
        # Communication
        'data visualization', 'dashboards', 'reporting', 'presentations',
        'communication', 'documentation',
        
        # Additional
        'google sheets', 'bigquery', 'snowflake', 'redshift', 'dax',
        'sap', 'oracle', 'nosql', 'mongodb', 'json', 'xml'
    }
    
    # Analyst job titles to look for
    ANALYST_TITLES = [
        'data analyst', 'business analyst', 'analytics engineer',
        'senior data analyst', 'senior business analyst',
        'junior data analyst', 'junior business analyst',
        'financial analyst', 'business intelligence analyst',
        'product analyst', 'marketing analyst', 'sales analyst',
        'operations analyst', 'data engineer', 'analytics specialist'
    ]
    
    def __init__(self, min_match_score=50):
        """
        Initialize analyst-focused job scraper.
        
        Args:
            min_match_score (int): Minimum match score for job filtering
        """
        self.min_match_score = min_match_score
        self.scraped_jobs = []
        self.tracker = ApplicationTracker('analyst_applications.xlsx')
        
        # Create analyst-focused profile
        self.profile = {
            'skills': list(self.ANALYST_SKILLS),
            'experience_level': 'Mid',
            'job_titles': self.ANALYST_TITLES
        }
        
        self.matcher = JobMatcher(self.profile)
        print("✓ Analyst Job Scraper initialized")
        print(f"  Tracking {len(self.ANALYST_SKILLS)} analyst-specific skills")
        print(f"  Targeting {len(self.ANALYST_TITLES)} analyst roles")
    
    def scrape_stripe_analyst_jobs(self):
        """Scrape analyst positions from Stripe careers (if available)."""
        print("\n📋 Checking Stripe for analyst positions...")
        
        url = "https://jobs.lever.co/stripe"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, "html.parser")
            jobs = soup.find_all("div", class_="posting")
            
            for job in jobs:
                try:
                    title_elem = job.find("h5") or job.find("a")
                    title = title_elem.text.strip() if title_elem else "Unknown"
                    
                    # Filter for analyst-related positions
                    if self._is_analyst_job(title):
                        link_elem = job.find("a", href=True)
                        link = link_elem["href"] if link_elem else "#"
                        
                        job_data = {
                            'title': title,
                            'link': link,
                            'description': '',
                            'company': 'Stripe',
                            'source': 'Lever'
                        }
                        
                        self.scraped_jobs.append(job_data)
                
                except Exception as e:
                    continue
            
            if self.scraped_jobs:
                print(f"✓ Found {len(self.scraped_jobs)} analyst positions at Stripe")
            else:
                print("ℹ No analyst positions currently posted at Stripe")
            
            return self.scraped_jobs
        
        except requests.RequestException as e:
            print(f"✗ Error scraping Stripe: {e}")
            return []
    
    def add_custom_job_sources(self, jobs_list):
        """
        Add jobs from custom sources (manual or other scrapers).
        
        Args:
            jobs_list (list): List of jobs with {title, link, description, company}
        """
        print(f"\n📥 Adding {len(jobs_list)} jobs from custom sources...")
        
        for job in jobs_list:
            if self._is_analyst_job(job.get('title', '')):
                self.scraped_jobs.append(job)
        
        print(f"✓ Added {len(jobs_list)} potential analyst jobs")
    
    def _is_analyst_job(self, job_title):
        """Check if job title matches analyst roles."""
        title_lower = job_title.lower()
        
        analyst_keywords = [
            'analyst', 'analytics', 'data', 'business intelligence', 'bi'
        ]
        
        return any(keyword in title_lower for keyword in analyst_keywords)
    
    def match_and_filter_jobs(self):
        """Match and filter jobs for analyst roles."""
        if not self.scraped_jobs:
            print("⚠️  No jobs to match")
            return []
        
        print(f"\n🔍 Matching {len(self.scraped_jobs)} jobs to analyst profile...")
        
        matched_jobs = self.matcher.filter_jobs(self.scraped_jobs, self.min_match_score)
        
        print(f"✓ Found {len(matched_jobs)} matching analyst positions:")
        print("-" * 100)
        
        for i, job in enumerate(matched_jobs, 1):
            print(f"\n{i}. {job['title']}")
            print(f"   Company: {job.get('company', 'Unknown')}")
            print(f"   Match Score: {job['score']}% ({job['match_level']})")
            print(f"   Required Skills Found: {', '.join(job['matched_skills'][:5])}")
            if job['unmatched_skills']:
                print(f"   Skills to Develop: {', '.join(job['unmatched_skills'][:3])}")
            print(f"   Link: {job['link']}")
        
        print("-" * 100)
        return matched_jobs
    
    def apply_to_matches(self, matched_jobs):
        """Track matched analyst jobs in Excel."""
        print(f"\n📝 Tracking {len(matched_jobs)} matched positions...")
        
        for job in matched_jobs:
            notes = f"Skills: {', '.join(job['matched_skills'][:5])}"
            
            self.tracker.add_application(
                company=job.get('company', 'Unknown'),
                position=job['title'],
                link=job['link'],
                match_score=job['score'],
                status="Pending Review",
                notes=notes
            )
        
        self.tracker.save_to_excel()
        self.tracker.print_summary()
        
        print(f"\n✅ Results saved to: analyst_applications.xlsx")
    
    def run_analyst_search(self):
        """Run complete analyst job search workflow."""
        print("\n" + "="*100)
        print("🔎 ANALYST JOB SEARCH & MATCHING")
        print("="*100)
        
        # Scrape analyst jobs
        self.scrape_stripe_analyst_jobs()
        
        # Match jobs
        if self.scraped_jobs:
            matched_jobs = self.match_and_filter_jobs()
            
            # Apply to matches
            if matched_jobs:
                self.apply_to_matches(matched_jobs)
            else:
                print("\n⚠️  No jobs met the match threshold")
        
        print("\n✓ Search complete!")


class AnalystProfileBuilder:
    """Build and manage analyst-specific profiles."""
    
    @staticmethod
    def create_data_analyst_profile():
        """Create a profile for Data Analyst roles."""
        return {
            'name': 'Data Analyst',
            'skills': [
                'sql', 'python', 'tableau', 'power bi', 'excel', 'statistics',
                'a/b testing', 'data analysis', 'google analytics', 'dashboards',
                'reporting', 'communication', 'postgresql', 'bigquery'
            ],
            'experience_level': 'Mid',
            'job_titles': [
                'data analyst', 'analytics engineer', 'product analyst',
                'business intelligence analyst', 'financial analyst'
            ],
            'description': 'Focused on data analysis, SQL, visualization, and reporting'
        }
    
    @staticmethod
    def create_business_analyst_profile():
        """Create a profile for Business Analyst roles."""
        return {
            'name': 'Business Analyst',
            'skills': [
                'business analysis', 'requirements gathering', 'process improvement',
                'stakeholder management', 'jira', 'sql', 'excel', 'data analysis',
                'communication', 'documentation', 'workflow analysis', 'crm'
            ],
            'experience_level': 'Mid',
            'job_titles': [
                'business analyst', 'senior business analyst', 'product analyst',
                'operations analyst', 'sales analyst'
            ],
            'description': 'Focused on business processes, requirements, and stakeholder management'
        }
    
    @staticmethod
    def create_hybrid_analyst_profile():
        """Create a profile for hybrid Data + Business Analyst roles."""
        return {
            'name': 'Data & Business Analyst',
            'skills': [
                'sql', 'python', 'tableau', 'power bi', 'excel', 'statistics',
                'business analysis', 'requirements gathering', 'data analysis',
                'a/b testing', 'dashboards', 'reporting', 'communication',
                'crm', 'google analytics', 'jira', 'process improvement'
            ],
            'experience_level': 'Mid',
            'job_titles': [
                'data analyst', 'business analyst', 'analytics engineer',
                'product analyst', 'business intelligence analyst',
                'operations analyst', 'financial analyst'
            ],
            'description': 'Hybrid role combining data analysis and business expertise'
        }


if __name__ == "__main__":
    # Example: Run analyst job search
    scraper = AnalystJobScraper(min_match_score=50)
    scraper.run_analyst_search()
    
    # Example: Manually add jobs
    custom_jobs = [
        {
            'title': 'Senior Data Analyst - Python & SQL',
            'link': 'https://example.com/job1',
            'description': 'Looking for data analyst with Python and SQL expertise',
            'company': 'TechCorp'
        }
    ]
    # scraper.add_custom_job_sources(custom_jobs)
    # scraper.match_and_filter_jobs()
