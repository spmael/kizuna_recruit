from django.contrib import admin

from apps.recruit.models import CV, CVTranslation, Education, EducationTranslation, Skill, WorkExperience, WorkExperienceTranslation

admin.site.register(CV)
admin.site.register(CVTranslation)
admin.site.register(WorkExperience)
admin.site.register(WorkExperienceTranslation)
admin.site.register(Education)
admin.site.register(EducationTranslation)
admin.site.register(Skill)
