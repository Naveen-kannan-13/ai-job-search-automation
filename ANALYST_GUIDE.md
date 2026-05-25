# Data Analyst & Business Analyst Job Automation

Specialized job hunting automation for **Data Analyst** and **Business Analyst** roles.

## 🎯 What This Does

Automatically finds and tracks analyst positions matching your profile:
- **Data Analyst**: SQL, Python, Analytics tools (Tableau, Power BI)
- **Business Analyst**: Requirements gathering, process improvement, stakeholder management
- **Hybrid Roles**: Combination of both skill sets

## 🚀 Quick Start

### 1. Customize Your Analyst Profile

Choose which analyst roles you want to target:

```python
# Option A: Pure Data Analyst
from analyst_scraper import AnalystProfileBuilder
profile = AnalystProfileBuilder.create_data_analyst_profile()

# Option B: Pure Business Analyst
profile = AnalystProfileBuilder.create_business_analyst_profile()

# Option C: Hybrid (Data + Business)
profile = AnalystProfileBuilder.create_hybrid_analyst_profile()
```

### 2. Run the Analyst Job Search

```bash
python analyst_scraper.py
```

This will:
1. ✓ Search for analyst positions
2. ✓ Match jobs to your skills (SQL, Python, Tableau, etc.)
3. ✓ Filter by match score (50%+ by default)
4. ✓ Save to `analyst_applications.xlsx`

### 3. Review Results

Open **`analyst_applications.xlsx`** to see:
- Jobs ranked by match score
- Which analyst skills are required
- Company details and application links
- Your notes and application status

## 💼 Analyst Skills We Look For

### Data Analyst Skills (60 skills tracked)
```
SQL, Python, R, Tableau, Power BI, Looker
Excel, VBA, Google Sheets
Statistics, A/B Testing, Forecasting, Regression
Data Analysis, Data Visualization, Dashboards
Google Analytics, BigQuery, Snowflake, Redshift
```

### Business Analyst Skills (45 skills tracked)
```
Business Analysis, Requirements Gathering
Process Improvement, Workflow Analysis
Stakeholder Management, Documentation
JIRA, CRM Systems (Salesforce, HubSpot)
SQL, Excel, Data Analysis, Communication
```

### Tools We Target
```
Tableau      - Data visualization
Power BI     - Business intelligence
SQL Server   - Database queries
PostgreSQL   - Database management
Looker       - Analytics platform
Excel        - Spreadsheet analysis
Python/R     - Statistical analysis
Google Analytics - Web analytics
JIRA         - Project management
Salesforce   - CRM system
```

## 📊 Match Score Explained

Jobs are scored 0-100% based on:

| Level | Score | Description |
|-------|-------|-------------|
| 🟢 Excellent | 80-100% | Strong match - Apply immediately |
| 🟡 Good | 60-79% | Good fit - Worth applying |
| 🟠 Fair | 40-59% | Some skills match - Consider applying |
| 🔴 Poor | <40% | Limited match - Development needed |

**How Scored:**
- **Skill Match (60%)**: How many of your tools are mentioned
- **Title Match (25%)**: How well the role matches analyst titles
- **Experience Match (15%)**: Experience level alignment

### Example Scoring

**Your Profile:**
- Mid-level analyst
- Skills: SQL, Python, Tableau, Excel, Statistics
- Roles: Data Analyst, Business Analyst

**Job: "Mid-level Data Analyst - SQL & Tableau"**
- Has SQL ✓, Tableau ✓, Python ✗, Excel ✗ = 2/5 skills
- Title matches "Data Analyst" ✓
- Experience Mid-level aligned ✓
- **Score: ~72% (GOOD FIT)** 🟡

## 🔧 Custom Setup

### Add Jobs From Specific Companies

```python
from analyst_scraper import AnalystJobScraper

scraper = AnalystJobScraper(min_match_score=60)

# Add your own job listings
my_jobs = [
    {
        'title': 'Senior Data Analyst - Python & Tableau',
        'link': 'https://example.com/jobs/123',
        'description': 'Looking for data analyst with Python and Tableau',
        'company': 'Google'
    },
    {
        'title': 'Business Analyst - SQL & JIRA',
        'link': 'https://example.com/jobs/456',
        'description': 'Requirements gathering and process improvement',
        'company': 'Microsoft'
    }
]

scraper.add_custom_job_sources(my_jobs)
matched = scraper.match_and_filter_jobs()
scraper.apply_to_matches(matched)
```

### Adjust Match Threshold

```python
# Only show high-quality matches
scraper = AnalystJobScraper(min_match_score=70)

# Show all positions with any match
scraper = AnalystJobScraper(min_match_score=30)
```

### Target Specific Analyst Type

