# Mboko Recruit — UX Documentation

**Version:** 1.0  
**Status:** Design System Complete  
**Purpose:** Complete UX reference for CV creation workflow

---

## Overview

This folder contains three HTML files that document the complete user experience design for Mboko Recruit MVP:

1. **`mboko-recruit.html`** — Interactive prototype with all 7 screens
2. **`mboko-workflow-overview.html`** — Visual workflow map showing screen transitions
3. **`mboko-recruit-components.html`** — Component inventory with all UI states

---

## Files

### 1. `mboko-recruit.html`

**Type:** Interactive Prototype  
**Purpose:** Full working prototype of the CV creation flow

**Contains:**
- All 7 screens (W1–W7) in a single-page application
- Complete JavaScript state management
- Form validation logic
- Screen navigation system
- Photo upload functionality
- Dynamic content management (experiences, education, skills)

**Screens:**
- **W1 — Landing:** Entry point with value propositions
- **W2 — Identité:** Required identity fields (name, phone, city, photo)
- **W3 — Profil:** Optional profile information (headline, summary)
- **W4 — Parcours:** Content sections (experiences, education, skills)
- **W5 — Vérification:** Review screen with edit links
- **W6 — Success:** CV generated successfully
- **W7 — Error:** Blocking error when minimum content rule not met

**Key Features:**
- Mobile-first design (375px frame)
- Brutalist-warm aesthetic
- No external dependencies (except HTMX for future use)
- Client-side state management
- Form validation with error states
- Photo preview functionality

---

### 2. `mboko-workflow-overview.html`

**Type:** Visual Documentation  
**Purpose:** Blueprint-style workflow map

**Contains:**
- Horizontal flow diagram showing all 7 screens
- Decision diamond for minimum content rule
- Screen cards with miniaturized UI previews
- Connector arrows showing navigation paths
- Color-coded tags (Required, Optional, Review, Success, Error)
- Legend explaining screen types

**Visual Style:**
- Dark canvas with grid background
- Engineering-drawing aesthetic
- Miniaturized phone cards showing actual UI
- Decision logic visualization
- Animation on load

**Use Cases:**
- Understanding the complete user journey
- Identifying decision points
- Planning implementation phases
- Stakeholder presentations

---

### 3. `mboko-recruit-components.html`

**Type:** Component Library  
**Purpose:** Complete component inventory with all states

**Contains:**
- **24 components** across 8 categories:
  - Design Tokens (CSS variables)
  - Navigation Components
  - Buttons (Primary, Secondary, Ghost)
  - Form Inputs (Text, Textarea, Photo Upload)
  - Content Sections (Accordions, Entry Cards)
  - Review Components (Cards, Feedback Widget)
  - System States (Success, Error, Action Cards)
  - Layout Components (Banners, Value Props)

**Each Component Includes:**
- Component ID and name
- Description
- All visual states (idle, hover, focus, error, disabled, etc.)
- Usage rules and constraints
- "Used in" tags showing which screens use it
- Validation logic tables
- Navigation map

**Key Sections:**
- Design tokens with color swatches
- Visual constraints (no web fonts, no gradients, no icons in MVP)
- Validation logic tables
- Screen navigation map
- Component completion checklist

---

## Design System

### Visual Principles

**From `mboko-recruit-components.html` (authoritative):**

1. **Greyscale + warm stone palette.** Black for emphasis.
2. **No gradients, no heavy shadows, no border-radius.**
3. **No web fonts in MVP. System font only.**
4. **No icons — use text symbols** (✓ ✎ ← × + ⚠ 📷 💡 💼 🎓).
5. **Errors never use color alone.** Always text + border change.
6. **Mobile-first.** Frame width: 375px.

### Color Palette

**From `mboko-recruit-components.html` (authoritative design system):**

```css
/* Neutrals */
--bg: #faf9f7           /* Background */
--surface: #ffffff      /* Surface/white */
--text: #0a0a0a         /* Primary text, borders, buttons */
--muted: #57534e        /* Secondary/muted text */
--border: #d6d3d1       /* Border color */
--subtle: #f0eeeb       /* Subtle backgrounds */

/* Semantic */
--accent: #0a0a0a       /* Accent (same as text) */
--error-bg: #fef2f2     /* Error background tint */
--success-bg: #f0fdf4   /* Success background tint */
--focus-ring: rgba(10,10,10,0.2)  /* Focus ring color */
```

