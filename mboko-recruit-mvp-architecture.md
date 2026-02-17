# Mboko Recruit – MVP Architecture & Models

**Version:** 1.0  
**Status:** Decision-locked  
**Scope:** Mboko Recruit – MVP 0.1 (CV Generator)  
**Supported Languages:** French (FR), English (EN)

**Related documents:**
- PRD: `docs/prd/mboko-recruit-prd-v1.md`
- Form Schema: `docs/forms/cv-form-schema-v1.md`

---

## 1. Architecture Principles

- Structure before intelligence
- Documentation before implementation
- Bilingual content, not bilingual structure
- MVP simplicity with future-proof design
- No magic libraries (no auto-translation, no OCR-first)
- Low-literacy and mobile-first constraints

---

## 2. High-Level Architecture Overview

```
User (Mobile / Web)
        ↓
Structured CV Form (FR default)
        ↓
Backend Validation Layer
        ↓
CV Data Models (Normalized)
        ↓
PDF Generation Service (FR / EN)
        ↓
Downloadable CV (1 page)
```

MVP constraints:
- No authentication required
- No employer dashboard
- No job matching
- SME hiring is the pilot context (restaurant as first deployment)

---

## 3. Backend Project Structure (Django)

```
mboko-recruit/
├── apps/
│   └── recruit/
│       ├── models/
│       │   ├── __init__.py
│       │   ├── cv.py
│       │   ├── cv_translation.py
│       │   ├── work_experience.py
│       │   ├── work_experience_translation.py
│       │   ├── education.py
│       │   ├── education_translation.py
│       │   └── skill.py
│       ├── services/
│       │   └── pdf_generator.py
│       ├── serializers/
│       │   └── cv_serializer.py
│       ├── views/
│       │   └── cv_generate.py
│       └── urls.py
├── config/
│   ├── __init__.py
│   ├── base.py
│   ├── local.py
│   └── prod.py
├── docs/
│   ├── prd/
│   ├── forms/
│   ├── ux/
│   └── architecture/
│       └── mboko-recruit-mvp-architecture.md
└── README.md
```

---

## 4. Data Model Design Rules

### Core Rule

The **CV** is the root entity.

- Structural data is stored in base tables
- Language-specific content is stored in translation tables
- No duplicated language fields in base models

---

## 5. Models Overview

### 5.1 CV (Root Model)

**File:** `apps/recruit/models/cv.py`

Purpose:
- Store identity and non-translatable information
- Act as the parent entity for all CV-related data

Fields:
- full_name
- phone_number
- email (optional)
- city
- address_line (optional)
- photo
- availability
- target_job_title (optional)
- target_sector (optional)
- created_at

Relationships:
- One CV → many CVTranslation
- One CV → many WorkExperience
- One CV → many Education
- One CV → many Skill

---

### 5.2 CVTranslation

**File:** `apps/recruit/models/cv_translation.py`

Purpose:
- Store language-specific profile information

Languages:
- fr (default)
- en (optional)

Fields:
- language
- headline
- summary

Constraints:
- Unique (cv, language)

---

### 5.3 WorkExperience

**File:** `apps/recruit/models/work_experience.py`

Purpose:
- Store job timeline and non-textual data

Fields:
- employer_name
- city
- start_month
- start_year
- end_month
- end_year
- is_current

Relationships:
- Many WorkExperience → one CV
- One WorkExperience → many WorkExperienceTranslation

---

### 5.4 WorkExperienceTranslation

**File:** `apps/recruit/models/work_experience_translation.py`

Purpose:
- Store language-specific job content

Fields:
- language
- job_title
- description

Constraints:
- Unique (work_experience, language)

---

### 5.5 Education

**File:** `apps/recruit/models/education.py`

Purpose:
- Store education timeline and level

Fields:
- level
- start_year
- end_year
- is_current

Relationships:
- Many Education → one CV
- One Education → many EducationTranslation

---

### 5.6 EducationTranslation

**File:** `apps/recruit/models/education_translation.py`

Purpose:
- Store language-specific education content

Fields:
- language
- school_name
- field_of_study

Constraints:
- Unique (education, language)

---

### 5.7 Skill (MVP Simplified)

**File:** `apps/recruit/models/skill.py`

Purpose:
- Store skills as simple keywords

Fields:
- name

Notes:
- Skills are not translated in MVP
- Normalisation or translation may be added later

---

## 6. Language Strategy (FR / EN)

- French is the default language
- English is optional
- CV output language is user-selected
- Fallback rule:
  - If English translation is missing, French content is used
- No automatic translation is performed in MVP

---

## 7. PDF Generation Strategy

**File:** `apps/recruit/services/pdf_generator.py`

Responsibilities:
- Receive CV ID and target language
- Fetch correct translation set
- Apply fixed one-page CV layout
- Generate PDF output

Rules:
- Identical layout across languages
- Only text content changes
- No template or styling selection

---

## 8. Explicitly Excluded from MVP

- Handwritten or printed OCR
- AI rewriting or content enhancement
- Multiple CV templates
- User authentication
- Employer dashboards
- Candidate scoring or ranking
- Job matching or search

---

## 9. Versioning & Change Policy

Any change to:
- Form fields
- Models
- Language handling
- PDF structure

Requires:
- Update to this document
- Version bump (v1.1, v2.0, etc.)

This document overrides ad-hoc implementation decisions.

---

## 10. Final Architecture Approval

- Architecture is minimal, clear, and scalable
- Translation pattern is explicit and robust
- Suitable for bilingual Cameroon context
- Approved for MVP implementation
