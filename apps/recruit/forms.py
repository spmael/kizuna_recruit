from django import forms

from apps.recruit.models import CV, CVTranslation, Skill


class CVForm(forms.ModelForm):
    headline = forms.CharField(max_length=80, required=False)
    summary = forms.CharField(widget=forms.Textarea, max_length=400, required=False)
    skills = forms.CharField(
        max_length=300,
        required=False,
        help_text="Sépare les compétences avec des virgules",
    )

    class Meta:
        model = CV
        fields = [
            "full_name",
            "phone_number",
            "city",
            "photo",
            "email",
            "address_line",
            "availability",
            "target_job_title",
            "target_sector",
        ]

    def clean_full_name(self):
        full_name = self.cleaned_data["full_name"].strip()
        if len(full_name.split()) < 2:
            raise forms.ValidationError("Le nom complet doit contenir au moins 2 mots.")
        return full_name

    def save(self, commit=True):
        cv = super().save(commit=commit)

        if commit:
            CVTranslation.objects.update_or_create(
                cv=cv,
                language=CVTranslation.Language.FRENCH,
                defaults={
                    "headline": self.cleaned_data.get("headline", ""),
                    "summary": self.cleaned_data.get("summary", ""),
                },
            )
            Skill.objects.filter(cv=cv).delete()
            skills_text = self.cleaned_data.get("skills", "")
            for skill in [s.strip() for s in skills_text.split(",") if s.strip()]:
                Skill.objects.create(cv=cv, name=skill)

        return cv
