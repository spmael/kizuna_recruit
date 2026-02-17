from apps.recruit.models.cv import CV
from apps.recruit.models.cv_translation import CVTranslation
from apps.recruit.models.education import Education
from apps.recruit.models.education_translation import EducationTranslation
from apps.recruit.models.skill import Skill
from apps.recruit.models.work_experience import WorkExperience
from apps.recruit.models.work_experience_translation import WorkExperienceTranslation

__all__ = [
    "CV",
    "CVTranslation",
    "WorkExperience",
    "WorkExperienceTranslation",
    "Education",
    "EducationTranslation",
    "Skill",
]
