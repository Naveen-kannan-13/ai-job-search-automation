# Data Analyst & Business Analyst Job Automation

Specialized AI-assisted job hunting automation for **Data Analyst** and **Business Analyst** roles.

---

## 🎯 Overview

This project automates job searching and tracking workflows using Python, Visual Studio Code, and GitHub Copilot.

The system helps:
- search analyst jobs across platforms
- match jobs based on resume skills and keywords
- track applications in Excel
- reduce repetitive manual effort involved in job hunting

The workflow was built to streamline repetitive tasks involved in searching, filtering, organizing, and tracking job opportunities.

---

## 🤖 AI-Assisted Development

This project was developed using:
- GitHub Copilot
- Visual Studio Code
- AI-assisted workflow generation

GitHub Copilot was used to:
- speed up script development
- improve filtering and matching logic
- generate reusable code structures
- optimize repetitive coding tasks
- streamline automation workflows

---

## 🚀 What This Does

Automatically finds and tracks analyst positions matching your profile:
- **Data Analyst**: SQL, Python, Analytics tools (Tableau, Power BI)
- **Business Analyst**: Requirements gathering, process improvement, stakeholder management
- **Hybrid Roles**: Combination of both skill sets

---

## 🚀 Features

- Automated job search workflow
- Resume and job description matching
- Keyword-based filtering
- Match scoring system
- Excel-based application tracking
- AI-assisted workflow development using GitHub Copilot
- Structured job tracking workflow
- Automated filtering and prioritization

---

## ⚙️ Workflow

1. Search job listings across platforms
2. Filter jobs based on:
   - skills
   - experience
   - keywords
3. Match jobs with resume profile
4. Rank jobs using match score
5. Store results in Excel tracker
6. Review and apply manually

---

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

---

### 2. Run the Analyst Job Search

```bash
python analyst_scraper.py
```

This will:
1. ✓ Search for analyst positions
2. ✓ Match jobs to your skills
3. ✓ Filter by match score
4. ✓ Save results to `analyst_applications.xlsx`

---

### 3. Review Results

Open **`analyst_applications.xlsx`** to see:
- Jobs ranked by match score
- Required skills
- Company details
- Application links
- Tracking status

---

## 💼 Analyst Skills Covered

### Data Analyst Skills
```text
SQL, Python, Tableau, Power BI, Excel,
Statistics, Data Visualization, Dashboards,
Google Analytics, BigQuery, Snowflake
```

### Business Analyst Skills
```text
Business Analysis, Requirements Gathering,
Process Improvement, Stakeholder Management,
Workflow Analysis, Documentation, JIRA, CRM
```

---

## 📊 Match Score System

Jobs are scored based on:
- Skill Match
- Title Match
- Experience Match

| Level | Score |
|-------|-------|
| Excellent | 80-100% |
| Good | 60-79% |
| Fair | 40-59% |
| Poor | <40% |

---

## 🔧 Technologies Used

- Python
- Pandas
- Excel
- GitHub Copilot
- Visual Studio Code

---

## 📁 Project Files

| File | Purpose |
|------|---------|
| `run_analyst_search.py` | Runs the workflow |
| `analyst_scraper.py` | Handles job search and extraction |
| `job_matcher.py` | Matches jobs with profile |
| `application_tracker.py` | Tracks applications in Excel |

---

## 📊 Application Tracking

The workflow generates:
`analyst_applications.xlsx`

Tracks:
- Company
- Role
- Match Score
- Application Status
- Notes
- Links

---

## 🎯 Purpose

This project was built to:
- automate repetitive job searching tasks
- reduce manual tracking effort
- improve workflow efficiency
- explore AI-assisted automation workflows

---

## 🔄 Future Improvements

- Automatic email alerts
- Better matching algorithms
- Dashboard for tracking applications
- Integration with more job platforms

---

## ✅ Next Steps

1. Run `python analyst_scraper.py`
2. Review results in Excel
3. Apply to matched roles
4. Track applications
5. Re-run weekly for new opportunities
