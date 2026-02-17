from django.db import models


class CVTranslation(models.Model):
    class Language(models.TextChoices):
        FRENCH = "fr", "Français"
        ENGLISH = "en", "English"

    cv = models.ForeignKey("recruit.CV", on_delete=models.CASCADE, related_name="translations")
    language = models.CharField(max_length=2, choices=Language.choices, default=Language.FRENCH)
    headline = models.CharField(max_length=80, blank=True)
    summary = models.TextField(max_length=400, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["cv", "language"], name="uniq_cv_language")
        ]

    def __str__(self) -> str:
        return f"{self.cv.full_name} ({self.language})"
