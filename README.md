# Mboko Recruit Django MVP

This repository now includes a Django implementation of the Mboko Recruit MVP CV flow, based on:
- `cv-form-schema-v1.md`
- `mboko-recruit-mvp-architecture.md`
- `mboko-recruit-components.html`

## What is implemented

- Django project config (`config/`, `manage.py`)
- `recruit` app with normalized models:
  - `CV`, `CVTranslation`
  - `WorkExperience`, `WorkExperienceTranslation`
  - `Education`, `EducationTranslation`
  - `Skill`
- Initial migration (`apps/recruit/migrations/0001_initial.py`)
- MVP CV form page (identity + profile + skills)
- CV detail/review page
- Placeholder PDF service (`PDFGeneratorService`) for future wiring

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Notes

- The app is mobile-first and follows the documented grayscale design tokens.
- The CV form currently covers the core MVP fields and persists French translation + skills.
- PDF generation is a placeholder and should be replaced with a real generator in the next iteration.
