# Signal 5 – Context Analysis

## Overview

Signal 5 analyzes the textual content of internship offers.

Unlike previous signals that validate domains or recruiters, this signal evaluates whether the message itself contains suspicious patterns.

---

# Objectives

- Detect scam-related keywords.
- Detect urgency tactics.
- Detect advance fee requests.
- Validate salary claims.
- Verify contact information.
- Evaluate grammar quality.
- Produce Context Trust Score.

---

# Architecture

Offer Letter
      │
      ▼
Scam Keyword Detection
      │
      ▼
Urgency Detection
      │
      ▼
Advance Fee Detection
      │
      ▼
Salary Validation
      │
      ▼
Contact Validation
      │
      ▼
Grammar Analysis
      │
      ▼
Context Trust Score

---

# Phase Breakdown

## Phase 3.5.1

### Scam Keyword Detection

Detect phrases such as

- guaranteed job
- registration fee
- immediate joining
- limited seats

Output

Scam Keyword Score

---

## Phase 3.5.2

### Urgency Detection

Detect pressure tactics

Examples

- Hurry
- Apply today
- Offer expires
- Immediate payment

Output

Urgency Score

---

## Phase 3.5.3

### Advance Fee Detection

Detect financial requests

Examples

- Registration Fee
- Processing Fee
- Security Deposit
- UPI Payment

Negation handling

- No Registration Fee
- No Payment Required

Output

Advance Fee Score

---

## Phase 3.5.4

### Salary Validation

Extract salary using Regular Expressions.

Compare against internship salary thresholds.

Categories

- Typical Internship
- Reasonable
- High
- Unrealistic

Output

Salary Score

---

## Phase 3.5.5

### Contact Validation

Verify presence of

- Email
- Phone Number
- Website

Output

Contact Score

---

## Phase 3.5.6

### Grammar Checker

Uses

LanguageTool

Measures

- Grammar
- Spelling
- Writing Quality

Output

Grammar Score

---

## Phase 3.5.7

### Context Trust Score

Combine

- Scam Keywords
- Urgency
- Advance Fee
- Salary
- Contact
- Grammar

Weights

| Module | Weight |
|---------|--------|
| Scam Keywords | 25% |
| Urgency | 15% |
| Advance Fee | 20% |
| Salary | 15% |
| Contact | 15% |
| Grammar | 10% |

Output

Context Trust Score (0–100)

---

# Folder Structure

signals/

signal5_context/

    scam_keyword_detector.py

    urgency_detector.py

    advance_fee_detector.py

    salary_validator.py

    contact_validator.py

    grammar_checker.py

    context_score.py

---

# Example

Legitimate Offer

Context Trust Score

95.25

Scam Offer

Context Trust Score

48.50

---

# Advantages

- Detects scam language.
- Detects urgency tactics.
- Detects advance fee fraud.
- Validates internship salary.
- Modular architecture.
- Explainable scoring.

---

# Limitations

- Rule-based keyword detection.
- Grammar quality depends on LanguageTool.
- Salary thresholds are static.
- Does not analyze intent using LLMs.

---

# Future Improvements

- LLM-based semantic analysis.
- Sentiment Analysis.
- Emotion Detection.
- Scam Pattern Learning.
- Multi-language Support.