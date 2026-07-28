# YEScape 2.0

# Phase 4.3

# Score Fusion Engine

---

## Objective

The Score Fusion Engine combines the outputs of all verification signals into a single Trust Score.

Instead of making decisions using one signal, YEScape evaluates multiple independent signals and computes a weighted score representing the overall trustworthiness of an internship offer.

---

# Inputs

The Fusion Engine currently receives five verification signals.

| Signal | Description |
|---------|-------------|
| Signal 1 | Offer Letter Analysis |
| Signal 2 | Domain Verification |
| Signal 3 | Company Verification |
| Signal 4 | Recruiter Verification |
| Signal 5 | Context Analysis |

---

# Weight Distribution

Each signal contributes a fixed percentage to the final score.

| Signal | Weight |
|---------|--------|
| Offer Letter | 20% |
| Domain | 20% |
| Company | 20% |
| Recruiter | 20% |
| Context | 20% |

Total Weight = 100%

---

# Final Trust Score

The final score is calculated as

Final Score =

Offer × 0.20

+

Domain × 0.20

+

Company × 0.20

+

Recruiter × 0.20

+

Context × 0.20

---

# Risk Classification

The final trust score is converted into a user-friendly risk level.

| Score | Risk |
|--------|------|
| 80–100 | SAFE |
| 50–79 | CAUTION |
| 0–49 | HIGH RISK |

Each risk level is associated with a UI color.

SAFE → Green

CAUTION → Yellow

HIGH RISK → Red

---

# Confidence Calculation

Confidence indicates how complete the extracted information is.

It is currently determined using the Offer Parser.

Required fields:

- Company
- Website
- Recruiter Email
- Salary

If every required field is extracted successfully

Confidence = 100%

---

# Reason Aggregation

The Fusion Engine generates simple explanations describing why an internship received its score.

Example:

✓ Offer contains sufficient information.

✓ Website domain appears trustworthy.

✓ Company verified in registry.

✓ Recruiter email is trustworthy.

✓ Offer content appears legitimate.

These reasons improve transparency and help users understand the decision.

---

# Output

The Fusion Engine returns

Final Trust Score

Risk Level

Risk Color

Confidence

Reasons

These values are stored inside the Verification Result Schema and later displayed by the Streamlit application and Chrome Extension.

---

# Status

Phase 4.3 Completed

Score Fusion Engine Fully Integrated