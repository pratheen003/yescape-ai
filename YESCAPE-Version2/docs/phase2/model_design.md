# YEScape 2.0 Model Design

## Version

Version: 1.0

---

# Purpose

The first AI model in YEScape predicts whether a posting is fraudulent using textual information only.

This model forms the first trust signal within the overall YESScore architecture.

---

# Model Type

Supervised Binary Classification

---

# Input

clean_text

---

# Output

fraudulent

0 = Legitimate

1 = Fraudulent

---

# Algorithm

TF-IDF

↓

XGBoost

---

# Why TF-IDF?

TF-IDF transforms textual information into numerical vectors while emphasizing informative words and reducing the influence of extremely common terms.

Advantages

- Fast
- Interpretable
- Proven baseline
- Research standard

---

# Why XGBoost?

XGBoost provides

- High predictive performance
- Handles sparse TF-IDF vectors efficiently
- Built-in feature importance
- Compatible with SHAP Explainability

---

# Role in YEScape

Signal 1

ML Scam Probability

↓

Fusion Engine

↓

YESScore