# Phase 0.1 – Final Problem Statement

# YEScape 2.0
## Multi-Signal Trust Fusion Framework for Internship Verification

## Last Updated

20 July 2026

## Status

Draft

---

# 1. Background

The rapid growth of digital recruitment platforms has significantly transformed the internship application process by making career opportunities more accessible to students and fresh graduates worldwide. Organizations now advertise internships through company career portals, university placement cells, professional networking platforms, online job portals, social media communities, and direct email campaigns.

While this digital transformation has increased accessibility, it has simultaneously created new opportunities for sophisticated internship fraud. Modern internship scams increasingly imitate legitimate organizations using forged offer letters, cloned company websites, impersonated recruiter identities, recently registered domains, and psychologically persuasive communication. As a result, distinguishing fraudulent internship offers from genuine opportunities has become increasingly difficult for students and educational institutions.

---

# 2. Problem Context

Students, fresh graduates, and educational institutions currently lack a unified, evidence-based mechanism for verifying the legitimacy of internship opportunities before accepting an offer.

Existing verification practices are highly fragmented and typically require users to manually investigate multiple independent sources, including:

- Official company websites
- Search engines
- Professional networking platforms
- Domain lookup services
- Discussion forums
- Social media communities

This manual verification process is time-consuming, inconsistent, dependent on individual experience, and often ineffective against sophisticated scams that successfully imitate legitimate organizations.

---

# 3. Existing Challenges

Current internship verification approaches suffer from several technical and practical limitations.

## 3.1 Fragmented Verification

Users must independently collect evidence from multiple online sources before making a trust decision.

## 3.2 Limited Verification Signals

Many existing systems primarily analyze textual content while ignoring independently verifiable trust signals such as:

- Company registration
- Recruiter identity consistency
- Website reputation
- Domain intelligence
- Contextual behavioural indicators

## 3.3 Static Rule-Based Systems

Traditional rule-based systems rely on manually defined conditions that are difficult to maintain as fraud strategies continuously evolve.

## 3.4 Limited Explainability

Many machine learning models provide classification outputs without offering transparent reasoning that users can easily understand and verify.

## 3.5 Internship-Specific Gap

Most existing research focuses on generic employment fraud detection rather than internship verification, despite internship scams exhibiting behavioural characteristics that differ from traditional job fraud.

---

# 4. Research Gap

Existing internship fraud detection approaches primarily rely on textual classification or isolated verification mechanisms. However, there remains a lack of a unified framework capable of integrating multiple independently verifiable trust signals into a transparent, explainable, and evidence-driven trust assessment specifically designed for internship verification.

Current literature largely evaluates textual information independently, while practical internship verification requires simultaneous analysis of recruiter authenticity, company legitimacy, website intelligence, contextual behavioural indicators, and machine learning-based fraud prediction.

This gap highlights the need for a comprehensive internship-specific verification framework capable of combining heterogeneous trust signals into a single explainable trust score.

---

# 5. Problem Statement

The absence of a unified, explainable, multi-signal internship verification framework forces students and educational institutions to rely on fragmented manual verification processes that are often insufficient for identifying sophisticated internship fraud.

Existing approaches typically analyze textual information in isolation and fail to incorporate independently verifiable evidence such as recruiter authenticity, company legitimacy, domain intelligence, and contextual behavioural indicators into a single transparent trust assessment.

Consequently, users remain vulnerable to fraudulent internship opportunities despite investing significant effort in manual verification.

---

# 6. Project Objective

The primary objective of YEScape 2.0 is to develop a globally applicable AI-assisted internship verification framework that combines machine learning-based textual fraud analysis with independently verifiable trust signals through a supervised trust fusion model.

The framework aims to generate an explainable trust score that enables transparent, evidence-driven decision-making for students, educational institutions, and placement officers.

Although the proposed methodology is designed to be globally applicable, its initial implementation focuses on India by integrating publicly accessible verification sources such as:

- Ministry of Corporate Affairs (MCA)
- Goods and Services Tax (GST)
- WHOIS Domain Intelligence
- Google Safe Browsing API

Future implementations can extend the same methodology using equivalent verification sources from other countries.

---

# 7. Research Scope

YEScape 2.0 focuses on developing an internship-specific verification framework that integrates multiple independent trust signals into a unified explainable decision-making pipeline.

The scope includes:

- Internship offer verification
- Machine learning-based fraud prediction
- Multi-signal trust fusion
- Explainable Artificial Intelligence
- Publicly verifiable evidence sources
- Transparent trust reporting

The scope explicitly excludes:

- Employment contract verification
- Candidate evaluation
- Recruitment automation
- Legal decision-making
- Background verification

---

# 8. Expected Research Contributions

The proposed research is expected to contribute the following:

1. A novel internship-specific multi-signal verification framework.

2. A manually curated internship benchmark dataset designed specifically for evaluating internship fraud detection systems.

3. A supervised trust fusion model that combines heterogeneous trust signals into a unified trust assessment.

4. An explainable AI framework capable of providing transparent evidence supporting every verification decision.

5. A reproducible evaluation framework comparing traditional text-only fraud detection with multi-signal trust fusion for internship verification.

---

# Conclusion

YEScape 2.0 seeks to shift internship verification from fragmented manual investigation toward an evidence-driven, explainable, and reproducible trust assessment framework.

By combining machine learning with independently verifiable trust signals, the proposed framework aims to provide transparent internship legitimacy assessment while reducing the reliance on subjective manual verification.

The long-term vision is to establish a globally adaptable internship verification methodology capable of supporting educational institutions, students, recruiters, and regulatory organizations through trustworthy AI-assisted decision-making.