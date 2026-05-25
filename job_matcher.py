"""
Job matcher module for matching job postings to resume qualifications.
"""
from difflib import SequenceMatcher


class JobMatcher:
    """Match job postings to resume profile."""
    
    def __init__(self, profile):
        """
        Initialize the job matcher with a resume profile.
        
        Args:
            profile (dict): Resume profile from ResumeParser.get_profile()
        """
        self.profile = profile
        self.skills = set(s.lower() for s in profile['skills'])
        self.experience_level = profile['experience_level']
        self.job_titles = set(t.lower() for t in profile['job_titles'])
    
    def match_job(self, job_posting):
        """
        Score a job posting against the resume (0-100).
        
        Args:
            job_posting (dict): Job with 'title' and 'description'
        
        Returns:
            dict: Match score and reasoning
        """
        score = 0
        matched_skills = []
        unmatched_skills = []
        
        job_text = (job_posting.get('title', '') + ' ' + 
                   job_posting.get('description', '')).lower()
        
        # Skill matching (max 60 points)
        for skill in self.skills:
            if skill in job_text:
                matched_skills.append(skill)
                score += 5  # Each matched skill: 5 points
            else:
                unmatched_skills.append(skill)
        
        # Title matching (max 25 points)
        title_match = self._match_title(job_posting.get('title', ''))
        score += title_match * 25
        
        # Experience level matching (max 15 points)
        exp_match = self._match_experience(job_text)
        score += exp_match * 15
        
        # Cap at 100
        score = min(score, 100)
        
        return {
            'score': int(score),
            'matched_skills': matched_skills,
            'unmatched_skills': unmatched_skills[:5],  # Show top 5 missing
            'title_match': title_match > 0,
            'experience_match': exp_match > 0,
            'match_level': self._score_to_level(score)
        }
    
    def _match_title(self, job_title):
        """Match job title to resume job titles."""
        job_title_lower = job_title.lower()
        
        for profile_title in self.job_titles:
            if profile_title in job_title_lower or job_title_lower in profile_title:
                return 1.0
        
        # Partial matches
        for profile_title in self.job_titles:
            similarity = SequenceMatcher(None, profile_title, job_title_lower).ratio()
            if similarity > 0.6:
                return similarity
        
        return 0.0
    
    def _match_experience(self, job_text):
        """Match experience level to job requirements."""
        experience_keywords = {
            'Senior': ['senior', 'lead', 'principal', '8+', '10+', '15+', 'years'],
            'Mid': ['mid-level', '4+', '5+', '6+', 'years'],
            'Junior': ['junior', 'entry-level', 'graduate', '0-2', '1-2', 'years']
        }
        
        profile_level = self.experience_level
        keywords = experience_keywords.get(profile_level, [])
        
        # Check if job has similar level indicators
        for keyword in keywords:
            if keyword in job_text:
                return 1.0
        
        # If no exact match, be flexible (0.5)
        return 0.5
    
    def _score_to_level(self, score):
        """Convert numeric score to match level."""
        if score >= 80:
            return 'Excellent'
        elif score >= 60:
            return 'Good'
        elif score >= 40:
            return 'Fair'
        else:
            return 'Poor'
    
    def filter_jobs(self, jobs, min_score=50):
        """
        Filter jobs that meet minimum score threshold.
        
        Args:
            jobs (list): List of job postings
            min_score (int): Minimum match score (0-100)
        
        Returns:
            list: Jobs that meet the threshold, sorted by score
        """
        matched_jobs = []
        
        for job in jobs:
            match_result = self.match_job(job)
            if match_result['score'] >= min_score:
                job_with_match = {**job, **match_result}
                matched_jobs.append(job_with_match)
        
        # Sort by score descending
        matched_jobs.sort(key=lambda x: x['score'], reverse=True)
        
        return matched_jobs


if __name__ == "__main__":
    # Test the matcher
    profile = {
        'skills': ['python', 'javascript', 'react'],
        'experience_level': 'Mid',
        'job_titles': ['frontend engineer', 'full stack developer']
    }
    
    matcher = JobMatcher(profile)
    
    test_job = {
        'title': 'Senior Frontend Engineer - React',
        'description': 'Looking for experienced React developer with Python knowledge'
    }
    
    result = matcher.match_job(test_job)
    print("Match result:", result)
