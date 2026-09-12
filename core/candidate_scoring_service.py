from core.certification_matching_service import CertificationMatchingService
from core.education_matching_service import EducationMatchingService
from core.embeddings_service import EmbeddingsService
from core.project_matching_service import ProjectMatchingService
from core.experience_matching_service import ExperienceMatchingService
from core.skill_matching_service import SkillMatchingService

class CandidateScoringService():

    """A blueprint for scoring the final match of candidate against the JD"""

    def __init__(self): 
        self.skill_service = SkillMatchingService() 
        self.experience_service = ExperienceMatchingService() 
        self.project_service = ProjectMatchingService() 
        self.education_service = EducationMatchingService() 
        self.certification_service = CertificationMatchingService()

    def calculate_score(self, jd, candidate) -> float: 
        skill_score = self.skill_service.calculate_skill_score(jd.required_skills, candidate.skills,25) 
        preferred_skill_score = self.skill_service.calculate_skill_score(jd.preferred_skills,candidate.skills,15)
        experience_score = self.experience_service.calculate_experience_score(jd.minimum_experience_years, candidate.experience) 
        project_score = self.project_service.calculate_project_score(jd.responsibilities, candidate.projects) 
        #education_score = self.education_service.calculate_education_score(jd.education, candidate.education) 
        certification_score = self.certification_service.calculate_certification_score(jd.certifications, candidate.certifications)
        total_score = skill_score + preferred_skill_score + experience_score + project_score + certification_score
        return total_score

