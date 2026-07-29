# YEScape 2.0

# Phase 4.4.9

# Score Fusion Documentation

---

## Purpose

The Score Fusion Engine combines all signal outputs into a single Trust Score.

---

## Inputs

Signal 1

Offer Confidence

Weight

20%

---

Signal 2

Domain Trust Score

Weight

20%

---

Signal 3

Company Trust Score

Weight

20%

---

Signal 4

Recruiter Trust Score

Weight

20%

---

Signal 5

Context Trust Score

Weight

20%

---

## Formula

Final Score

=

Average of all five weighted scores

---

## Risk Levels

SAFE

80–100

GREEN

---

CAUTION

40–79

YELLOW

---

HIGH RISK

0–39

RED

---

## Confidence

Confidence is calculated from the availability of extracted offer fields.

Fields

- Company
- Website
- Recruiter Email
- Salary

Example

4 / 4 fields

↓

Confidence = 100%

---

## Reasons

The fusion engine generates user-readable explanations.

Examples

✓ Offer contains sufficient information.

✓ Company verified in registry.

✓ Recruiter email is trustworthy.

✓ Offer content appears legitimate.

---

## Output

The engine returns

- Final Score
- Risk Level
- Risk Color
- Confidence
- Reasons

These values are stored inside VerificationResult.