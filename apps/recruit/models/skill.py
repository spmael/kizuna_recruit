from django.db import models


class Skill(models.Model):
    cv = models.ForeignKey("recruit.CV", on_delete=models.CASCADE, related_name="skills")
    name = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.name
