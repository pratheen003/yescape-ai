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

---

# Phase 4.2.4 – Offer Analysis Engine

## Objective

The Offer Analysis Engine transforms raw extracted OfferData into a validated and normalized structure.

Unlike the Offer Parser, which only extracts fields, the engine evaluates extraction completeness and generates an extraction confidence score.

## Processing Pipeline

Offer Text

↓

Offer Parser

↓

OfferData

↓

Offer Analysis Engine

↓

Validated OfferData

## Confidence Calculation

The first version calculates confidence using four essential fields:

- Company
- Website
- Recruiter Email
- Salary

Each detected field contributes equally to the confidence score.

## Benefits

- Detects incomplete OCR results.
- Supports future PDF and image processing.
- Standardizes extracted offer information.
- Provides confidence values for AI explanations.

---

# Phase 4.2.6 – Website Selection Improvement

## Objective

The Offer Parser now selects the most specific website when multiple domains are present.

## Previous Behavior

The parser selected the first detected domain.

Example:

- google.com
- careers.google.com

Result:

google.com

## New Behavior

The parser detects all website candidates and prefers the longest match, which usually corresponds to the most specific subdomain.

Result:

careers.google.com

## Benefits

- Better company verification accuracy.
- Higher confidence in official career portal detection.
- Reduced false score reduction.