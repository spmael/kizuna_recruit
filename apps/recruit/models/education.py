from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Education(models.Model):
    class Level(models.TextChoices):
        PRIMARY = "primary", "Primaire"
        MIDDLE = "middle", "Collège (BEPC)"
        HIGH = "high", "Lycée (Probatoire / BAC)"
        UNIVERSITY = "university", "Université"
        VOCATIONAL = "vocational", "Formation professionnelle"
        OTHER = "other", "Autre"

    cv = models.ForeignKey("recruit.CV", on_delete=models.CASCADE, related_name="educations")
    level = models.CharField(max_length=20, choices=Level.choices, blank=True)
    start_year = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1960), MaxValueValidator(2100)],
    )
    end_year = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1960), MaxValueValidator(2100)],
    )
    is_current = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.get_level_display() or "Education"
