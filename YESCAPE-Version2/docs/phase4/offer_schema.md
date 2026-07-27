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