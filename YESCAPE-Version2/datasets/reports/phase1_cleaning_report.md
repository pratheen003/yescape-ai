# Phase 1.3 — Data Cleaning Report

## Version

Version: 1.0

---

# Objective

Prepare the EMSCAD dataset for machine learning by removing redundant information, handling missing values, and standardizing feature formats.

---

# Cleaning Steps Performed

## Duplicate Removal

Removed duplicate job postings.

Reason:

Duplicate samples can bias machine learning models and reduce generalization.

---

## Feature Removal

Removed:

- department
- salary_range
- in_balanced_dataset

Reason:

These features were excluded during Feature Selection because they contain excessive missing values or no predictive value.

---

## Missing Value Treatment

### Text Features

Missing values replaced with empty strings.

Affected columns:

- company_profile
- requirements
- benefits

---

### Metadata Features

Missing values replaced with:

Unknown

Affected columns:

- location
- employment_type
- required_experience
- required_education
- industry
- function

---

## Binary Standardization

Converted

- t → 1
- f → 0

Affected columns:

- telecommuting
- has_company_logo
- has_questions
- fraudulent

---

## Final Dataset Summary

| Property | Value |
|-----------|------:|
| Total Samples | 17,645 |
| Total Features | 15 |
| Missing Values | 0 |
| Duplicate Records | Removed |
| Binary Features | 4 |
| Text Features | 5 |
| Metadata Features | 6 |

The cleaned dataset is fully standardized and ready for feature engineering.

---

# Output

Generated Dataset

processed_dataset_v1.csv

---

# Status

Phase 1.3 Completed successfully.

The dataset is now standardized and ready for feature engineering and TF-IDF vectorization in Phase 2.