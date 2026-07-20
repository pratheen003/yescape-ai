# YEScape 2.0 Architecture

## Version

Version: 1.0

## Last Updated

20 July 2026

## Status

Draft

---


Diagram 1
High Level Methodology

This explains the complete workflow.



                     USER

                       │

        Internship URL / PDF / Text

                       │

                       ▼

               Input Processing

                       │

                       ▼

             Feature Extraction Layer

                       │

                       ▼

         Five Independent Trust Signals

                       │

                       ▼

      Logistic Regression Fusion Model

                       │

                       ▼

                  YESScore

                       │

                       ▼

             SHAP Explainability

                       │

                       ▼

             Final AI Trust Report







Diagram 2
Complete Internal Architecture

This explains how the AI internally works.



                           USER
                             │
                             ▼
                 Internship Offer Input
                             │
──────────────────────────────────────────────────────────────
                  INPUT PROCESSING LAYER
──────────────────────────────────────────────────────────────
                             │
                             ▼
                  FEATURE EXTRACTION LAYER
──────────────────────────────────────────────────────────────
      Company
      Recruiter Email
      Website URL
      Internship Description
      Contextual Features
──────────────────────────────────────────────────────────────
                             │
                             ▼
──────────────────────────────────────────────────────────────
            FIVE TRUST VERIFICATION MODULES
──────────────────────────────────────────────────────────────
│
├── Signal 1
│   ML Scam Probability
│
├── Signal 2
│   Domain Intelligence
│
├── Signal 3
│   Recruiter Identity Verification
│
├── Signal 4
│   Company Verification
│
└── Signal 5
    Context Intelligence
──────────────────────────────────────────────────────────────
                             │
                             ▼
──────────────────────────────────────────────────────────────
      Logistic Regression Meta Fusion Model
──────────────────────────────────────────────────────────────
                             │
                             ▼
                    YESScore (0-100)
                             │
                             ▼
──────────────────────────────────────────────────────────────
             SHAP Explainability Layer
──────────────────────────────────────────────────────────────
                             │
                             ▼
                 AI Trust Report Generator
                             │
                             ▼
                Final Internship Verdict