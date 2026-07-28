# YEScape 2.0

# Master System Architecture

---

# Project Objective

YEScape is an AI-powered Internship Verification System that analyzes internship offers using multiple independent verification signals.

Each signal evaluates one aspect of an internship offer.

All signals are combined inside a centralized Verification Engine.

---

# Overall Workflow

User

↓

Offer Letter (PDF / Text / URL)

↓

Extraction Layer

↓

Verification Layer

↓

Risk Analysis

↓

Final Trust Score

↓

AI Explanation

↓

User Report

---

# Current Architecture

Offer Letter

↓

Signal 1

Offer Parser

↓

Offer Analysis Engine

↓

OfferData

↓

Verification Engine

↓

Signal 2

Domain Verification

↓

Signal 3

Company Verification

↓

Signal 4

Recruiter Verification

↓

Signal 5

Context Analysis

↓

Verification Result

↓

UI Report

---

# Signal Overview

## Signal 1

Offer Analysis

Purpose

Extract structured information from the internship offer.

Current Outputs

- Company
- Recruiter Email
- Website
- Salary
- Extraction Confidence

---

## Signal 2

Domain Verification

Purpose

Verify website legitimacy.

Checks

- WHOIS
- DNS
- HTTPS
- Safe Browsing

Output

Domain Trust Score

---

## Signal 3

Company Verification

Purpose

Verify whether the internship belongs to the real company.

Checks

- Registry
- Official Domain
- Career Portal

Output

Company Trust Score

---

## Signal 4

Recruiter Verification

Purpose

Verify recruiter legitimacy.

Checks

- Email Format
- Domain Reputation
- Company Domain Match
- Free Email Detection

Output

Recruiter Trust Score

---

## Signal 5

Context Analysis

Purpose

Analyze internship content.

Checks

- Scam Keywords
- Urgency
- Advance Fee
- Salary
- Contact Details
- Grammar

Output

Context Trust Score

---

# Verification Engine

The Verification Engine coordinates all signals.

Responsibilities

- Receive OfferData
- Execute every signal
- Store individual results
- Return VerificationResult

The engine never contains business logic.

Each signal is completely independent.

---

# Signal Factory

Purpose

Create all signal objects.

Benefits

- Cleaner architecture
- Easier maintenance
- Supports future dependency injection

---

# Current Folder Structure

core/

config/

schemas/

signals/

utils/

docs/

tests/

models/

trained_models/

vectorizers/

---

# Current Project Status

Completed

✓ Signal 1

✓ Signal 2

✓ Signal 3

✓ Signal 4

✓ Signal 5

✓ Verification Engine

✓ Signal Factory

Pending

Signal 6

Signal 7

Signal 8

Signal 9

Signal 10

Final Risk Fusion

UI

Browser Extension

Deployment

---

# Future Architecture

Offer Letter

↓

Signal 1

↓

Signals 2–10

↓

Score Fusion Engine

↓

Final Trust Score

↓

Risk Level

↓

Explanation Engine

↓

Report Generator

↓

Chrome Extension

↓

Web Dashboard

---

# Design Principles

YEScape follows

- Modular Design
- Single Responsibility Principle
- Separation of Concerns
- Independent Signals
- Central Verification Engine
- Reusable Components

---

# Version

YEScape 2.0

Current Phase

Phase 4.2 Completed

Architecture Version

1.0