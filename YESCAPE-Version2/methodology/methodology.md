# YEScape 2.0 Methodology

## Version

Version: 1.0

## Last Updated

20 July 2026

## Status

Draft

---

# Project Title

YEScape 2.0: A Multi-Signal Fusion Framework for Internship Scam Detection Using Machine Learning, Trust Intelligence, and Explainable Artificial Intelligence

---

# 1. Objective

YEScape 2.0 is designed to verify the legitimacy of internship opportunities using multiple independent trust signals rather than relying solely on text classification.

Existing internship scam detection systems primarily analyse textual content. However, many real-world internship scams imitate legitimate writing styles while hiding their fraudulent nature through fake recruiter identities, recently registered domains, non-existent companies, and psychological manipulation.

To address this limitation, YEScape introduces a Multi-Signal Trust Fusion Framework that combines evidence from independent verification modules using a trained Logistic Regression meta-model.

The output of this framework is an explainable trust score called YESScore.

---

# 2. Methodology Overview

The proposed methodology consists of six sequential stages.

1. Input Collection

The system accepts internship offers in the form of

- Internship URL
- PDF Offer Letter
- Plain Text Description

---

2. Feature Extraction

Relevant information is extracted from the input.

Examples include

- Company Name
- Recruiter Email
- Website Domain
- Internship Description
- Contextual Language Features

---

3. Independent Trust Signal Generation

Instead of making a prediction directly from the internship description, the extracted information is evaluated by five independent trust verification modules.

Each module independently produces a trust score ranging from 0 to 100.

---

4. Multi-Signal Fusion

The five trust scores are combined using a Logistic Regression meta-model.

Unlike weighted averaging or manually assigned scores, Logistic Regression learns the contribution of every trust signal during model training.

This stage generates a unified internship trust score called YESScore.

---

5. Explainable AI

The generated YESScore is explained using SHAP.

SHAP identifies

- Positive evidence supporting legitimacy
- Negative evidence indicating fraud
- Contribution of every verification signal

This ensures every prediction remains transparent and interpretable.

---

6. Final Decision

Based on YESScore, the internship is categorized as

- Safe
- Caution
- Risky
- Scam

The user receives a detailed AI-generated verification report.

---

# 3. Multi-Signal Trust Fusion

YEScape differs from traditional scam detection systems by separating verification into five independent trust signals.

Signal 1
Machine Learning Scam Probability

Purpose

Estimate the probability that the internship text resembles fraudulent postings using supervised machine learning.

Input

Internship description

Output

ML Trust Score

---

Signal 2
Domain Intelligence

Purpose

Evaluate the trustworthiness of the internship website.

Checks include

- Domain Age
- WHOIS Information
- Registrar
- Google Safe Browsing Status

Output

Domain Trust Score

---

Signal 3
Recruiter Identity Verification

Purpose

Verify recruiter authenticity.

Checks include

- Recruiter Email Domain
- Domain Matching
- Manual LinkedIn Verification Flag

Output

Recruiter Trust Score

---

Signal 4
Company Verification

Purpose

Verify whether the company exists and matches official public records.

Checks include

- MCA Registration
- GST Verification
- Official Company Website

Output

Company Trust Score

---

Signal 5
Context Intelligence

Purpose

Analyse contextual scam behaviour rather than keywords alone.

Checks include

- Urgency
- Pressure Language
- Payment Requests
- Psychological Manipulation
- Grammar Quality

Output

Context Trust Score

---

# 4. Fusion Strategy

Each verification module generates a normalized trust score.

The resulting feature vector is

[
ML Trust,
Domain Trust,
Recruiter Trust,
Company Trust,
Context Trust
]

This feature vector becomes the input to a Logistic Regression meta-model.

The model learns the contribution of every signal during training and predicts the overall internship legitimacy.

The predicted probability is transformed into YESScore ranging from 0 to 100.

---

# 5. Explainability

YEScape does not produce black-box predictions.

SHAP is applied to the trained fusion model to explain every decision.

The explanation includes

- Most influential positive signals
- Most influential negative signals
- Individual contribution of every trust signal

This provides complete transparency to both users and reviewers.

---

# 6. Expected Contributions

The proposed methodology contributes

- Internship-specific scam verification
- Multi-signal trust intelligence
- Logistic Regression based trust fusion
- Explainable AI decision support
- Reproducible verification pipeline
- Research benchmark for internship scam detection

---

# 7. Expected Outcome

The framework is expected to

- Improve scam detection reliability
- Reduce dependence on text-only classification
- Increase prediction transparency
- Support reproducible academic evaluation
- Serve as the foundation for future internship verification platforms.