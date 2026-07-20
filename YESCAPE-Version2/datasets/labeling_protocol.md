# YEScape 2.0 Labeling Protocol

## Version

Version: 1.0

## Last Updated

20 July 2026

## Status

Draft

---

# Purpose

This document defines the labeling procedure used to assign ground-truth labels for the YEScape Internship Benchmark Dataset.

The objective is to ensure consistency, transparency, and reproducibility across all dataset annotations.

---

# Label Classes

Each internship sample must receive one of three labels.

| Label | Description |
|--------|-------------|
| Legitimate | Internship verified as genuine |
| Scam | Internship identified as fraudulent |
| Unverifiable | Evidence insufficient for verification |

---

# Legitimate Label Rules

Assign "Legitimate" only if all of the following conditions are satisfied.

✓ Company exists

✓ Official website available

✓ Recruiter identity appears consistent

✓ No payment request

✓ Internship information appears reasonable

---

# Scam Label Rules

Assign "Scam" if one or more high-confidence fraud indicators are present.

Examples include:

- Registration fee required
- Training fee required
- Recruiter email unrelated to company
- Fake company identity
- Fake website
- Newly created suspicious domain
- Urgent pressure language
- Unrealistic salary promises
- Grammar patterns commonly found in scam campaigns

A single extremely strong fraud indicator may be sufficient for a Scam label.

---

# Unverifiable Label Rules

Assign "Unverifiable" when available evidence is insufficient.

Examples include:

- Company cannot be confirmed
- Website unavailable
- Recruiter identity missing
- Limited internship information
- Conflicting public information

Do not force a Scam or Legitimate label without adequate evidence.

---

# Labeling Workflow

```text
Collect Internship Sample
            │
            ▼
Review Internship Content
            │
            ▼
Verify Company
            │
            ▼
Verify Website
            │
            ▼
Verify Recruiter
            │
            ▼
Check Scam Indicators
            │
            ▼
Assign Preliminary Label
            │
            ▼
Second Reviewer Validation
            │
            ▼
Ground Truth Label
```

---

# Independent Review

To improve dataset reliability:

- Two independent reviewers will annotate approximately 20% of the dataset.
- Reviewer disagreements will be discussed.
- Final labels will be agreed upon before inclusion.

---

# Inter-Annotator Agreement

Dataset consistency will be measured using:

Cohen's Kappa Score

Interpretation:

| Kappa Score | Agreement |
|--------------|-----------|
| >0.80 | Excellent |
| 0.60–0.80 | Good |
| 0.40–0.60 | Moderate |
| <0.40 | Poor |

Target:

Kappa ≥ 0.80

---

# Label Priority

When multiple signals conflict, follow this priority order.

1. Official Government Registry
2. Official Company Website
3. Recruiter Identity
4. Domain Verification
5. Internship Content Analysis

Higher-priority evidence overrides lower-priority indicators.

---

# Evidence Recording

Each labeled sample should maintain supporting evidence.

Examples:

- Company registry verification
- Domain age
- Safe Browsing result
- Official website match
- Recruiter email verification
- Scam indicators identified

Evidence should be documented whenever possible to support reproducibility.

---

# Final Dataset Approval

A sample enters the benchmark dataset only after:

✓ Complete review

✓ Label assigned

✓ Evidence verified

✓ Reviewer approval recorded

This protocol ensures the YEScape Internship Benchmark Dataset remains transparent, reproducible, and suitable for research evaluation.