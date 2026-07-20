# YEScape 2.0 Fusion Model Design

## Version

Version: 1.0

## Last Updated

20 July 2026

## Status

Draft

---

# Objective

The Fusion Model is the core intelligence layer of YEScape 2.0.

Instead of averaging multiple trust scores, the system learns how different verification signals interact and predicts a final internship legitimacy score (YESScore).

This transforms YEScape from a rule-based scoring engine into a machine learning–driven decision support system.

---

# Why a Fusion Model?

Traditional scam detection systems often depend on a single source of information, such as text classification or manually assigned rules.

However, internship fraud is a multi-dimensional problem.

A scam internship may:

- contain professional language
- use a fake recruiter email
- have a newly registered domain
- impersonate a legitimate company
- request payment before onboarding

No single signal can reliably detect every scenario.

The Fusion Model combines independent evidence from multiple verification modules to produce a more accurate prediction.

---

# Input Signals

The Fusion Model receives five normalized trust scores.

| Signal | Description | Range |
|---------|-------------|------:|
| ML Scam Probability | Output from the text classification model | 0–100 |
| Domain Trust | Website age, HTTPS status, Google Safe Browsing | 0–100 |
| Recruiter Trust | Email-domain verification and recruiter legitimacy | 0–100 |
| Company Trust | MCA, GST and official company verification | 0–100 |
| Context Trust | Fee requests, urgency, pressure tactics and contextual analysis | 0–100 |

---

# Fusion Strategy

The five trust signals are combined using a supervised machine learning model.

Candidate models include:

- Logistic Regression
- Random Forest
- Gradient Boosting

Each model will be evaluated using cross-validation.

The best-performing model will become the final Fusion Engine.

---

# Selected Initial Model

The initial implementation uses:

**Logistic Regression**

Reasons:

- Highly interpretable
- Fast training
- Low computational cost
- Suitable for small and medium datasets
- Produces calibrated probabilities
- Easily explainable using SHAP

Future versions may replace Logistic Regression if another model consistently outperforms it.

---

# Fusion Workflow

```
ML Scam Probability
        │
        │
Domain Trust
        │
        │
Recruiter Trust
        │
        │
Company Trust
        │
        │
Context Trust
        │
        ▼
Feature Vector
        │
        ▼
Logistic Regression
        │
        ▼
YESScore Probability
        │
        ▼
SAFE / CAUTION / RISKY / SCAM
```

---

# Feature Vector

The input feature vector is represented as:

```
[
 ML_Probability,
 Domain_Trust,
 Recruiter_Trust,
 Company_Trust,
 Context_Trust
]
```

Each feature is normalized to the range 0–100 before training.

---

# Training Strategy

Training data consists of:

- EMSCAD
- Kaggle Fake Job Postings Dataset

Evaluation uses:

- Internship Benchmark Dataset

The benchmark dataset is never used for model training.

---

# Cross Validation

The Fusion Model will be evaluated using K-Fold Cross Validation.

This reduces variance and provides a more reliable estimate of real-world performance.

---

# Model Output

The model predicts:

- YESScore (0–100)

The YESScore is mapped to four decision categories:

| YESScore | Decision |
|----------:|-----------|
| 80–100 | SAFE |
| 60–79 | CAUTION |
| 40–59 | RISKY |
| 0–39 | SCAM |

---

# Explainability

The Fusion Model is designed to support Explainable AI.

SHAP values will identify how much each signal contributed to the final YESScore.

Example:

- Domain Trust: +18
- Company Trust: +14
- Recruiter Trust: -22
- Context Trust: -11

This allows users to understand why the system reached its decision.

---

# Expected Advantages

Compared with simple weighted averaging, the Fusion Model:

- Learns relationships between signals
- Reduces manual bias
- Improves prediction consistency
- Supports future retraining
- Enables explainable decision making
- Provides stronger research contribution

---

# Future Improvements

Future versions may investigate:

- XGBoost Fusion
- LightGBM Fusion
- Neural Network Fusion
- Dynamic confidence weighting
- Online model updates
- Active learning from verified user feedback