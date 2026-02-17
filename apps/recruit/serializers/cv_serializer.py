from dataclasses import dataclass

from apps.recruit.models import CV


@dataclass
class CVSerializer:
    cv: CV

    def data(self) -> dict:
        translation = self.cv.translations.filter(language="fr").first()
        return {
            "id": self.cv.id,
            "full_name": self.cv.full_name,
            "phone_number": self.cv.phone_number,
            "city": self.cv.city,
            "email": self.cv.email,
            "availability": self.cv.availability,
            "headline": translation.headline if translation else "",
            "summary": translation.summary if translation else "",
            "skills": [skill.name for skill in self.cv.skills.all()],
        }
