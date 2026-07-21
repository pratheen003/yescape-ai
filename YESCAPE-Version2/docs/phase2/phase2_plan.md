# YEScape 2.0 – Phase 2 Plan

## Version

Version: 1.0

---

# Phase Name

Phase 2 – Text Classification Engine

---

# Objective

Build the baseline machine learning classifier that predicts whether a job or internship posting is fraudulent based solely on textual information.

This model serves as Signal 1 of the YEScape multi-signal trust framework.

---

# Input

Processed Dataset

processed_dataset_v2.csv

Target Column

fraudulent

Feature Column

clean_text

---

# Pipeline

Processed Dataset

↓

Train-Test Split

↓

TF-IDF Vectorization

↓

Feature Matrix

↓

XGBoost Classifier

↓

Prediction

↓

Performance Evaluation

↓

Baseline Model

---

# Deliverables

- TF-IDF Vectorizer
- Feature Matrix
- Train/Test Split
- XGBoost Baseline
- Saved Model
- Evaluation Metrics

---

# Expected Outputs

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Confusion Matrix

---

# Next Phase

Phase 3

Independent Trust Signals