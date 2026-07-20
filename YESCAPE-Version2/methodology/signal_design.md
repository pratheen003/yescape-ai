# YEScape 2.0 Signal Design

## Version

Version: 1.0

## Last Updated

20 July 2026

## Status

Draft

---

# Purpose

YEScape 2.0 is designed around the principle that internship legitimacy cannot be determined from text alone.

Instead of relying on a single machine learning prediction, the framework independently evaluates multiple trust signals that represent different aspects of an internship opportunity.

Each signal operates independently and produces its own trust score.

These scores are later fused into a single overall YESScore using a trained Fusion Model.

---

# Multi-Signal Trust Architecture

```text
                   Internship Opportunity
                            │
                            ▼
          ┌────────────────────────────────────┐
          │    Independent Trust Signals       │
          └────────────────────────────────────┘
                            │
        ┌──────────┬──────────┬──────────┬──────────┬──────────┐
        ▼          ▼          ▼          ▼          ▼
   Signal 1   Signal 2   Signal 3   Signal 4   Signal 5
      ML       Domain    Recruiter   Company    Context
 Probability Intelligence Identity Verification Intelligence
        │          │          │          │          │
        └──────────┴──────────┴──────────┴──────────┘
                            │
                            ▼
              Logistic Regression Fusion Engine
                            │
                            ▼
                       Final YESScore
                            │
                            ▼
               Explainable AI (SHAP Analysis)
                            │
                            ▼
              Interactive AI Verification Report
```

---

# Signal Overview

YEScape 2.0 evaluates five independent trust signals.

| Signal | Purpose |
|----------|---------|
| Signal 1 | Predict scam probability using machine learning |
| Signal 2 | Evaluate website and domain trust |
| Signal 3 | Verify recruiter identity |
| Signal 4 | Verify company legitimacy |
| Signal 5 | Analyze contextual scam indicators |

Each signal contributes unique evidence.

No signal alone determines the final verdict.

---

# Signal 1 — Machine Learning Scam Probability

## Objective

Predict whether the internship description resembles known scam postings.

---

## Input

- Internship description
- Offer letter text
- Email content

---

## Model

Primary Model

TF-IDF + XGBoost

(Optional Future)

DistilBERT

---

## Output

Scam Probability

Range

0–100

Example

87 → Highly suspicious

18 → Likely legitimate

---

## Why This Signal Exists

Text often contains hidden fraud patterns.

Examples

- Unrealistic salary
- Work-from-home promises
- Guaranteed placement
- Fee requests
- Generic company descriptions

Machine Learning captures these linguistic patterns.

---

# Signal 2 — Domain Intelligence

## Objective

Determine whether the internship website appears trustworthy.

---

## Input

Website URL

---

## Features

- Domain Age
- Registrar Information
- HTTPS Availability
- Google Safe Browsing Status
- Domain Consistency

---

## APIs

- WHOIS Lookup
- Google Safe Browsing API

---

## Output

Domain Trust Score

Range

0–100

Higher score indicates greater trust.

---

## Why This Signal Exists

Scam websites often

- use newly registered domains
- imitate legitimate companies
- lack HTTPS
- appear in Safe Browsing warnings

Text models cannot detect these risks.

---

# Signal 3 — Recruiter Identity Verification

## Objective

Evaluate whether the recruiter appears legitimate.

---

## Input

Recruiter Email

Company Name

---

## Verification Rules

- Email domain matches company domain
- Official recruiter contact available
- Manual LinkedIn verification (optional)
- Public recruiter information

---

## Output

Recruiter Trust Score

Range

0–100

---

## Why This Signal Exists

Many internship scams impersonate HR personnel.

Identity verification provides evidence unavailable in text alone.

---

# Signal 4 — Company Verification

## Objective

Verify that the claimed organization actually exists.

---

## Input

Company Name

Website

---

## Verification Sources

- MCA Public Registry
- GST Registration
- Official Company Website

---

## Output

Company Trust Score

Range

0–100

---

## Why This Signal Exists

Scammers frequently invent companies or imitate existing organizations.

Company verification reduces identity fraud.

---

# Signal 5 — Context Intelligence

## Objective

Analyze behavioral characteristics commonly found in internship scams.

---

## Input

Internship Description

Offer Letter

Email

---

## Indicators

- Registration fee
- Training fee
- Urgent response requests
- Guaranteed placement
- Grammar quality
- Excessive promises
- Emotional pressure
- Contact inconsistencies

---

## Method

Rule-based Context Analyzer

---

## Output

Context Trust Score

Range

0–100

---

## Why This Signal Exists

Certain scam behaviors are difficult to learn from datasets alone.

Explicit contextual rules improve robustness.

---

# Signal Independence

Each signal operates independently.

Failure of one signal does not affect the execution of the others.

Example

A legitimate company may still have

- suspicious language

or

A scam posting may use

- professional language
- fake recruiter
- newly created website

Each signal contributes different evidence.

---

# Signal Output

Every signal produces

| Output |
|----------|
| Trust Score (0–100) |
| Evidence |
| Confidence |
| Metadata |

These outputs become inputs to the Fusion Engine.

---

# Why Multiple Signals?

Traditional internship verification systems rely primarily on textual analysis.

YEScape 2.0 combines independent evidence from multiple perspectives.

Benefits include

- Better robustness
- Reduced false positives
- Reduced false negatives
- Transparent reasoning
- Improved real-world reliability

---

# Research Contribution

The novelty of YEScape 2.0 is not any individual signal.

The contribution lies in the combination of independently verifiable trust signals into a unified trust intelligence framework for internship verification.

This methodology enables the system to detect scams that text-only machine learning models may fail to identify.

---

# Next Stage

The outputs of all five signals are provided to the Fusion Engine.

The Fusion Engine learns how much importance should be assigned to each signal and produces the final YESScore.

This replaces manual weighted scoring with a trained meta-model capable of learning optimal trust fusion.