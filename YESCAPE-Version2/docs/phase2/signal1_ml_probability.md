# Signal 1 — ML Scam Probability

## Objective

Estimate the likelihood that an internship posting is fraudulent based solely on textual content.

---

## Input

clean_text

---

## Feature Extraction

TF-IDF

Vocabulary Size

5000

---

## Classifier

XGBoost

---

## Output

Continuous probability

0.00

↓

Legitimate

1.00

↓

Fraudulent

---

## Role Inside YEScape

Signal 1 contributes one of the five independent trust signals used by the YESScore Fusion Engine.

It does not produce the final trust score.

The final YESScore is calculated only after combining all five signals.

---

## Advantages

Excellent precision

Fast inference

Lightweight

Explainable with SHAP

Suitable for production deployment

---

## Limitations

Uses only textual information.

Cannot verify

- Company legitimacy

- Recruiter identity

- Website authenticity

- Domain age

Those checks are handled in later phases.