```python
from analyst_scraper import AnalystProfileBuilder, JobMatcher

# Get profile for your target role
profile = AnalystProfileBuilder.create_data_analyst_profile()

# Use with job matcher
matcher = JobMatcher(profile)
```

## 📈 Tips for Data & Business Analysts

### Resume Tips

When creating your resume, emphasize:

**For Data Analyst roles:**
- Specific SQL queries you've written
- Dashboards/reports you've created (Tableau, Power BI)
- A/B tests you've ran
- Python/R scripts for automation
- Business impact (e.g., "Reduced report time by 40%")

**For Business Analyst roles:**
- Requirements documents delivered
- Process improvements implemented
- Stakeholder management experience
- Number of requirements gathered/analyzed
- Tools used (JIRA, Confluence, etc.)

**For Hybrid roles:**
- Balance both technical and process skills
- Show ability to bridge business and data teams

### LinkedIn Optimization

- Use keywords: "SQL", "Python", "Tableau", "Data Analysis"
- Include analyst tools in your skills
- Pin your most impressive analysis work

### Application Strategy

1. **Excellent Match (80%+)**: Apply immediately with personalized cover letter
2. **Good Match (60-79%)**: Apply with details about your relevant skills
3. **Fair Match (40-59%)**: Apply if you're interested in development
4. **Poor Match (<40%)**: Skip and focus on better fits

## 🎓 Skill Development Resources

Need to level up your skills?

**SQL & Databases:**
- LeetCode SQL
- HackerRank SQL
- Mode Analytics SQL Tutorial

**Python for Data Analysis:**
- Real Python (realpython.com)
- DataCamp
- Kaggle Learn

**Tableau & Power BI:**
- Tableau Public Gallery (learn by example)
- Microsoft Learn (Power BI)
- YouTube tutorials

**Statistics & A/B Testing:**
- Khan Academy (Statistics)
- A/B Testing by Google (free course)

**Business Analysis:**
- Bridging the BA Knowledge Gap (book)
- IIBA CCBA certification prep
- Requirements elicitation techniques

## 📊 Tracking Applications

The system creates `analyst_applications.xlsx` with:

| Column | Purpose |
|--------|---------|
| Company | Which company |
| Position | Job title |
| Link | Application URL |
| Match Score % | Relevance percentage |
| Status | Applied/Interview/Rejected |
| Date Applied | When you applied |
| Notes | Skills matched/missing |

**Status Options:**
- Pending Review (default)
- Applied
- Interview Scheduled
- Interview Completed
- Offer Received
- Rejected
- Withdrawn

## 🔄 Workflow

```
1. Run analyst_scraper.py
   ↓
2. Review matched jobs in Excel
   ↓
3. Update Job Link in your resume
   ↓
4. Apply to jobs manually (or auto-apply if configured)
   ↓
5. Update status in Excel as you progress
   ↓
6. Track which strategies work
   ↓
7. Re-run weekly for new opportunities
```

## ⚙️ Advanced Configuration

### Add Multiple Job Sources

```python
scraper = AnalystJobScraper()

# Add jobs from different sources
stripe_jobs = scraper.scrape_stripe_analyst_jobs()
# linkedin_jobs = scraper.scrape_linkedin_analysts()
# indeed_jobs = scraper.scrape_indeed_analysts()
# custom_jobs = scraper.scrape_via_api()

scraper.match_and_filter_jobs()
```

### Schedule Automated Search

**Windows Task Scheduler:**
1. Open Task Scheduler
2. Create task to run: `python C:\Users\Navee\Documents\Job Project\analyst_scraper.py`
3. Set to daily at 9 AM

**Mac/Linux Cron:**
```bash
0 9 * * 1-5 cd ~/Job\ Project && python analyst_scraper.py
# Runs weekdays at 9 AM
```

## 🆘 Troubleshooting

### No analyst jobs found
- Check internet connection
- Wait 30 seconds and try again
- Job listings may be empty on Stripe

### Low match scores
- Add skills to your Excel/profile
- Lower the `min_match_score` threshold
- Update your resume with more analyst skills

### Excel file won't open
- Close it first if already open
- Ensure you have Excel or LibreOffice installed
- Check file permissions

## 📚 Additional Resources

- **README.md** - Full system documentation
- **GETTING_STARTED.md** - Setup instructions
- **job_matcher.py** - Understand scoring logic
- **application_tracker.py** - Excel file structure

## Next Steps

1. ✅ Run `python analyst_scraper.py`
2. ✅ Review results in Excel
3. ✅ Customize profiles as needed
4. ✅ Apply to matched positions
5. ✅ Re-run weekly for new opportunities

Good luck with your analyst job search! 🎯📊