**Note:** The interactive prototype (`mboko-recruit.html`) uses different variable names (`--ink`, `--paper`, `--warm-gray`, etc.) for compatibility, but the component library uses the above names as the canonical design system.

**Inline Colors (not variables):**
- Green `#16a34a` — Photo upload success border (ONLY color outside greyscale)
- Red `#dc2626` — Error icon border only (not used for text)

### Typography

- **Body:** DM Sans (prototype) / System font (MVP)
- **Monospace:** Space Mono (prototype) / System monospace (MVP)
- **Sizes:** 0.6875rem (11px) to 1.5rem (24px)
- **Weights:** 400 (regular), 700 (bold)

---

## User Flow

### Linear Forward, Flexible Backward

```
W1 (Landing)
  ↓ [CTA click]
W2 (Identité) ← Required fields
  ↓ [All valid]
W3 (Profil) ← Optional, can skip
  ↓ [Continue / Skip]
W4 (Parcours) ← Content (exp/edu/skills)
  ↓ [Continue]
W5 (Vérification) ← Review with edit links
  ↓ [Generate]
  ├─→ W6 (Success) ← If minimum rule met
  └─→ W7 (Error) ← If minimum rule NOT met
       ↓ [3 fix paths]
       └─→ W4 (to add content)
```

### Minimum Content Rule

CV can be generated if **at least one of:**
- ≥ 1 work experience, OR
- ≥ 1 education entry, OR
- ≥ 3 skills (non-empty)

If none met → W7 (Error screen) with 3 recovery paths

---

## Component Categories

### A) Navigation
- Screen Header (back link + title + step indicator)
- Progress Bar (3px, 25%/50%/75%/100%)

### B) Buttons
- Primary (black bg, white text, full width)
- Secondary (white bg, black border)
- Ghost (text link, underline on hover)

### C) Form Inputs
- Text Input (6 states: idle, filled, focus, error, disabled, optional)
- Textarea (multiline, min-height 96px)
- Photo Upload (3 states: empty, with photo, error)

### D) Content Sections
- Accordion (collapsed/expanded, emphasized variant)
- Entry Card (experience/education with remove button)
- Add Entry Button (dashed border)

### E) Review
- Review Card (identity/content summary with edit links)
- Feedback Widget (thumbs up/down, 3 states)

### F) System States
- Success Header (confirmation banner)
- Error Header (blocking error, empathetic copy)
- Rule Box + Status (minimum rule + current counts)
- Action Cards (3 recovery paths)
- Tip Box (helpful hints)
- Trust Footer (privacy messaging)

### G) Layout
- Info Banner (contextual messages)
- Value Proposition (landing page features)

---

## Validation Rules

