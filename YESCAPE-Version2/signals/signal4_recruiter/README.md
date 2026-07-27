# Signal 4 — Recruiter Trust

## Phase

Phase 3.4

---

# Objective

The Recruiter Trust Signal evaluates whether the recruiter contacting the student is legitimate.

Many internship scams impersonate Human Resources personnel using fake names, free email providers, disposable email services, or domains that do not belong to the claimed company.

This signal verifies the recruiter's identity by analyzing the email address, domain ownership, company association, and email provider before generating a Recruiter Trust Score.

---

# Signal Architecture

Internship Offer

↓

Recruiter Information Extraction

↓

Email Parsing

↓

Email Domain Verification

↓

Company Email Matching

↓

Free Email Detection

↓

Recruiter Trust Score

---

# Modules

## 3.4.1 Recruiter Information Extraction

### Objective

Extract recruiter email addresses from internship offers.

The extracted email serves as the starting point for all recruiter verification modules.

Example

Input

Contact our HR Team

John Smith

johnsmith@google.com

Output

johnsmith@google.com

Status

Completed

---

## Upcoming Modules

### 3.4.2

Email Parser

Extract

- Username
- Email Domain

Example

johnsmith@google.com

↓

Username

johnsmith

↓

Domain

google.com

---

### 3.4.3

Email Domain Verification

Reuse Domain Trust Signal to verify

- WHOIS
- DNS
- HTTPS
- Google Safe Browsing

---

### 3.4.4

Company Email Matching

Verify whether the email domain belongs to the claimed company.

Example

Google

↓

john@google.com

↓

Match

Example

Google

↓

john@gmail.com

↓

Mismatch

---

### 3.4.5

Free Email Detection

Detect public email providers such as

- gmail.com
- yahoo.com
- outlook.com
- hotmail.com
- proton.me

These are not automatically malicious but reduce recruiter trust for official internship recruitment.

---

### 3.4.6

Recruiter Trust Score

Combine

- Domain Verification
- Company Match
- Email Provider
- Domain Trust

into a single Recruiter Trust Score.

---

# Current Status

Completed

Modules Implemented

- Recruiter Information Extraction

Version

YEScape 2.0

### 3.4.2 Email Parser

#### Objective

Split the extracted recruiter email into its username and domain.

Example

johnsmith@google.com

↓

Username

johnsmith

↓

Domain

google.com

Output

```json
{
  "email": "johnsmith@google.com",
  "username": "johnsmith",
  "domain": "google.com"
}
```


## 3.4.3 Email Domain Verification

### Objective

Verify the recruiter's email domain using the existing Domain Trust Signal developed in Signal 2.

This module reuses the complete Domain Trust pipeline instead of implementing a separate verification system.

### Reused Components

- WHOIS Verification
- DNS Verification
- HTTPS Verification
- Google Safe Browsing

### Input

Recruiter Email Domain

Example

google.com

### Output

- WHOIS Score
- DNS Score
- HTTPS Score
- Safe Browsing Score
- Domain Trust Score

Example

Domain

google.com

↓

Domain Trust Score

100

### Status

Completed

---

## 3.4.4 Company Email Matching

### Objective

Verify whether the recruiter's email domain belongs to the official company.

This module compares the parsed email domain against the Company Registry created in Signal 3.

### Verification Logic

Company

↓

Official Domain

↓

Career Portal Domain

↓

Recruiter Email Domain

↓

Match / Mismatch

### Examples

Google

Recruiter Email

john@google.com

↓

Match

Recruiter Email

john@gmail.com

↓

Mismatch

Recruiter Email

john@google-careers-job.com

↓

Mismatch

### Output

- Match Status
- Matching Reason
- Company Email Score

### Status

Completed

---

## 3.4.5 Free Email Detection

### Objective

Determine whether the recruiter is using a public email provider instead of an official corporate email.

Although public email providers are legitimate services, they reduce recruiter trust because established organizations generally recruit using official company domains.

### Supported Providers

- Gmail
- Yahoo
- Outlook
- Hotmail
- Live
- Proton Mail
- iCloud
- AOL
- Mail.com
- GMX
- Yandex
- Rediffmail
- Zoho Mail

### Examples

hr@google.com

↓

Corporate Email

↓

Score 100

jobs@gmail.com

↓

Free Email

↓

Score 20

recruitment@yahoo.com

↓

Free Email

↓

Score 20

### Output

- Free Email Detection
- Provider Name
- Free Email Score

### Status

Completed

---

# Current Progress

Completed Modules

- 3.4.1 Recruiter Information Extraction
- 3.4.2 Email Parser
- 3.4.3 Email Domain Verification
- 3.4.4 Company Email Matching
- 3.4.5 Free Email Detection

Remaining

- 3.4.6 Recruiter Trust Score

Version

YEScape 2.0

## 3.4.6 Recruiter Trust Score

### Objective

Combine all recruiter verification modules into a single Recruiter Trust Score.

### Components

- Email Domain Trust (35%)
- Company Email Matching (35%)
- Free Email Detection (20%)
- Email Format Validation (10%)

### Output

- Recruiter Trust Score (0–100)

### Interpretation

| Score | Meaning |
|------:|---------|
| 90–100 | Highly Trusted Recruiter |
| 70–89 | Trusted Recruiter |
| 50–69 | Needs Manual Verification |
| Below 50 | Suspicious Recruiter |

### Status

Completed