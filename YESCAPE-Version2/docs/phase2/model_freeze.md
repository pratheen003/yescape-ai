# Phase 2.3 — Model Freeze

## Purpose

The XGBoost baseline model is officially frozen as the baseline classifier for YEScape 2.0.

No additional tuning, balancing, or optimization will be performed on this model.

All future improvements will be measured against this baseline.

---

# Signal Assignment

Signal Name

Signal 1 — ML Scam Probability

Algorithm

TF-IDF + XGBoost

Input

clean_text

Output

Probability between 0 and 1

Example

0.93

↓

93% Scam Probability

---

# Baseline Metrics

Accuracy

97.96%

Precision

93.86%

Recall

62.21%

F1 Score

74.83%

ROC-AUC

97.73%

---

# Why Freeze Here?

Research requires a reproducible baseline.

Improving the model before benchmarking would invalidate later comparisons.

Future improvements will be introduced through Multi-Signal Fusion rather than modifications to this baseline.

---

# Status

Signal 1 Completed.

This model will now be used unchanged throughout the remaining research pipeline.