### W2 Form Validation
- **Nom complet:** Required, min 2 words, 3-80 chars
- **Téléphone:** Required, accepts local/international format
- **Ville:** Required, 2-60 chars
- **Photo:** Required, accepts image/*, max 4MB

**Button:** Disabled until all required fields valid

### Minimum Content Rule (W5 → W6/W7)
Checked on "Générer mon CV" click:
- `experiences.length > 0` OR
- `education.length > 0` OR
- `skills.filter(s => s.trim()).length >= 3`

---

## Implementation Notes

### For Developers

1. **Copy CSS variables** from `mboko-recruit-components.html` section ★
2. **Use component HTML** as templates from component inventory
3. **Follow validation logic** from tables in section H
4. **Respect navigation map** from section H
5. **Mobile-first:** Start with 375px, scale up

### For Designers

1. **All states documented:** Every component shows all visual states
2. **Copy guidelines:** Empathetic, reassuring, no blame language
3. **Accessibility:** Focus states, error states, disabled states all defined
4. **Constraints:** MVP uses system fonts, no icons, no gradients

### For Product

1. **7 screens total:** Linear flow with error recovery
2. **No dead ends:** Every screen has escape path
3. **Minimum rule:** Flexible (1 exp OR 1 edu OR 3 skills)
4. **Optional sections:** W3 can be skipped entirely

---

## Screen Details

### W1 — Landing
- **Purpose:** Entry point, value propositions
- **CTA:** "Créer mon CV →"
- **No header** (entry point)
- **Trust footer:** Privacy messaging

### W2 — Identité
- **Purpose:** Required identity information
- **Fields:** Name, phone, city, photo
- **Validation:** All required, button disabled until valid
- **Progress:** 25%

### W3 — Profil
- **Purpose:** Optional profile information
- **Fields:** Professional title, summary
- **Can skip:** Ghost button "Passer cette étape"
- **Progress:** 50%

### W4 — Parcours
- **Purpose:** Content collection (experiences, education, skills)
- **Sections:** 3 accordions (exp, edu, skills)
- **Skills emphasized:** Open by default, thicker border
- **Minimum rule info:** Banner explains requirement
- **Progress:** 75%

### W5 — Vérification
- **Purpose:** Review before generation
- **Edit links:** ✎ Modifier → W2, W3, or W4
- **Feedback widget:** Optional thumbs up/down
- **Progress:** 100%

### W6 — Success
- **Purpose:** CV generated successfully
- **Actions:** Download PDF, Share WhatsApp
- **Tip box:** Save link for later
- **Restart:** "Créer un autre CV" → W1

### W7 — Error
- **Purpose:** Blocking error when minimum rule not met
- **Tone:** Empathetic, no blame
- **Recovery:** 3 action cards → W4
- **Status:** Shows current counts (exp/edu/skills)

---

## File Structure

```
docs/ux/
├── mboko-recruit.html              # Interactive prototype (1291 lines)
├── mboko-workflow-overview.html    # Workflow map (962 lines)
├── mboko-recruit-components.html   # Component library (565 lines)
└── README.md                       # This file
```

---

## Usage

### Viewing the Prototypes

1. **Interactive Prototype:** Open `mboko-recruit.html` in browser
   - Click through all screens
   - Test form validation
   - Try photo upload
   - Navigate forward/backward

2. **Workflow Map:** Open `mboko-workflow-overview.html` in browser
   - See complete flow at a glance
   - Understand decision points
   - Review screen relationships

3. **Component Library:** Open `mboko-recruit-components.html` in browser
   - Browse all 24 components
   - See all visual states
   - Copy CSS and HTML
   - Reference validation rules

### Implementation

1. Start with design tokens (CSS variables)
2. Implement navigation components (header, progress)
3. Build form inputs with all states
4. Add content sections (accordions, entries)
5. Create review screen
6. Implement success/error states
7. Add validation logic
8. Test navigation flow

---

## Design Constraints (MVP)

✅ **Allowed:**
- System fonts
- Text symbols (✓ ✎ ← × + ⚠ 📷 💡 💼 🎓)
- Greyscale + warm stone palette
- Black for emphasis
- Sharp borders (no radius)
- Subtle shadows

❌ **Not Allowed:**
- Web fonts (use system fonts)
- Icon libraries (use text symbols)
- Gradients
- Heavy shadows
- Border radius
- Color-only error states

---

## Related Documents

- **PRD:** `docs/prd/mboko-recruit-prd-v1.md`
- **Form Schema:** `docs/forms/cv-form-schema-v1.md`
- **Architecture:** `docs/architecture/mboko-recruit-mvp-architecture.md`

---

## Version History

- **v1.0** — Initial design system complete
  - All 7 screens designed
  - 24 components documented
  - Complete workflow mapped
  - Validation rules defined

---

## Notes

- **Green is the ONLY color** outside greyscale (photo upload success border)
- **No red text anywhere** — errors use ⚠ prefix + bold border
- **Copy is empathetic** — "Pas de panique !", "Même une petite expérience compte"
- **Mobile-first** — Designed for 375px, scales up
- **No dead ends** — Every screen has at least one escape path

---

**Status:** ✅ Ready for implementation  
**Last Updated:** 2024  
**Maintained By:** Product & Design Team
