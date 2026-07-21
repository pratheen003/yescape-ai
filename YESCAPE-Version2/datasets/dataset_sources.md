# YEScape 2.0 Dataset Sources

## Version

Version: 1.0

---

# Objective

YEScape 2.0 is designed as a multi-signal internship scam detection framework.

To ensure reproducibility and scientific validity, the framework is built upon publicly available benchmark datasets combined with a custom internship-specific benchmark dataset.

The public datasets are used for training the text classification model, while the custom internship benchmark dataset is used to evaluate the complete multi-signal trust framework.

---

# Dataset Categories

The project uses three datasets.

| Dataset | Purpose | Usage |
|----------|----------|------|
| EMSCAD | Primary Training Dataset | Machine Learning |
| Kaggle Fake Job Postings | Secondary Training Dataset | Model Validation |
| Internship Benchmark Dataset | Evaluation Dataset | Final System Evaluation |

---

# Dataset 1

## EMSCAD Dataset

Purpose

Primary dataset for supervised text classification.

Reason for Selection

- One of the most widely cited fake job datasets.
- Publicly available.
- Balanced scam and legitimate job postings.
- Suitable for baseline model development.

Used For

- TF-IDF Feature Extraction
- XGBoost Training
- DistilBERT Benchmark (optional)
- Baseline Evaluation

---

# Dataset 2

## Kaggle Fake Job Postings

Purpose

Secondary benchmark dataset.

Reason for Selection

- Contains thousands of labeled fake and legitimate job advertisements.
- Independent source for validating model generalization.
- Allows comparison with EMSCAD.

Used For

- Cross-validation
- Model robustness testing
- Baseline comparison

---

# Dataset 3

## Internship Benchmark Dataset

Purpose

Custom evaluation dataset developed for YEScape 2.0.

Reason for Selection

Existing public datasets focus on general employment fraud.

However, internship scams exhibit different characteristics including:

- Training fee scams
- Fake HR recruiters
- Temporary domains
- Internship certificates without employment
- College-targeted recruitment scams

This dataset addresses the internship-specific research gap.

---

# Dataset Usage Strategy

Training

EMSCAD

↓

Kaggle Fake Job Postings

↓

Machine Learning Model

↓

YEScape Signal 1

---

Evaluation

Internship Benchmark Dataset

↓

Five Trust Signals

↓

Fusion Model

↓

YESScore

---

# Research Contribution

The Internship Benchmark Dataset represents the primary research contribution of YEScape 2.0.

Unlike existing datasets, it focuses exclusively on internship fraud and supports evaluation of multi-signal trust fusion rather than text classification alone.

---

# Current Status

EMSCAD Dataset
Pending Download

Kaggle Fake Job Postings
Pending Download

Internship Benchmark Dataset
Design Completed
Collection Pending