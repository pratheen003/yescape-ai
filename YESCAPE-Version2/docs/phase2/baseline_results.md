# Phase 2.2 — XGBoost Baseline Results

## Objective

Train a reproducible baseline machine learning model for internship scam detection using TF-IDF features and XGBoost classification.

This baseline serves as Signal 1 (ML Scam Probability) within the YEScape 2.0 Multi-Signal Fusion Architecture.

---

## Dataset

Processed Dataset Version:
processed_dataset_v2.csv

Training Samples:
14,116

Testing Samples:
3,529

Class Distribution:

- Legitimate: 95%
- Fraudulent: 5%

---

## Feature Engineering

Feature Extraction:
TF-IDF Vectorization

Vocabulary Size:
5000

Text Source:
clean_text

---

## Model

Algorithm:
XGBoost Classifier

Parameters:

- Objective: binary:logistic
- Estimators: 100
- Learning Rate: 0.1
- Maximum Depth: 6
- Random State: 42

---

## Performance

| Metric       | Score     |
|--------------|-----------|
| Accuracy     | 97.96%    |
| Precision    | 93.86%    |
| Recall       | 62.21%    |
| F1 Score     | 74.83%    |
| ROC-AUC      | 97.73%    |

---

## Confusion Matrix

```
[[3350    7]
 [  65  107]]
```

---

## Interpretation

The baseline classifier demonstrates excellent discrimination capability with a ROC-AUC of 97.73%.

Precision is very high, indicating that when the model predicts an internship as fraudulent, it is correct approximately 94% of the time.

Recall remains moderate because of the highly imbalanced dataset, where only approximately 5% of samples are fraudulent.

Improving recall will be addressed in later phases through Multi-Signal Fusion rather than modifications to the baseline classifier.

---

## Status

Phase 2.2 Completed Successfully.

This model becomes Signal 1 of the YEScape 2.0 Trust Scoring Engine.