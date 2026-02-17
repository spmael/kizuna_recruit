from django.db import models


class WorkExperienceTranslation(models.Model):
    work_experience = models.ForeignKey(
        "recruit.WorkExperience", on_delete=models.CASCADE, related_name="translations"
    )
    language = models.CharField(max_length=2, choices=[("fr", "Français"), ("en", "English")])
    job_title = models.CharField(max_length=60)
    description = models.TextField(max_length=300, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["work_experience", "language"],
                name="uniq_work_experience_language",
            )
        ]

    def __str__(self) -> str:
        return f"{self.job_title} ({self.language})"
