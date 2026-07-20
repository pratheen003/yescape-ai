# YEScape 2.0 Dataset Design

## Version

Version: 1.0

## Last Updated

20 July 2026

## Status

Draft

---

# Objective

The YEScape Internship Benchmark Dataset is designed to evaluate AI systems that verify the legitimacy of internship opportunities.

Unlike existing fake job datasets that focus on general employment fraud, this dataset specifically targets internship-related scams by incorporating multiple independent trust signals.

This dataset is intended primarily for benchmarking and evaluation rather than large-scale model training.

---

# Dataset Sources

The dataset consists of two categories.

## Training Dataset

Primary Dataset

- EMSCAD (Employment Scam Aegean Dataset)

Secondary Dataset

- Kaggle Fake Job Postings Dataset

These datasets are used only to train the baseline text-classification model.

---

## Evaluation Dataset (YEScape Internship Benchmark Dataset)

The evaluation dataset is manually curated from publicly available internship scam reports and legitimate internship opportunities.

Sources include:

- Reddit internship scam discussions
- Consumer complaint forums
- Public scam reports
- University internship notices
- Company internship portals
- Government internship portals
- Verified internship programs

No automated scraping of LinkedIn or private platforms will be performed.

---

# Dataset Purpose

The benchmark dataset is designed to evaluate whether combining multiple trust signals improves internship scam detection compared to text-only machine learning models.

---

# Dataset Structure

Each record contains one internship opportunity.

| Column                    | Description                       |
|---------------------------|-----------------------------------|
| Sample ID                 | Unique sample identifier          |
| Offer Text                | Internship description or message |
| Company Name              | Company mentioned                 |
| Website                   | Claimed website                   |
| Recruiter Email           | Recruiter contact email           |
| Domain                    | Extracted website domain          |
| Source                    | Public source URL or reference    |
| Verdict                   | Scam / Legitimate / Unverifiable  |
| Ground Truth              | Final verified label              |
| Labeler ID                | Annotator responsible             |

---

# Dataset Categories

The benchmark contains three classes.

## Legitimate

Verified internship opportunity.

Requirements:

- Company exists
- Domain matches company
- No suspicious payment request
- Recruiter identity consistent

---

## Scam

Internship opportunity identified as fraudulent.

Possible indicators include:

- Registration fee
- Fake recruiter
- Fake company
- Suspicious domain
- Identity mismatch
- Pressure tactics

---

## Unverifiable

Cases where evidence is insufficient.

Examples include:

- Missing company information
- Missing recruiter identity
- Website unavailable
- Insufficient evidence

These samples are intentionally preserved instead of forcing incorrect labels.

---

# Target Dataset Size

| Category | Target Samples |
|------------|---------------|
| Legitimate | 150–200 |
| Scam | 150–200 |
| Unverifiable | 50–100 |

Total Target Size

300–500 samples

---

# Data Quality Principles

The dataset follows five quality principles.

- Publicly verifiable
- Human reviewed
- No duplicate samples
- Balanced class distribution
- Reproducible collection process

---

# Ethical Considerations

The dataset does not include:

- Private user information
- Confidential internship offers
- Personal recruiter details beyond publicly visible information

The dataset is intended solely for academic research and AI benchmarking.

---

# Expected Output

This dataset will be used to evaluate:

- Text Classification Model
- Multi-Signal Fusion Engine
- Explainable AI Module
- Overall YESScore Accuracy

It serves as the primary evaluation benchmark for YEScape 2.0.