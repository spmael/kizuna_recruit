# CV Form Schema – Mboko Recruit (MVP 0.1)

**Version:** 1.0  
**Status:** Decision-locked  
**Related PRD:** docs/prd/mboko-recruit-prd-v1.md  
**Purpose:** Define the exact fields, validations, and UX rules for the CV generation form.

This document is the single source of truth for:
- Frontend form implementation
- Backend data models
- Validation rules
- PDF CV generation

---

## Design Principles

- Structure over creativity
- Simplicity over exhaustiveness
- The form compensates for user limitations
- The user is never blamed for poor structure
- Mobile-first, low-literacy friendly

---

## Section A — Identity

### 1. full_name (required)
- Type: text
- Validation:
  - Minimum 2 words
  - 3–80 characters
- Placeholder: `Ex: Jean Dupont`

---

### 2. phone_number (required)
- Type: text
- Validation:
  - Accept local or international format
  - Digits, spaces, `+` allowed
- Placeholder: `Ex: +237 6XX XXX XXX`

---

### 3. city (required)
- Type: text
- Validation:
  - 2–60 characters
- Placeholder: `Ex: Douala`

---

### 4. photo (required)
- Type: image upload
- Accepted formats: JPG, PNG, WebP
- Max size: 4 MB
- UX helper text:
  - `Photo claire, visage centré, fond neutre si possible`

---

### 5. email (optional)
- Type: email
- Validation: standard email format
- Placeholder: `Ex: nom@gmail.com`

---

### 6. address_line (optional)
- Type: text
- Max length: 120
- Placeholder: `Quartier, rue (facultatif)`

---

## Section B — Profile

### 7. headline (optional, recommended)
- Type: text
- Max length: 80
- Quick-select suggestions (dynamic based on target_sector):
  - If sector = Hospitality: `Serveur / Serveuse`, `Cuisinier / Aide-cuisinier`, `Caissier / Caissière`, `Agent polyvalent`
  - If sector = Construction: `Ouvrier / Ouvrière`, `Maçon`, `Plombier`, `Électricien`
  - If sector = Retail: `Vendeur / Vendeuse`, `Caissier / Caissière`, `Gestionnaire de stock`
  - If sector = Transport: `Chauffeur / Chauffeuse`, `Livreur / Livreuse`, `Agent logistique`
  - Generic: `Agent polyvalent`, `Employé / Employée`, `Ouvrier / Ouvrière`

---

### 8. summary (optional)
- Type: textarea
- Max length: 400
- UX guidance:
  - `1 à 2 phrases sur ton expérience et ce que tu cherches`
- Examples (sector-agnostic):
  - `Expérience de 2 ans dans le service client, ponctuel, disponible immédiatement.`
  - `Travailleur expérimenté, sérieux et motivé, recherche un poste stable.`

---

## Section C — Work Experience (repeatable)

**Field group:** `work_experiences[]`  
Zero or more entries allowed.

### Per entry:

#### 9. job_title (required if entry exists)
- Type: text
- Max length: 60
- Example: `Serveur`, `Cuisinier`

---

#### 10. employer_name (optional)
- Type: text
- Max length: 80

---

#### 11. city (optional)
- Type: text
- Max length: 60

---

#### 12. start_month (optional)
- Type: select (Jan–Dec)

#### 13. start_year (optional)
- Type: number
- Range: current year - 60 → current year

---

#### 14. end_month (optional)
- Type: select (Jan–Dec)

#### 15. end_year (optional)
- Type: number
- Same range as start_year

---

#### 16. is_current (optional)
- Type: boolean
- Rule:
  - If `true`, end_month and end_year must be empty

---

#### 17. description (optional)
- Type: textarea
- Max length: 300
- UX hint:
  - `Décris ce que tu faisais (même en phrases simples)`
- Example bullets (displayed as help text):
  - `Accueil des clients`
  - `Prise de commandes`
  - `Encaissement / caisse`

---

## Section D — Education (repeatable)

**Field group:** `educations[]`  
Zero or more entries allowed.

### Per entry:

#### 18. school_name (required if entry exists)
- Type: text
- Max length: 100

---

#### 19. level (optional, recommended)
- Type: select
- Values:
  - `Primaire`
  - `Collège (BEPC)`
  - `Lycée (Probatoire / BAC)`
  - `Université`
  - `Formation professionnelle`
  - `Autre`

---

#### 20. field_of_study (optional)
- Type: text
- Max length: 80

---

#### 21. start_year (optional)
- Type: number

#### 22. end_year (optional)
- Type: number

---

#### 23. is_current (optional)
- Type: boolean

---

## Section E — Skills

### 24. skills (optional, strongly recommended)
- Type: text
- Format: comma-separated values
- Max length: 300
- Placeholder:
  - `Ex: service client, cuisine, hygiène, caisse, ponctualité`

---

## Section F — Languages (optional)

**Field group:** `languages[]`

### Per entry:
- language_name (text)
- level (select):
  - `Débutant`
  - `Intermédiaire`
  - `Avancé`

---

## Section G — Availability (optional)

### 25. availability
- Type: select
- Values:
  - `Immédiate`
  - `Dans 2 semaines`
  - `Dans 1 mois`
  - `À discuter`

---

### 26. target_job_title (optional)
- Type: text (free text)
- Max length: 60
- Placeholder: `Ex: Serveur, Vendeur, Ouvrier, Chauffeur`
- UX note: Dynamic suggestions based on target_sector (UI hints only, not DB constraints)

---

### 27. target_sector (optional)
- Type: select
- Values:
  - `Retail / Shop` (Commerce / Magasin)
  - `Hospitality` (Restauration / Hôtellerie)
  - `Transport / Logistics` (Transport / Logistique)
  - `Construction` (Bâtiment / Construction)
  - `Admin / Office` (Administration / Bureau)
  - `Health / Care` (Santé / Soins)
  - `Education` (Éducation)
  - `Security` (Sécurité)
  - `IT / Digital` (Informatique / Numérique)
  - `Other` (Autre)

---

## Global Validation Rules

The CV can be generated if:
- Identity section is valid (name, phone, city, photo)
- AND at least one of the following:
  - At least one work experience entry
  - OR at least one education entry
  - OR at least 3 skills provided

If not satisfied:
- Show message:
  - `Ajoute au moins une expérience, une école ou trois compétences pour générer ton CV.`

---

## Explicit Exclusions (MVP 0.1)

- Date of birth
- National ID numbers
- Marital status
- Automatic handwriting OCR
- AI rewriting of handwritten content

---

## Change Policy

- Any modification to this schema requires:
  - Version bump (v1.1, v2.0, etc.)
  - Update to related backend models if applicable
- This document overrides any conflicting implementation detail.

---
