# YEScape 2.0 Feature Selection

## Version

Version: 1.0

---

# Purpose

This document defines how every dataset feature is used within the YEScape 2.0 architecture.

The objective is to ensure that only meaningful attributes are retained for machine learning, trust signal generation, and explainable fraud detection.

Every feature is classified before preprocessing begins.

---

# Feature Classification

| Feature | Category | Decision | Reason |
|----------|----------|----------|--------|
| job_id | Remove | ❌ Drop | Unique identifier. No predictive value. |
| title | ML Feature | ✅ Keep | Job title contains semantic information about the internship. |
| location | Metadata | ✅ Keep | Geographic information may support later verification. |
| department | Remove | ❌ Drop | Extremely sparse (>60% missing) with low predictive importance. |
| salary_range | Remove | ❌ Drop | More than 80% missing values make this unreliable. |
| company_profile | ML Feature | ✅ Keep | Company descriptions help distinguish legitimate organizations from fake ones. |
| description | ML Feature | ✅ Keep | Primary textual feature used for fraud classification. |
| requirements | ML Feature | ✅ Keep | Strong indicator of posting legitimacy and recruiter intent. |
| benefits | ML Feature | ✅ Keep | Contains useful employment-related context. |
| telecommuting | Trust Signal | ✅ Keep | Useful behavioural indicator for remote-job fraud analysis. |
| has_company_logo | Trust Signal | ✅ Keep | Presence of company branding improves trust estimation. |
| has_questions | Trust Signal | ✅ Keep | Recruitment process indicator useful for trust modelling. |
| employment_type | Metadata | ✅ Keep | Internship, Full-time, Part-time etc. provide contextual information. |
| required_experience | Metadata | ✅ Keep | Helps identify unrealistic experience requirements. |
| required_education | Metadata | ✅ Keep | Useful contextual attribute for internship analysis. |
| industry | Metadata | ✅ Keep | Industry verification may assist trust estimation. |
| function | Metadata | ✅ Keep | Functional role information supports contextual analysis. |
| fraudulent | Target Label | ✅ Keep | Ground truth used for supervised learning. |
| in_balanced_dataset | Remove | ❌ Drop | Artificial balancing indicator. Not a real-world feature. |

---

# Final Feature Groups

## Signal 1 — Machine Learning Features

These textual attributes will be combined and converted into TF-IDF vectors for the baseline XGBoost classifier.

- title
- company_profile
- description
- requirements
- benefits

---

## Signal 2 — Domain Intelligence

(Not available in the EMSCAD dataset)

Generated dynamically during prediction.

- Domain age
- HTTPS availability
- Registrar information
- Google Safe Browsing status

---

## Signal 3 — Recruiter Identity

(Not available in the EMSCAD dataset)

Generated dynamically.

- Recruiter email
- Email-domain consistency
- Company-domain matching

---

## Signal 4 — Company Verification

Partially supported by dataset metadata and later enriched using external public registries.

Relevant metadata:

- company_profile
- industry
- function
- location

External verification sources:

- MCA Registry
- GST Registry
- Official company website

---

## Signal 5 — Context Intelligence

Derived during inference using NLP techniques.

Primary textual inputs:

- description
- requirements
- benefits

Generated indicators include:

- urgency language
- payment requests
- grammatical quality
- suspicious wording
- psychological pressure

---

# Features Removed

The following features are excluded from the learning pipeline.

- job_id
- department
- salary_range
- in_balanced_dataset

Reasons:

- Identifier-only information
- Extremely sparse
- Artificial balancing metadata
- No contribution to fraud prediction

---

# Outcome

After feature selection, YEScape 2.0 retains only features that contribute to:

- Machine Learning
- Trust Signal Generation
- Explainability
- Internship-specific fraud detection

This feature selection serves as the foundation for Phase 1.3 (Data Cleaning) and Phase 2 (Text Classification Engine).