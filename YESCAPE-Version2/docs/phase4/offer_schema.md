# Offer Data Schema

## Phase

4.2.1

---

## Purpose

The OfferData schema represents the normalized internship offer extracted from PDFs, images, OCR, or plain text.

Instead of every verification signal performing its own extraction, Signal 1 converts all input into one structured object.

---

## Stored Fields

- Company
- Recruiter Email
- Website
- Salary
- Offer Text
- Contact Email
- Phone Number
- Job Role
- Internship Duration
- Location
- PDF Metadata

---

## Benefits

- Single source of truth
- Cleaner verification engine
- Easier testing
- Easier AI explanation generation
- Future-proof for OCR and document uploads

# Offer Parser

## Phase

4.2.2

---

## Purpose

The Offer Parser converts raw internship offer text into a structured OfferData object.

Instead of requiring every verification signal to perform its own extraction, Signal 1 performs extraction once and stores the results inside OfferData.

---

## Current Extraction

- Company
- Recruiter Email
- Website
- Salary

---

## Future Expansion

- Candidate Name
- Job Role
- Internship Duration
- Location
- Joining Date
- Offer ID
- PDF Metadata

---

## Benefits

- Single extraction pipeline
- Cleaner verification engine
- Easier OCR integration
- Easier AI explanation generation

### Phase 4.2.3

The Offer Parser no longer maintains a hardcoded company list.

Instead, it dynamically reads company names from the centralized Company Registry (`company_registry.csv`) through the Registry Loader.

Benefits:

- Single source of truth
- Automatic support for newly added companies
- No duplicated company definitions
- Easier maintenance