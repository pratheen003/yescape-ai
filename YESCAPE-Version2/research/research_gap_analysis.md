# Phase 0.3 – Research Gap Analysis

# Research Gap Analysis

## Last Updated

20 July 2026

## Status

Draft

---

## Overview

Numerous studies have explored fake job detection using machine learning, deep learning, and rule-based techniques. These studies have significantly improved textual fraud classification by learning linguistic patterns associated with fraudulent recruitment advertisements.

However, internship verification presents additional challenges that extend beyond textual analysis alone. Verifying internship legitimacy often requires independent evidence regarding recruiter authenticity, company legitimacy, website credibility, and contextual behavioural indicators.

This creates a research opportunity for developing an internship-specific verification methodology capable of integrating heterogeneous trust evidence into a unified decision-support framework.

---

# Existing Research Categories

Current literature can broadly be divided into four categories.

## 1. Traditional Machine Learning

These approaches employ techniques such as:

- TF-IDF
- Logistic Regression
- Random Forest
- XGBoost
- Support Vector Machines

Strengths

- Efficient
- Interpretable
- Good textual classification

Limitations

- Depend entirely on textual information.
- Unable to verify external trust evidence.

---

## 2. Deep Learning Approaches

Recent research utilizes models including:

- BERT
- DistilBERT
- RoBERTa
- LSTM

Strengths

- Superior contextual understanding
- Higher textual classification accuracy

Limitations

- Still operate primarily on textual information.
- External verification evidence is not incorporated into model decisions.

---

## 3. Rule-Based Verification Systems

These systems use manually defined verification rules.

Strengths

- Transparent
- Fast
- Easy to understand

Limitations

- Difficult to maintain
- Limited adaptability
- Poor generalization to evolving fraud patterns

---

## 4. Explainable AI Systems

These approaches employ SHAP or LIME to interpret machine learning predictions.

Strengths

- Improved transparency
- Better model interpretability

Limitations

- Explain model predictions rather than the complete verification process.
- Do not integrate heterogeneous trust evidence.

---

# Common Research Limitations

Across existing literature, several recurring limitations are observed.

- Heavy dependence on textual classification.
- Limited use of independently verifiable trust signals.
- Generic employment datasets dominate evaluation.
- Binary predictions provide limited decision support.
- Verification components remain isolated rather than integrated.

---

# Research Gap

Although substantial progress has been made in textual fake job detection, there remains no internship-specific verification framework capable of integrating machine learning prediction with independently verifiable trust evidence through supervised trust fusion while simultaneously providing transparent explainability and reproducible evaluation.

---

# YEScape 2.0 Contribution

YEScape addresses the identified research gap by introducing:

- Internship-specific verification methodology.
- Multi-signal trust assessment.
- Supervised trust fusion.
- Explainable evidence-driven YESScore.
- Internship benchmark dataset.
- Unified AI-assisted decision-support framework.

---

# Gap Analysis Summary

| Existing Limitation              |        YEScape Contribution           |
|----------------------------------|---------------------------------------|
| Text-only detection              |        Multi-signal verification      |
| Generic employment focus         |        Internship-specific framework  |
| Independent verification modules |        Unified trust fusion           |
| Black-box prediction             |        Explainable YESScore           |
| Generic evaluation datasets      |        Internship Benchmark Dataset   |
| Manual verification              |        AI-assisted decision support   |

---

# Conclusion

Rather than proposing another textual fraud classifier, YEScape 2.0 contributes a unified internship verification methodology that integrates heterogeneous trust evidence into an explainable, reproducible, and evidence-driven trust assessment framework.

This research shifts internship fraud detection from isolated classification toward comprehensive AI-assisted verification.