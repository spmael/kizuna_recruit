from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class WorkExperience(models.Model):
    cv = models.ForeignKey("recruit.CV", on_delete=models.CASCADE, related_name="work_experiences")
    employer_name = models.CharField(max_length=80, blank=True)
    city = models.CharField(max_length=60, blank=True)
    start_month = models.PositiveSmallIntegerField(blank=True, null=True)
    start_year = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1960), MaxValueValidator(2100)],
    )
    end_month = models.PositiveSmallIntegerField(blank=True, null=True)
    end_year = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1960), MaxValueValidator(2100)],
    )
    is_current = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.employer_name or "Experience"
