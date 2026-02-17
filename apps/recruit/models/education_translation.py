from django.db import models


class EducationTranslation(models.Model):
    education = models.ForeignKey("recruit.Education", on_delete=models.CASCADE, related_name="translations")
    language = models.CharField(max_length=2, choices=[("fr", "Français"), ("en", "English")])
    school_name = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=80, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["education", "language"], name="uniq_education_language")
        ]

    def __str__(self) -> str:
        return f"{self.school_name} ({self.language})"
