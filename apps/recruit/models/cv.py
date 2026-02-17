from django.db import models


class CV(models.Model):
    class Availability(models.TextChoices):
        IMMEDIATE = "immediate", "Immédiate"
        TWO_WEEKS = "2_weeks", "Dans 2 semaines"
        ONE_MONTH = "1_month", "Dans 1 mois"
        DISCUSS = "discuss", "À discuter"

    full_name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=24)
    email = models.EmailField(blank=True)
    city = models.CharField(max_length=60)
    address_line = models.CharField(max_length=120, blank=True)
    photo = models.ImageField(upload_to="cv_photos/")
    availability = models.CharField(
        max_length=20,
        choices=Availability.choices,
        blank=True,
    )
    target_job_title = models.CharField(max_length=60, blank=True)
    target_sector = models.CharField(max_length=40, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.full_name
