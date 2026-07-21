# TF-IDF Pipeline

## Version

Version: 1.0

---

# Objective

Convert cleaned internship/job posting text into numerical feature vectors.

---

# Pipeline

Raw Text

↓

Cleaning

↓

Tokenization

↓

Stopword Removal

↓

Lemmatization

↓

clean_text

↓

TF-IDF

↓

Sparse Feature Matrix

↓

XGBoost

---

# TF-IDF Configuration

Input

clean_text

Stop Words

English

Maximum Features

To be selected experimentally

N-grams

Unigram (initial baseline)

Future Work

Bigram evaluation

---

# Outputs

Vocabulary

TF-IDF Matrix

Saved Vectorizer

Feature Statistics

---

# Deliverables

tfidf_vectorizer.pkl

feature_matrix.npz

feature_names.txt