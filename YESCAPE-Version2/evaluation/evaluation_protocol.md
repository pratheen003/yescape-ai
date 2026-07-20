# YEScape 2.0 Evaluation Protocol

## Version

Version: 1.0

## Last Updated

20 July 2026

## Status

Draft

---

# Objective

The Evaluation Protocol defines how YEScape 2.0 will be validated throughout development.

Its purpose is to ensure that every model is evaluated using a consistent, reproducible, and scientifically sound methodology.

Rather than comparing our results directly with values reported in published research papers, YEScape compares its own baseline model against the proposed Multi-Signal Fusion Model using identical datasets and evaluation settings.

This approach provides a fair comparison and demonstrates the contribution of the proposed methodology.

---

# Evaluation Strategy

YEScape 2.0 follows a two-stage evaluation process.

## Stage 1 — Baseline Evaluation

The baseline represents a traditional text-only scam detection model.

Input:

- Internship posting text

Processing:

- TF-IDF Vectorization
- XGBoost Classifier

Output:

- Scam Probability

The baseline model is trained and evaluated before any trust signals are introduced.

This serves as the reference point for all later comparisons.

---

## Stage 2 — Fusion Model Evaluation

The proposed YEScape Fusion Model combines five independent verification signals.

Inputs:

- ML Scam Probability
- Domain Trust
- Recruiter Trust
- Company Trust
- Context Trust

Fusion Method:

- Logistic Regression

Output:

- YESScore
- Final Verdict

The Fusion Model will be evaluated using the same benchmark dataset used for the baseline evaluation.

---

# Dataset Usage

Training Dataset

- EMSCAD
- Kaggle Fake Job Postings Dataset

Evaluation Dataset

- Internship Benchmark Dataset

The Internship Benchmark Dataset is never used during model training.

It is reserved exclusively for performance evaluation.

---

# Train/Test Strategy

For the text classification model:

- Fixed Train/Test Split

The same split will be reused throughout the project.

This prevents performance differences caused by changing data partitions.

---

# Cross Validation

The Fusion Model will be evaluated using K-Fold Cross Validation.

Configuration:

- K = 5

This provides a more reliable estimate of model performance and reduces evaluation variance.

---

# Performance Metrics

The following metrics will be reported.

## Classification Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

---

## Error Analysis

The following diagnostic outputs will also be generated.

- Confusion Matrix
- ROC Curve
- Precision-Recall Curve

---

## Explainability Metrics

SHAP will be used to explain:

- Feature importance
- Individual prediction contributions

This allows each YESScore prediction to be interpreted by users and reviewers.

---

# Baseline Comparison

The following comparison will be performed.

| Component | Baseline | YEScape 2.0 |
|------------|----------|-------------|
| Text Analysis | TF-IDF + XGBoost | TF-IDF + XGBoost |
| Domain Verification | ✗ | ✓ |
| Recruiter Verification | ✗ | ✓ |
| Company Verification | ✗ | ✓ |
| Context Verification | ✗ | ✓ |
| Multi-Signal Fusion | ✗ | ✓ |
| Explainability | Limited | SHAP |
| Output | Scam Probability | YESScore |

---

# Comparative Evaluation

The same internship benchmark dataset will be evaluated twice.

Experiment 1

Baseline Model

↓

Performance Metrics

Experiment 2

Fusion Model

↓

Performance Metrics

The results will be compared directly using identical evaluation data.

This isolates the contribution of the Fusion Engine.

---

# Expected Improvements

The Fusion Model is expected to improve:

- Detection of professionally written scam internships
- Detection of company impersonation
- Detection of fake recruiter identities
- Detection of suspicious domains
- Overall prediction reliability
- Decision transparency

---

# Failure Case Analysis

Special attention will be given to difficult internship scenarios.

Examples include:

- Genuine internship with minimal information
- Professionally written scam postings
- Newly registered company websites
- Fake recruiter using free email providers
- Company impersonation using lookalike domains

Each failure case will be documented to understand model limitations.

---

# Reproducibility

To ensure reproducibility:

- Fixed random seed
- Fixed train/test split
- Version-controlled datasets
- Version-controlled preprocessing pipeline
- Version-controlled model parameters

This allows future researchers to reproduce the reported results.

---

# Deliverables

The evaluation stage will produce:

- Baseline Performance Report
- Fusion Model Performance Report
- Confusion Matrix
- ROC Curve
- Precision-Recall Curve
- SHAP Analysis
- Comparative Benchmark Report
- Failure Case Analysis

---

# Success Criteria

YEScape 2.0 will be considered successful if it demonstrates:

- Higher Accuracy than the baseline
- Higher Precision than the baseline
- Higher Recall than the baseline
- Higher F1 Score than the baseline
- Improved internship-specific fraud detection
- Transparent and explainable decision making
- Consistent performance under cross validation

---

# Final Research Goal

The objective of YEScape 2.0 is not only to achieve higher predictive performance but also to establish a reproducible, explainable, and internship-specific fraud detection framework that can serve as a reliable decision-support system for students, educational institutions, and recruiters.