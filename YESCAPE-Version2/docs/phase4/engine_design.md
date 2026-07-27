# Phase 4 – Verification Engine

## Overview

The Verification Engine is the central controller of YEScape Version 2.

Instead of manually invoking individual verification signals, the engine receives a single verification request and orchestrates the execution of all verification modules.

---

## Objectives

- Centralize verification logic.
- Standardize inputs.
- Standardize outputs.
- Improve maintainability.
- Simplify future API and UI integration.

---

## Phase Breakdown

- Phase 4.1 – Verification Engine
- Phase 4.2 – Score Fusion
- Phase 4.3 – Explanation Generator
- Phase 4.4 – Report Generator
- Phase 4.5 – Pipeline Testing


---

## Verification Flow

Each verification module returns a standardized SignalResult object.

SignalResult contains:

- Signal Name
- Score
- Success Status
- Human-readable Reason
- Detailed Metadata

This common structure allows the Verification Engine to combine all verification modules without custom parsing logic.

---

## Core Schemas

### VerificationRequest

Stores all inputs required for one verification.

### SignalResult

Represents the standardized output of one verification signal.

### VerificationResult

Represents the complete verification outcome after all signals have executed.

---

## Verification Engine

The Verification Engine is the single entry point for the YEScape verification pipeline.

Instead of invoking verification modules individually, the engine orchestrates all signals in a predefined sequence.

Current execution order:

1. Offer Letter Verification
2. Domain Verification
3. Company Verification
4. Recruiter Verification
5. Context Analysis

Each signal produces a SignalResult object.

All SignalResult objects are collected into a VerificationResult object for downstream score fusion and report generation.

---

## Signal Integration Progress

### Completed

- Signal 5 – Context Analysis

The Verification Engine now invokes the Context Analysis module directly. The returned context verification dictionary is wrapped into a standardized SignalResult object and stored inside the VerificationResult.

This establishes the integration pattern that will be reused for Signals 1–4.

### Signal 2 – Domain Verification

The Verification Engine now executes the Domain Verification module.

The engine forwards the internship website from the VerificationRequest into the DomainTrustScore module.

The returned domain verification dictionary is wrapped into a standardized SignalResult object.

The engine now performs:

VerificationRequest
      ↓
Domain Verification
      ↓
SignalResult

### Signal 3 – Company Verification

The Verification Engine now executes the Company Verification module.

The company name and internship website are passed to the Company Trust module.

The module verifies:

- Registry availability
- Official company domain
- Career portal match

The resulting Company Trust Score is wrapped inside a SignalResult and stored in the VerificationResult.

### Signal 4 – Recruiter Verification

The Verification Engine now executes the Recruiter Verification module.

Inputs:

- Company name
- Recruiter email

The Recruiter module internally combines:

- Domain Trust
- Company Domain Match
- Free Email Detection

The final Recruiter Trust Score is wrapped into a SignalResult and stored inside the VerificationResult.

## Phase 4.1 Completion

The Verification Engine now orchestrates the four completed verification modules:

- Signal 2 – Domain Verification
- Signal 3 – Company Verification
- Signal 4 – Recruiter Verification
- Signal 5 – Context Analysis

Each module executes independently and returns a standardized `SignalResult`.

Signal 1 (Offer Letter Analysis) is intentionally deferred to Phase 4.2 because it requires OCR, PDF parsing, and metadata extraction before it can be integrated cleanly into the engine.