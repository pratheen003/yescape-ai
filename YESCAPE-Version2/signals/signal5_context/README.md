# Signal 5 — Context Trust

## Objective

Evaluate the internship offer itself by analyzing textual content.

Unlike previous signals that verify domains, companies, and recruiters, Signal 5 focuses on identifying suspicious language, scam indicators, unrealistic claims, and contextual red flags commonly found in fraudulent internship offers.

---

## Modules

- 3.5.1 Scam Keyword Detection
- 3.5.2 Urgency Detection
- 3.5.3 Advance Fee Detection
- 3.5.4 Salary Validation
- 3.5.5 Contact Information Validation
- 3.5.6 Grammar & Writing Quality
- 3.5.7 Context Trust Score

---

## 3.5.1 Scam Keyword Detection

### Objective

Detect scam-related phrases frequently used in fake internship offers.

Instead of relying only on machine learning, YEScape also performs deterministic keyword analysis to improve explainability and identify explicit scam indicators.

### Examples

- Registration Fee
- Processing Fee
- Security Deposit
- Pay Now
- Wire Transfer
- Bank Transfer
- Guaranteed Job
- 100% Placement
- Easy Money
- Earn From Home
- Investment Required

### Output

- Matched Scam Keywords
- Keyword Count
- Scam Keyword Score (0–100)

### Interpretation

| Score | Meaning |
|------:|---------|
| 90–100 | No suspicious keywords detected |
| 70–89 | Few suspicious phrases |
| 40–69 | Multiple scam indicators |
| Below 40 | Highly suspicious content |

### Status

Completed

---

## 3.5.2 Urgency Detection

### Objective

Detect psychological pressure tactics commonly used in fraudulent internship offers.

Examples

- Hurry
- Apply Immediately
- Offer Expires Today
- Limited Seats
- Last Date
- Act Now
- Closing Soon
- Within 24 Hours

### Output

- Matched Urgency Phrases
- Urgency Count
- Urgency Score (0–100)

### Interpretation

| Score | Meaning |
|------:|---------|
| 90–100 | No urgency tactics |
| 70–89 | Mild urgency |
| 40–69 | Moderate pressure |
| Below 40 | Strong urgency manipulation |

### Status

Completed

---

## Current Progress

Completed

- ✅ 3.5.1 Scam Keyword Detection
- ✅ 3.5.2 Urgency Detection

Remaining

- ⬜ 3.5.3 Advance Fee Detection
- ⬜ 3.5.4 Salary Validation
- ⬜ 3.5.5 Contact Information Validation
- ⬜ 3.5.6 Grammar & Writing Quality
- ⬜ 3.5.7 Context Trust Score

---

Version

YEScape 2.0

## 3.5.3 Advance Fee Detection

### Objective

Detect whether the internship requires any payment before selection or joining.

Unlike scam keyword detection, this module specifically focuses on monetary requests made to candidates.

### Examples

- Registration Fee
- Processing Fee
- Training Fee
- Security Deposit
- Bank Transfer
- UPI Payment
- Joining Fee

### False Positive Handling

The detector ignores common negated statements such as:

- No registration fee
- No application fee
- No payment required

to avoid penalizing legitimate internship offers.

### Output

- Matched Fee Keywords
- Fee Keyword Count
- Advance Fee Detected (True/False)
- Advance Fee Score (0–100)

### Status

Completed

## 3.5.4 Salary Reasonableness

### Objective

Estimate whether the internship stipend or salary falls within a realistic range.

Scam offers frequently advertise unusually high salaries to attract applicants.

### Salary Categories

| Monthly Salary | Interpretation |
|---------------:|----------------|
| ≤ ₹15,000 | Typical Internship |
| ₹15,001–30,000 | Reasonable |
| ₹30,001–50,000 | Slightly High |
| > ₹50,000 | Potentially Unrealistic |

### Output

- Salary Found
- Extracted Salary
- Salary Score
- Reason

### Status

Completed

## 3.5.5 Contact Information Validation

### Objective

Verify whether the internship offer includes sufficient contact information.

Legitimate internship offers generally include:

- Company Email
- Phone Number
- Official Website

Missing contact information is a common characteristic of fraudulent offers.

### Output

- Emails Found
- Phone Number Found
- Website Found
- Contact Score (0–100)

### Status

Completed

## 3.5.6 Grammar & Writing Quality

### Objective

Evaluate the grammatical quality of internship offer text.

Scam messages often contain poor grammar, spelling mistakes, incorrect capitalization, and awkward sentence construction.

This module uses LanguageTool to estimate writing quality.

### Output

- Grammar Error Count
- Grammar Score (0–100)

### Technology

- language-tool-python
- English (US) grammar rules

### Status

Completed

## 3.5.7 Context Trust Score Fusion

### Objective

Combine all Context Analysis modules into one overall trust score.

### Inputs

- Scam Keyword Score
- Urgency Score
- Advance Fee Score
- Salary Score
- Contact Score
- Grammar Score

### Weights

| Module | Weight |
|---------|--------:|
| Scam Keyword | 25% |
| Urgency | 15% |
| Advance Fee | 20% |
| Salary | 15% |
| Contact | 15% |
| Grammar | 10% |

### Output

- Individual Module Scores
- Final Context Trust Score (0–100)

### Status

Completed