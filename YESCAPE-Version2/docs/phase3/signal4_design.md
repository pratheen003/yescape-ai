# Signal 4 – Recruiter Identity Verification

## Overview

Signal 4 verifies whether the recruiter contacting the candidate is genuine.

Many internship scams use fake recruiter email addresses such as:

- hr.google@gmail.com
- googlejobs@yahoo.com
- microsoft.hr@outlook.com

instead of official corporate email addresses.

Signal 4 evaluates recruiter authenticity using multiple verification layers.

---

# Objectives

- Extract recruiter email from offer text.
- Validate email domain.
- Compare recruiter email domain with official company domains.
- Detect free/public email providers.
- Produce a Recruiter Trust Score.

---

# Architecture

Offer Letter
      │
      ▼
Email Extraction
      │
      ▼
Email Domain Extraction
      │
      ▼
Domain Trust Verification
      │
      ▼
Company Domain Matching
      │
      ▼
Free Email Detection
      │
      ▼
Recruiter Trust Score

---

# Phase Breakdown

## Phase 3.4.1

### Recruiter Email Extraction

Purpose

Extract recruiter email address using Regular Expressions.

Input

Offer letter text

Output

- recruiter email
- username
- domain

Technology

- Python re

---

## Phase 3.4.2

### Email Domain Verification

Purpose

Verify whether the email domain itself is trustworthy.

Example

hr@google.com

↓

google.com

↓

Signal 2 Domain Trust Score

Output

Domain Trust Score

---

## Phase 3.4.3

### Company Domain Matching

Purpose

Compare recruiter email domain with the official company registry.

Official domains

- google.com
- careers.google.com

Scam domains

- google-careers-job.com
- googlejobs.org

Output

Company Match Score

---

## Phase 3.4.4

### Free Email Detection

Purpose

Detect public email providers.

Examples

- gmail.com
- yahoo.com
- outlook.com

Corporate domains receive maximum score.

Public providers receive low score.

---

## Phase 3.4.5

### Recruiter Trust Score Fusion

Combine

- Domain Trust
- Company Match
- Free Email Detection

Weights

| Module | Weight |
|---------|--------|
| Domain Trust | 35% |
| Company Match | 40% |
| Free Email | 25% |

Output

Recruiter Trust Score (0–100)

---

# Folder Structure

signals/

signal4_recruiter/

    email_extractor.py

    email_domain.py

    company_domain_match.py

    free_email_detector.py

    recruiter_score.py

---

# Example

Input

Recruiter Email

hr@google.com

Output

Recruiter Trust Score

100

---

Input

jobs@gmail.com

Output

Recruiter Trust Score

49

---

# Advantages

- Detects fake recruiter emails.
- Uses company registry instead of web search.
- Reuses Signal 2 domain verification.
- Lightweight and offline.

---

# Limitations

- Cannot verify employee identity.
- Relies on known company domains.
- Does not validate mailbox existence.

---

# Future Improvements

- SPF Verification
- DKIM Verification
- DMARC Validation
- Employee Directory Verification
- Corporate LDAP Integration