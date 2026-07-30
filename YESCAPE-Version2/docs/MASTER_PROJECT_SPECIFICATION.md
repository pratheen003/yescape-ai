# YESCAPE 2.0

# MASTER PROJECT SPECIFICATION

---

## Document Information

| Field | Value |
|-------|-------|
| Project Name | YEScape |
| Version | 2.0 |
| Current Development Phase | Phase 5 |
| Document Version | 1.0 |
| Document Type | Master Project Specification |
| Purpose | Complete Software Architecture & Development Guide |

---

# Table of Contents

- Chapter 1 – Project Overview
- Chapter 2 – Project History
- Chapter 3 – Project Objectives
- Chapter 4 – Current Folder Architecture
- Chapter 5 – Backend Architecture
- Chapter 6 – Frontend Architecture
- Chapter 7 – Completed Development
- Chapter 8 – Current Project Status
- Chapter 9 – Version Migration Strategy
- Chapter 10 – AI Development Rules
- Chapter 11 – Development Tasks
- Chapter 12 – Acceptance Criteria

---

# Chapter 1 — Project Overview

---

## 1.1 Project Name

**YEScape**

> AI Powered Internship Verification Platform

---

## 1.2 Project Vision

YEScape is an Artificial Intelligence powered internship verification platform designed to help students identify fraudulent internship offers before they become victims of online internship scams.

The platform performs multi-layer verification by analysing:

- Offer Letter
- Company
- Recruiter
- Website
- Context
- Trust Signals

The results are combined using an intelligent score fusion system to produce a final trust score together with an explanation that is easy for students to understand.

---

## 1.3 Problem Statement

Every year thousands of students receive internship offers through:

- Email
- WhatsApp
- Telegram
- LinkedIn
- Social Media
- Fake Career Websites

Many of these offers are fraudulent.

Students often lose money by:

- Paying fake registration fees
- Sharing personal documents
- Accepting offers from non-existent companies
- Downloading malicious attachments

Currently there is no single platform capable of automatically verifying all these aspects together.

YEScape solves this problem by performing automated multi-level verification and producing a trustworthy confidence score.

---

## 1.4 Primary Objectives

The primary objectives of YEScape are:

- Detect fake internship offers.
- Verify recruiter authenticity.
- Verify company legitimacy.
- Verify internship websites.
- Detect scam language.
- Produce an explainable trust score.
- Help students make safe decisions.
- Reduce internship fraud.

---

## 1.5 Target Users

### Primary Users

- Engineering Students
- College Students
- Fresh Graduates
- Internship Applicants

---

### Secondary Users

- Placement Officers
- Universities
- Career Guidance Centers
- Training Institutions
- Internship Coordinators

---

## 1.6 Core Features

YEScape currently performs verification using five independent signals.

| Signal | Purpose |
|---------|----------|
| Signal 1 | Offer Letter Analysis |
| Signal 2 | Website / Domain Verification |
| Signal 3 | Company Verification |
| Signal 4 | Recruiter Verification |
| Signal 5 | Context Analysis |

The results of all five signals are combined into a single intelligent trust score.

---

## 1.7 Development Philosophy

YEScape follows the following engineering principles.

### Reliability

Every verification should produce deterministic and repeatable results whenever possible.

---

### Transparency

Every trust score must be explainable.

No hidden "black-box" decisions should exist.

---

### Modularity

Every verification signal must function independently.

Signals should be replaceable without affecting the remaining architecture.

---

### Maintainability

The project should remain:

- Modular
- Documented
- Easy to extend
- Easy to debug

---

### Production Readiness

Every completed phase must include:

- Documentation
- Testing
- Git milestone
- Stable implementation

before progressing to the next phase.

---

## 1.8 Current Project Status

| Component | Status |
|-----------|--------|
| Backend | ✅ Completed |
| Verification Engine | ✅ Completed |
| Signal Engine | ✅ Completed |
| Score Fusion | ✅ Completed |
| Testing | ✅ Completed |
| Documentation | ✅ Completed |
| Frontend | ⚠ Version 1 Available |
| Deployment | ✅ Already Live |
| Current Goal | Integrate Version 2 Backend with Version 1 Frontend |

---

## 1.9 Current Live Application

Version 1 of YEScape has already been deployed successfully using Streamlit.

The deployed application contains:

- Landing Page
- Verification Page
- Trust Score Gauge
- Verification Report
- Research Page
- Downloadable PDF Report

The purpose of Version 2 is **NOT** to redesign these pages.

Instead, the objective is to integrate the newly developed backend architecture into the existing Version 1 interface.

---

## 1.10 End of Chapter

This chapter introduces the YEScape project, explains its objectives, identifies the target users, summarizes the completed work, and establishes the overall purpose of the system.

The following chapter describes the complete development history of YEScape from Version 1 through Version 2.


# Chapter 2 — Project History

---

## 2.1 Introduction

YEScape has evolved through multiple development stages.

The project did not start with the current architecture.

Instead, it has gradually matured from a simple proof-of-concept into a modular AI-powered internship verification platform.

Understanding this development history is important because Version 2 was intentionally designed to solve the limitations discovered during Version 1.

---

# 2.2 Version 1

## Initial Development

YEScape Version 1 was developed as the first working prototype of the internship verification platform.

The primary objective was to demonstrate the feasibility of automatically verifying internship offers using Artificial Intelligence and rule-based analysis.

Version 1 successfully proved that the concept worked.

---

## Version 1 Features

The first version included the following major features.

- Landing Page
- Internship Verification Page
- Trust Score Gauge
- Verification Report
- Research Page
- Downloadable PDF Report
- OCR Support
- Basic Rule Engine
- Streamlit Deployment

---

## Deployment

Version 1 was successfully deployed using Streamlit Cloud.

The deployed application is the first public working version of YEScape.

The deployment proved that the platform could successfully perform internship verification through an accessible web interface.

---

## Limitations of Version 1

Although Version 1 functioned successfully, several architectural limitations were identified during development.

### Monolithic Design

Most verification logic was directly connected to the user interface.

This made maintenance difficult.

---

### Tight Coupling

Business logic and UI components depended heavily on each other.

Changing one module frequently required modifying several unrelated files.

---

### Limited Modularity

Individual verification components could not easily be tested independently.

---

### Difficult Debugging

As development progressed, frequent AI-generated modifications caused working code to become mixed with experimental implementations.

Tracking stable versions became increasingly difficult.

---

### Limited Scalability

Adding new verification signals required modifying existing files rather than extending independent modules.

---

# 2.3 Motivation for Version 2

The limitations discovered in Version 1 motivated a complete backend redesign.

Instead of continuing to extend the existing implementation, the backend architecture was redesigned from the ground up.

The objective was not to redesign the user interface.

The objective was to build a professional backend architecture that could support future expansion while remaining easy to maintain.

---

# 2.4 Version 2 Goals

Version 2 was designed with the following objectives.

- Completely modular architecture
- Independent verification signals
- Central verification engine
- Signal factory
- Unified score fusion
- Structured schemas
- Complete documentation
- Automated testing
- Easier debugging
- Production-ready architecture

---

# 2.5 Version 2 Development

Version 2 development was divided into multiple structured phases.

Each phase focused on a single architectural component.

Every completed phase included implementation, testing, and documentation before moving to the next phase.

This ensured that each module remained stable before introducing additional complexity.

---

# 2.6 Backend Completed in Version 2

The following components have been completed.

## Core Engine

- Verification Engine
- Signal Factory
- Score Fusion
- Pipeline Execution

---

## Verification Signals

- Signal 1 — Offer Letter Analysis
- Signal 2 — Domain Verification
- Signal 3 — Company Verification
- Signal 4 — Recruiter Verification
- Signal 5 — Context Analysis

---

## Data Models

- Verification Request Schema
- Verification Result Schema
- Signal Result Schema
- Offer Data Schema

---

## Testing

Dedicated testing has been completed for:

- Individual Signals
- Verification Engine
- Offer Parser
- Pipeline Execution
- Score Fusion
- Integration Tests

---

## Documentation

Every completed module includes technical documentation.

Documentation is stored inside the `docs/` directory and follows a phase-wise organization.

---

# 2.7 Current Project State

At the time this document was written, the backend has reached production-level stability.

The following components are considered complete.

| Component | Status |
|-----------|--------|
| Signal Engine | ✅ Complete |
| Verification Engine | ✅ Complete |
| Offer Parser | ✅ Complete |
| Score Fusion | ✅ Complete |
| Schemas | ✅ Complete |
| Tests | ✅ Complete |
| Documentation | ✅ Complete |

---

# 2.8 Remaining Work

The remaining work is focused entirely on integration.

The existing Version 1 frontend will be connected to the Version 2 backend.

No backend redesign is planned.

The frontend will continue to use the existing Streamlit interface while replacing the old backend logic with the new modular verification architecture.

---

# 2.9 Important Development Principle

Version 2 is **NOT** a new application.

Version 2 is an architectural upgrade.

The existing user interface already performs its intended purpose and has been successfully deployed.

Therefore:

- The frontend should be preserved.
- The backend should be integrated.
- Existing user experience should remain familiar.
- Backend quality should be significantly improved.

---

# 2.10 End of Chapter

This chapter documents the evolution of YEScape from Version 1 to Version 2.

It explains why the backend was redesigned, what improvements were introduced, and establishes that the remaining work is focused on integration rather than redevelopment.

The following chapter explains the complete folder architecture of the project.

# Chapter 3 — Project Folder Architecture

---

## 3.1 Introduction

YEScape follows a modular project architecture.

The repository is divided into two major systems.

1. Version 1 User Interface
2. Version 2 Backend Architecture

These systems are intentionally separated to allow independent development while preserving the deployed application.

The objective of future development is to integrate these two systems rather than redesign either one.

---

# 3.2 High Level Repository Structure

```text
YESCAPE-AI/

├── Version 1 (Current Streamlit Application)
│
├── YESCAPE-Version2/
│
└── Supporting Project Files
```

---

# 3.3 Version 1

The root project contains the existing Streamlit application.

This application is already deployed and contains the complete user interface.

Current deployment includes:

- Landing Page
- Verification Page
- Trust Score Gauge
- Verification Report
- Research Page
- Downloadable PDF
- Streamlit Navigation

Version 1 is considered the official frontend.

Future development must preserve these user interface components.

---

# 3.4 Version 2

The directory

```text
YESCAPE-Version2/
```

contains the complete backend architecture.

Unlike Version 1, this folder contains almost no user interface logic.

Instead it contains the verification engine and supporting modules.

---

# 3.5 Major Folder Responsibilities

---

## core/

### Purpose

Contains the central execution engine of YEScape.

Responsible for:

- Verification Engine
- Signal Factory
- Score Fusion
- Logging
- Pipeline
- Future API Layer

---

### Responsibility

This folder coordinates all verification signals.

It never performs verification directly.

Instead it delegates work to individual signal modules.

---

### Status

✅ Production Ready

---

### Modification Policy

READ ONLY

Do not redesign architecture.

Do not rename files.

Only extend when absolutely necessary.

---

## signals/

### Purpose

Contains every independent verification signal.

Each signal performs one specific verification task.

---

### Current Signals

Signal 1

Offer Letter Analysis

---

Signal 2

Domain Verification

---

Signal 3

Company Verification

---

Signal 4

Recruiter Verification

---

Signal 5

Context Analysis

---

### Design Principle

Every signal must remain independent.

Signals should never directly depend on another signal.

Communication happens only through the Verification Engine.

---

### Status

✅ Production Ready

---

### Modification Policy

READ ONLY

Do not change scoring logic.

Do not merge signals.

Do not rename folders.

---

## schemas/

### Purpose

Contains all project data models.

Examples include

- VerificationRequest
- VerificationResult
- SignalResult
- OfferData

---

### Design Principle

Schemas provide standardized communication between modules.

No business logic should exist inside schemas.

---

### Status

✅ Stable

---

### Modification Policy

READ ONLY

---

## tests/

### Purpose

Contains automated testing modules.

Tests verify

- Individual Signals
- Verification Engine
- Offer Parser
- Pipeline
- Integration

---

### Design Principle

Every completed backend module should have a corresponding test.

---

### Status

✅ Stable

---

### Modification Policy

READ ONLY

Tests may only be extended.

Existing tests should never be removed.

---

## docs/

### Purpose

Contains technical documentation for every development phase.

Documentation includes

- Phase Notes
- Architecture
- Design Decisions
- Specifications

---

### Design Principle

Every completed feature must have documentation.

---

### Status

Growing continuously

---

### Modification Policy

Append only.

Never delete previous documentation.

---

## assets/

### Purpose

Stores project resources.

Examples include

- Images
- Logos
- Icons
- UI Resources

---

### Modification Policy

Editable

---

## config/

### Purpose

Stores project configuration.

Examples

- Environment Variables
- API Keys
- Constants

---

### Modification Policy

Editable

---

## models/

### Purpose

Reserved for future Machine Learning models.

Examples

- Classification Models
- Embeddings
- Serialized Models

---

### Current Status

Reserved

---

## data/

### Purpose

Stores datasets used by YEScape.

Examples

- Company Registry
- Scam Keywords
- Safe Domain Lists

---

### Modification Policy

Editable

Data may be updated.

Structure should remain unchanged.

---

# 3.6 Folder Dependency Diagram

```text
                    Streamlit UI

                          │

                          ▼

              Verification Engine

                          │

         ┌─────────────────────────────────┐

         ▼               ▼                ▼

     Signals         Score Fusion      Schemas

         │

         ▼

      Datasets

```

---

# 3.7 Read-Only Components

The following folders are considered production-ready.

They must remain unchanged unless explicitly approved.

| Folder | Status |
|----------|---------|
| core/ | READ ONLY |
| signals/ | READ ONLY |
| schemas/ | READ ONLY |
| tests/ | READ ONLY |
| docs/ | READ ONLY |

---

# 3.8 Editable Components

The following components may be modified during future development.

| Folder | Purpose |
|----------|----------|
| app.py | Main Streamlit Entry Point |
| pages/ | UI Pages |
| assets/ | UI Resources |
| config/ | Configuration |
| data/ | Registry Updates |
| reports/ | PDF Rendering |
| frontend components | User Interface |

---

# 3.9 Integration Boundary

The backend and frontend communicate only through the Verification Engine.

The UI should never directly access individual signals.

Correct Flow

```text
UI

↓

Verification Engine

↓

Signals

↓

Fusion

↓

Verification Result

↓

UI
```

Incorrect Flow

```text
UI

↓

Signal 2

↓

Signal 5

↓

Signal 3
```

Direct communication between UI and individual signals is prohibited.

---

# 3.10 Development Principle

The folder architecture has been intentionally designed to maximize

- Maintainability
- Modularity
- Testability
- Scalability

Future development should preserve this structure.

Existing architecture should be extended rather than redesigned.

---

# 3.11 End of Chapter

This chapter defines the responsibilities of every major folder within the YEScape repository.

Future contributors and AI development assistants must follow these architectural boundaries throughout development.

The next chapter describes the complete backend architecture and execution flow.

# Chapter 4 — Backend Architecture

---

# 4.1 Introduction

The YEScape Version 2 backend is designed as a modular verification system.

Unlike Version 1, where verification logic was tightly coupled with the user interface, Version 2 separates every responsibility into independent modules.

Every verification process follows a fixed execution pipeline.

The backend is responsible for

- Parsing internship offers
- Executing independent verification signals
- Combining signal scores
- Producing a final trust score
- Returning a structured verification result

The frontend never performs verification.

The frontend only displays the results returned by the backend.

---

# 4.2 High-Level Architecture

```text
                    User Interface
                         │
                         ▼
              Verification Request
                         │
                         ▼
              Verification Engine
                         │
         ┌───────────────┼───────────────┐
         ▼               ▼               ▼
   Signal Factory     Score Fusion    Schemas
         │
         ▼
 ┌─────────────────────────────────────────┐
 │               Signals                   │
 │                                         │
 │ Offer Analysis                          │
 │ Domain Verification                     │
 │ Company Verification                    │
 │ Recruiter Verification                  │
 │ Context Analysis                        │
 └─────────────────────────────────────────┘
                         │
                         ▼
              Verification Result
                         │
                         ▼
                   Streamlit UI
```

---

# 4.3 Backend Philosophy

The backend follows four design principles.

---

## Modularity

Each verification signal performs exactly one task.

No signal is responsible for another signal.

---

## Separation of Concerns

Different responsibilities are handled by different modules.

Example

Offer Parsing

↓

Domain Verification

↓

Company Verification

↓

Recruiter Verification

↓

Context Analysis

↓

Score Fusion

---

## Extensibility

New signals can be added without modifying existing signals.

Only the Signal Factory needs to register new modules.

---

## Testability

Every major module has its own independent test.

Modules can be verified individually without executing the complete application.

---

# 4.4 Verification Flow

The verification process follows the exact sequence shown below.

```text
User submits internship offer

↓

Offer Parser

↓

Verification Engine

↓

Signal Factory

↓

Offer Analysis

↓

Domain Verification

↓

Company Verification

↓

Recruiter Verification

↓

Context Analysis

↓

Score Fusion

↓

Verification Result

↓

Frontend Display
```

No module is allowed to skip this execution order.

---

# 4.5 Verification Engine

Location

```text
core/verification_engine.py
```

---

## Responsibility

The Verification Engine controls the entire verification workflow.

It is the central controller of the backend.

The engine

- receives requests
- executes signals
- collects scores
- performs score fusion
- generates the final result

---

## Responsibilities

✓ Execute signals

✓ Handle failures safely

✓ Collect results

✓ Perform score fusion

✓ Build VerificationResult

---

The Verification Engine does not perform verification itself.

It delegates work to individual signal modules.

---

# 4.6 Signal Factory

Location

```text
core/signal_factory.py
```

---

## Purpose

Creates every verification signal.

Instead of directly creating objects inside the Verification Engine,

the engine asks the Signal Factory to build them.

Example

```text
Verification Engine

↓

Signal Factory

↓

Offer

↓

Domain

↓

Company

↓

Recruiter

↓

Context
```

---

Advantages

- Centralized object creation
- Easier maintenance
- Future dependency injection support

---

# 4.7 Verification Signals

Every signal produces one independent trust score.

---

## Signal 1

Offer Letter Analysis

Responsibilities

- Parse offer
- Extract entities
- Calculate offer confidence

Output

Offer Confidence Score

---

## Signal 2

Domain Verification

Responsibilities

- WHOIS
- DNS
- HTTPS
- Safe Browsing

Output

Domain Trust Score

---

## Signal 3

Company Verification

Responsibilities

- Company Registry
- Official Domain
- Career Portal

Output

Company Trust Score

---

## Signal 4

Recruiter Verification

Responsibilities

- Email Validation
- Company Email Match
- Free Email Detection

Output

Recruiter Trust Score

---

## Signal 5

Context Analysis

Responsibilities

- Scam Keywords
- Grammar
- Urgency
- Advance Fee
- Contact Quality
- Salary Validation

Output

Context Trust Score

---

# 4.8 Score Fusion

Location

```text
core/fusion/score_fusion.py
```

---

Purpose

Combine all signal scores into one final trust score.

Inputs

- Offer Confidence
- Domain Score
- Company Score
- Recruiter Score
- Context Score

Outputs

- Final Trust Score
- Risk Level
- Confidence
- Explanation

---

Example

```text
Offer        100

Domain        80

Company      100

Recruiter    100

Context       94

↓

Weighted Fusion

↓

94.8

↓

SAFE
```

---

# 4.9 Verification Result

Location

```text
schemas/verification_result.py
```

---

Purpose

Stores the complete verification output.

Contains

- Final Score
- Risk Level
- Confidence
- Reasons
- Signal Results

This object is returned directly to the frontend.

---

# 4.10 Signal Result

Location

```text
schemas/signal_result.py
```

---

Each verification signal returns

- Signal Name
- Score
- Success Status
- Reason
- Details

Example

```text
Signal

↓

Score

↓

Reason

↓

Details
```

---

# 4.11 Safe Execution

The Verification Engine never allows one failed signal to crash the entire verification process.

Every signal executes using

```python
safe_execute()
```

Benefits

- Exception Handling
- Graceful Failure
- Better Debugging
- Reliable Pipeline

---

# 4.12 Current Backend Status

Completed Components

| Module | Status |
|----------|--------|
| Offer Analysis | ✅ Complete |
| Domain Verification | ✅ Complete |
| Company Verification | ✅ Complete |
| Recruiter Verification | ✅ Complete |
| Context Analysis | ✅ Complete |
| Verification Engine | ✅ Complete |
| Signal Factory | ✅ Complete |
| Score Fusion | ✅ Complete |
| Schemas | ✅ Complete |
| Pipeline | ✅ Complete |
| Tests | ✅ Complete |

---

# 4.13 Backend Constraints

Future development must follow these rules.

✓ Do not bypass Verification Engine

✓ Do not call signals directly from UI

✓ Do not merge signals

✓ Do not duplicate score calculations

✓ Add future verification modules through Signal Factory

✓ Preserve modular architecture

---

# 4.14 End of Chapter

This chapter documents the complete backend architecture of YEScape Version 2.

Every verification request follows this architecture from input parsing to final trust score generation.

The next chapter describes the detailed architecture and responsibilities of each verification signal individually.

# Chapter 5 — Verification Signal Specifications

---

# 5.1 Introduction

YEScape evaluates every internship offer using five independent verification signals.

Each signal is responsible for evaluating one aspect of the internship offer.

The signals operate independently and never directly communicate with one another.

The Verification Engine executes them sequentially and passes their results to the Score Fusion Engine.

This modular design allows individual signals to be upgraded without affecting the rest of the system.

---

# 5.2 Overall Verification Architecture

```text
Offer Letter

↓

Signal 1
Offer Analysis

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

Score Fusion

↓

Final Trust Score
```

---

# 5.3 Signal Weight Distribution

Every signal contributes equally to the final trust score.

| Signal | Weight |
|----------|-------:|
| Offer Letter Analysis | 20% |
| Domain Verification | 20% |
| Company Verification | 20% |
| Recruiter Verification | 20% |
| Context Analysis | 20% |

Total Weight

```text
100%
```

Future versions may adjust these weights based on model evaluation and validation experiments.

---

# 5.4 Signal 1 — Offer Letter Analysis

---

## Objective

Extract structured information from an internship offer.

This signal converts an unstructured internship offer into machine-readable information.

---

## Folder

```text
signals/

signal1_offer/
```

---

## Primary Files

```text
offer_parser.py

offer_engine.py

offer_score.py

offer_schema.py
```

---

## Input

Offer Letter Text

---

## Output

OfferData Object

Containing

- Company Name
- Website
- Recruiter Email
- Salary
- Contact Information
- Parsed Metadata

---

## Internal Workflow

```text
Offer Text

↓

Parser

↓

Entity Extraction

↓

Validation

↓

Confidence Score
```

---

## Confidence Calculation

Confidence is calculated using four extracted entities.

| Entity | Contribution |
|----------|-------------:|
| Company Name | 25% |
| Website | 25% |
| Recruiter Email | 25% |
| Salary | 25% |

---

Maximum Confidence

```text
100
```

---

Current Output Example

```text
Company

Google

Website

https://careers.google.com

Recruiter

hr@google.com

Salary

25000

Confidence

100
```

---

## Signal Contribution

20% of Final Trust Score

---

# 5.5 Signal 2 — Domain Verification

---

## Objective

Verify whether the internship website belongs to a trustworthy domain.

---

## Folder

```text
signals/

signal2_domain/
```

---

## Primary Files

```text
domain_score.py

whois_checker.py

dns_checker.py

https_checker.py

safe_browsing.py
```

---

## Input

Website URL

---

## Output

Domain Trust Score

---

## Internal Workflow

```text
Website

↓

WHOIS

↓

DNS

↓

HTTPS

↓

Safe Browsing

↓

Domain Trust Score
```

---

## Internal Score Distribution

| Component | Weight |
|------------|-------:|
| WHOIS | 30% |
| DNS | 20% |
| HTTPS | 20% |
| Safe Browsing | 30% |

---

Maximum Domain Score

```text
100
```

---

Current Output Example

```text
WHOIS

100

DNS

80

HTTPS

100

Safe Browsing

100

↓

Domain Trust

94
```

---

## Signal Contribution

20% of Final Trust Score

---

# 5.6 Signal 3 — Company Verification

---

## Objective

Verify that the internship belongs to a genuine registered company.

---

## Folder

```text
signals/

signal3_company/
```

---

## Primary Files

```text
company_score.py

registry_loader.py

domain_match.py

career_match.py
```

---

## Input

Company Name

Website

---

## Output

Company Trust Score

---

## Internal Workflow

```text
Company

↓

Registry Check

↓

Official Domain Match

↓

Career Portal Match

↓

Company Trust Score
```

---

## Internal Score Distribution

| Component | Score |
|------------|------:|
| Registry Verification | 20 |
| Official Domain Match | 40 |
| Career Portal Match | 40 |

Maximum Score

```text
100
```

---

## Current Output Example

```text
Registry

20

Official Domain

40

Career Portal

40

↓

Company Score

100
```

---

## Signal Contribution

20% of Final Trust Score

---

# 5.7 Signal 4 — Recruiter Verification

---

## Objective

Determine whether the recruiter email belongs to the verified company.

---

## Folder

```text
signals/

signal4_recruiter/
```

---

## Primary Files

```text
recruiter_score.py

email_parser.py

email_domain.py

company_email_match.py

free_email_checker.py
```

---

## Input

Company

Recruiter Email

---

## Output

Recruiter Trust Score

---

## Internal Workflow

```text
Recruiter Email

↓

Email Parser

↓

Domain Verification

↓

Company Match

↓

Free Email Detection

↓

Recruiter Trust Score
```

---

## Internal Score Distribution

| Component | Weight |
|------------|-------:|
| Domain Trust | 35% |
| Company Match | 35% |
| Free Email Detection | 20% |
| Email Format | 10% |

Maximum Score

```text
100
```

---

Current Output Example

```text
Domain

100

Company Match

100

Free Email

100

Format

100

↓

Recruiter Score

100
```

---

## Signal Contribution

20% of Final Trust Score

---

# 5.8 Signal 5 — Context Analysis

---

## Objective

Analyze the content of the internship offer for suspicious patterns.

---

## Folder

```text
signals/

signal5_context/
```

---

## Primary Files

```text
context_score.py

grammar_checker.py

salary_checker.py

contact_checker.py

scam_keywords.py

urgency_checker.py

advance_fee_checker.py
```

---

## Input

Offer Letter Text

---

## Output

Context Trust Score

---

## Internal Workflow

```text
Offer Text

↓

Scam Keywords

↓

Urgency

↓

Advance Fee

↓

Salary

↓

Contact

↓

Grammar

↓

Context Trust Score
```

---

## Internal Score Distribution

| Component | Weight |
|------------|-------:|
| Scam Keywords | 20% |
| Urgency | 15% |
| Advance Fee | 20% |
| Salary | 15% |
| Contact Information | 15% |
| Grammar | 15% |

Maximum Score

```text
100
```

---

Current Output Example

```text
Scam

100

Urgency

100

Advance Fee

100

Salary

90

Contact

70

Grammar

100

↓

Context Score

94
```

---

## Signal Contribution

20% of Final Trust Score

---

# 5.9 Signal Independence

Every signal operates independently.

No signal directly communicates with another signal.

Communication occurs only through the Verification Engine.

```text
Correct

Verification Engine

↓

Signal

↓

Result

↓

Verification Engine
```

```text
Incorrect

Signal

↓

Signal

↓

Signal
```

---

# 5.10 Future Signal Expansion

The current architecture supports adding additional verification signals.

Examples include

- Internship Duration Verification
- LinkedIn Verification
- Government Company Registry Verification
- AI Semantic Analysis
- Offer Authenticity Prediction Model
- Chrome Extension Signals

These future signals can be added through the Signal Factory without modifying the existing verification engine.

---

# 5.11 End of Chapter

This chapter defines the technical specifications of every verification signal currently implemented in YEScape Version 2.

These signal specifications form the foundation of the verification engine and are combined by the Score Fusion Engine to generate the final internship trust score.

# Chapter 6 — Score Fusion Engine

---

# 6.1 Introduction

The Score Fusion Engine is responsible for converting the outputs of all verification signals into a single trust score.

Instead of making a decision based on one verification signal, YEScape combines multiple independent trust indicators to produce a balanced final assessment.

The Score Fusion Engine is the final decision-making component of the backend.

---

# 6.2 Purpose

The Score Fusion Engine performs the following tasks.

- Combine all signal scores
- Calculate the final trust score
- Determine the internship risk level
- Generate confidence score
- Produce explanation messages
- Return the final verdict

---

# 6.3 Location

```text
core/

fusion/

score_fusion.py
```

---

# 6.4 Inputs

The fusion engine receives five scores.

| Signal | Input |
|---------|------:|
| Offer Letter Analysis | Offer Confidence |
| Domain Verification | Domain Trust Score |
| Company Verification | Company Trust Score |
| Recruiter Verification | Recruiter Trust Score |
| Context Analysis | Context Trust Score |

---

# 6.5 Equal Weight Architecture

Version 2 uses an equal-weight verification model.

Each signal contributes equally.

| Signal | Weight |
|---------|-------:|
| Offer Analysis | 20% |
| Domain Verification | 20% |
| Company Verification | 20% |
| Recruiter Verification | 20% |
| Context Analysis | 20% |

Total

```text
100%
```

---

# 6.6 Final Score Formula

The final trust score is calculated as

```text
Final Score

=

(

Offer

+

Domain

+

Company

+

Recruiter

+

Context

)

÷

5
```

Equivalent weighted formula

```text
Final Score

=

Offer × 0.20

+

Domain × 0.20

+

Company × 0.20

+

Recruiter × 0.20

+

Context × 0.20
```

---

# 6.7 Example Calculation

Input Scores

| Signal | Score |
|---------|------:|
| Offer | 100 |
| Domain | 80 |
| Company | 100 |
| Recruiter | 100 |
| Context | 94 |

Calculation

```text
100 × 0.20

+

80 × 0.20

+

100 × 0.20

+

100 × 0.20

+

94 × 0.20

=

94.8
```

Final Trust Score

```text
94.8
```

---

# 6.8 Risk Classification

After computing the final score, the fusion engine classifies the internship.

Current classification rules

| Score Range | Risk Level | Color |
|-------------|------------|-------|
| 80–100 | SAFE | Green |
| 60–79.99 | SUSPICIOUS | Yellow |
| Below 60 | HIGH RISK | Red |

---

# 6.9 Risk Classification Flow

```text
Final Score

↓

80+

↓

SAFE

↓

Green



Final Score

↓

60–79

↓

SUSPICIOUS

↓

Yellow



Final Score

↓

Below 60

↓

HIGH RISK

↓

Red
```

---

# 6.10 Confidence Calculation

The confidence score measures how much useful information was successfully extracted from the internship offer.

Confidence is based on four required entities.

| Entity | Contribution |
|---------|-------------:|
| Company Name | 25% |
| Website | 25% |
| Recruiter Email | 25% |
| Salary | 25% |

Example

```text
Company

✓

Website

✓

Recruiter Email

✓

Salary

✓

↓

Confidence

100%
```

Another example

```text
Company

✓

Website

✓

Recruiter Email

✓

Salary

✗

↓

Confidence

75%
```

---

# 6.11 Explanation Generation

Instead of returning only a score, YEScape also produces human-readable explanations.

Each explanation is generated from signal outcomes.

Examples

```text
Offer contains sufficient information.

Website domain appears trustworthy.

Company verified in registry.

Recruiter email is trustworthy.

Offer content appears legitimate.
```

Negative examples

```text
Website domain appears suspicious.

Recruiter email belongs to a free email provider.

Company verification failed.

Offer contains suspicious language.
```

---

# 6.12 Final Verification Result

The fusion engine produces a complete verification summary.

Example

```text
Final Trust Score

94.8

Risk Level

SAFE

Confidence

100%

Reasons

Offer contains sufficient information.

Website domain appears trustworthy.

Company verified in registry.

Recruiter email is trustworthy.

Offer content appears legitimate.
```

---

# 6.13 Output Schema

The Score Fusion Engine updates the following fields inside the Verification Result.

```text
VerificationResult

├── final_score

├── risk_level

├── risk_color

├── confidence

├── reasons

└── signals
```

---

# 6.14 Advantages of Score Fusion

The fusion approach offers several benefits.

- Balanced decision making
- Reduced false positives
- Reduced false negatives
- Easier future expansion
- Explainable AI output
- Stable scoring architecture

---

# 6.15 Future Improvements

Future versions may introduce

- Adaptive weights
- Machine Learning based weighting
- Historical company reputation
- User feedback based calibration
- Bayesian score fusion
- Ensemble trust prediction

Version 2 intentionally uses equal weighting for transparency and explainability.

---

# 6.16 End of Chapter

The Score Fusion Engine is the final decision-making component of YEScape.

It combines the outputs of all verification signals into one trustworthy, explainable, and user-friendly internship trust score.

This score is returned to the frontend and presented to the user as the final verification result.

# Chapter 7 — Frontend Architecture & Version 1 Integration

---

# 7.1 Introduction

YEScape already has a fully designed frontend developed during Version 1.

The Version 1 frontend is deployed and operational.

Version 2 introduces a completely rebuilt backend with modular verification architecture.

The objective of Phase 5 is **NOT** to redesign the application.

The objective is to connect the existing frontend with the new backend.

---

# 7.2 Current Situation

Version 1

✅ Complete UI

✅ Streamlit Pages

✅ Navigation

✅ Landing Page

✅ Verification Page

✅ Research Page

✅ Report Page

✅ Trust Gauge

✅ PDF Download UI

❌ Backend Logic (Old)

---

Version 2

✅ Complete Verification Backend

✅ Offer Parser

✅ Domain Verification

✅ Company Verification

✅ Recruiter Verification

✅ Context Analysis

✅ Verification Engine

✅ Score Fusion

✅ Test Framework

❌ UI Integration

---

# 7.3 Phase 5 Objective

Replace the Version 1 backend with the Version 2 backend.

No redesign is required.

No backend recreation is required.

No duplicate code should be written.

---

# 7.4 Existing Frontend

The frontend already contains

- Landing Page
- Verification Page
- Report Page
- Research Page
- Score Gauge
- Trust Meter
- PDF Download
- Streamlit Navigation
- Session State
- User Workflow

These components should be preserved.

---

# 7.5 Existing Backend

Version 2 backend contains

```text
Verification Engine

↓

Signal Factory

↓

Offer Analysis

↓

Domain Verification

↓

Company Verification

↓

Recruiter Verification

↓

Context Analysis

↓

Score Fusion

↓

Verification Result
```

This backend is production-ready.

No verification logic should be rewritten.

---

# 7.6 Integration Architecture

Current Architecture

```text
User

↓

Version 1 UI

↓

Old Verification Logic

↓

Result
```

Target Architecture

```text
User

↓

Version 1 UI

↓

Verification Engine

↓

Signal Factory

↓

Verification Signals

↓

Score Fusion

↓

Verification Result

↓

Version 1 UI
```

Only the backend connection changes.

The user experience should remain almost identical.

---

# 7.7 Streamlit Entry Point

The deployment entry point is

```text
app.py
```

This file already powers the deployed application.

The final deployment must continue using this file.

The application entry point should **not** be renamed.

---

# 7.8 Required UI Components

The following UI pages already exist and should continue to exist.

---

Landing Page

Purpose

Introduce YEScape.

---

Verification Page

Purpose

Collect internship details.

Inputs

- Offer Letter
- PDF Upload
- Website
- Company
- Recruiter Email

---

Processing Screen

Purpose

Display verification progress.

---

Verification Report

Purpose

Display

- Final Score
- Gauge
- Risk Level
- Confidence
- Signal Breakdown
- Reasons

---

Research Page

Purpose

Display detailed research information.

---

PDF Download

Purpose

Generate downloadable verification reports.

---

# 7.9 Backend Connection

Instead of directly calculating scores inside the UI,

the frontend should only call

```python
VerificationEngine.verify()
```

The UI must never calculate

- Trust Scores

- Risk Levels

- Confidence

- Reasons

These are backend responsibilities.

---

# 7.10 Verification Flow

```text
User clicks

Verify

↓

UI collects input

↓

VerificationRequest

↓

VerificationEngine.verify()

↓

VerificationResult

↓

UI renders report
```

---

# 7.11 Data Flow

Input

```text
User

↓

VerificationRequest
```

Backend

```text
VerificationEngine

↓

VerificationResult
```

Output

```text
VerificationResult

↓

Streamlit Components
```

---

# 7.12 Session State

Existing session management should be preserved.

Session State should store

- Uploaded Offer

- Parsed Offer

- Verification Result

- PDF Path

- User Inputs

No duplicate state management should be introduced.

---

# 7.13 Trust Gauge

The existing semicircle trust gauge should remain.

Only its data source changes.

Current source

Version 1 score.

New source

```python
VerificationResult.final_score
```

---

# 7.14 Report Page

The report page should display

Final Score

Risk Level

Confidence

Reasons

Signal Breakdown

Every displayed value must come from

```python
VerificationResult
```

---

# 7.15 Signal Cards

Each verification signal should display

- Signal Name

- Score

- Status

- Reason

- Details

These values already exist inside

```python
VerificationResult.signals
```

---

# 7.16 PDF Report

The PDF layout already exists.

Only replace the data source.

Instead of Version 1 variables,

use

```python
VerificationResult
```

---

# 7.17 Research Page

The existing research page should remain.

Instead of placeholder information,

populate it using

Signal Details

For example

WHOIS

DNS

HTTPS

Company Registry

Recruiter

Context Analysis

---

# 7.18 Deployment

Deployment platform

Streamlit Cloud

Current deployment

Version 1

Target deployment

Version 2 Backend

Same URL

Same app.py

No new deployment project.

---

# 7.19 What MUST NOT Be Changed

The following should remain unchanged.

❌ Landing Page Design

❌ Streamlit Navigation

❌ Color Theme

❌ Trust Gauge Design

❌ Research Page Layout

❌ Report Page Layout

❌ PDF Layout

❌ Existing User Flow

Only backend connectivity should change.

---

# 7.20 Integration Rules

Future developers must follow these rules.

✓ Never recreate the frontend.

✓ Never rewrite verification logic.

✓ Never duplicate backend modules.

✓ Always call VerificationEngine.

✓ Always use VerificationResult.

✓ Preserve Version 1 UI.

✓ Preserve app.py.

---

# 7.21 End of Chapter

Phase 5 is an integration phase.

The Version 1 frontend already provides a polished user experience.

Version 2 provides a production-ready verification backend.

The goal is to connect these two systems without redesigning either one.

# Chapter 8 — Development Rules & Engineering Guidelines

---

# 8.1 Purpose

This chapter defines the mandatory engineering rules that must be followed while working on YEScape.

These rules apply to

- Human Developers
- AI Coding Assistants
- Antigravity
- Future Contributors

Violation of these rules may break the architecture or introduce duplicate implementations.

---

# 8.2 Primary Development Principle

YEScape Version 2 follows one strict philosophy.

> Reuse Existing Components Whenever Possible.

Before writing new code,

always check whether the functionality already exists.

Never duplicate an existing implementation.

---

# 8.3 Backend Rules

The backend architecture is considered complete.

The following modules must not be rewritten.

```text
Offer Analysis

Domain Verification

Company Verification

Recruiter Verification

Context Analysis

Verification Engine

Signal Factory

Score Fusion
```

Only bug fixes and feature extensions are permitted.

---

# 8.4 Frontend Rules

The Version 1 frontend is considered the official frontend.

Do NOT

- redesign pages
- create duplicate pages
- replace Streamlit
- change navigation
- rewrite layouts

Instead,

connect the existing frontend to the Version 2 backend.

---

# 8.5 Verification Engine Rules

The Verification Engine is the only component allowed to coordinate verification.

Never call verification signals directly from

- UI
- app.py
- Streamlit Pages
- Test Runner

Always use

```python
VerificationEngine.verify()
```

---

# 8.6 Signal Rules

Signals must remain completely independent.

Correct

```text
Verification Engine

↓

Signal

↓

Verification Engine
```

Incorrect

```text
Signal

↓

Signal

↓

Signal
```

Signals must never directly call other signals.

---

# 8.7 Score Fusion Rules

The Score Fusion Engine is the only component allowed to

- calculate final score
- classify risk
- generate confidence
- generate explanations

Frontend code must never calculate

- trust score
- risk level
- confidence

---

# 8.8 Schema Rules

Communication between modules must happen only through schemas.

Examples

```text
VerificationRequest

VerificationResult

SignalResult

OfferData
```

Avoid passing dictionaries when a schema already exists.

---

# 8.9 Testing Rules

Every new feature must include a corresponding test.

Examples

```text
tests/

phase4/

phase5/

future_phase/
```

No feature should be merged without verification.

---

# 8.10 Documentation Rules

Every completed phase must include documentation.

Documentation should contain

- Objective
- Folder
- Workflow
- Inputs
- Outputs
- Status

Documentation should always be updated together with code.

---

# 8.11 Folder Rules

Do not move existing folders unless absolutely necessary.

Preferred structure

```text
core/

signals/

schemas/

tests/

docs/

ui/
```

New modules should follow the same organization.

---

# 8.12 Naming Conventions

Classes

```text
PascalCase
```

Example

```python
VerificationEngine

OfferParser

ScoreFusion
```

Functions

```text
snake_case
```

Example

```python
calculate_score()

verify_company()

parse_offer()
```

Variables

```text
snake_case
```

Constants

```text
UPPER_CASE
```

---

# 8.13 Code Style

Follow PEP 8 conventions.

Rules

- descriptive names
- small functions
- single responsibility
- avoid deeply nested logic
- meaningful comments

Readable code is preferred over clever code.

---

# 8.14 Error Handling

All external operations must use exception handling.

Examples

- DNS
- WHOIS
- HTTP
- File Reading
- PDF Parsing
- OCR

The application should continue operating even if one component fails.

---

# 8.15 Logging Rules

Important operations should be logged.

Examples

```text
Verification Started

Signal Completed

Verification Finished

Execution Time

Errors
```

Logs should help debugging without exposing sensitive user data.

---

# 8.16 Performance Rules

Avoid unnecessary computations.

Reuse parsed data whenever possible.

Do not perform repeated network requests for the same information during a single verification session.

---

# 8.17 Security Rules

Never

- hardcode API keys
- hardcode passwords
- expose secrets
- commit credentials

Sensitive values should be loaded from configuration or environment variables.

---

# 8.18 AI Assistant Rules

When modifying YEScape,

AI assistants must

✓ Understand the existing architecture before writing code.

✓ Extend existing modules instead of replacing them.

✓ Preserve folder structure.

✓ Preserve public interfaces.

✓ Avoid unnecessary refactoring.

✓ Keep backward compatibility whenever possible.

---

# 8.19 Git Rules

Every completed phase should be committed separately.

Example

```text
Phase 4.1

Phase 4.2

Phase 4.3

Phase 4.4

Phase 5.1
```

Commit messages should clearly describe the completed work.

---

# 8.20 Development Philosophy

YEScape follows a modular, maintainable, and scalable architecture.

The goal is not to write the shortest code.

The goal is to build a system that is

- understandable
- reusable
- extensible
- production-ready

Every new feature should improve the system without increasing unnecessary complexity.

---

# 8.21 End of Chapter

This chapter defines the engineering standards that govern the YEScape project.

All future development should follow these rules to maintain consistency, reliability, and long-term maintainability.

# Chapter 9 — Project Roadmap & Current Development Status

---

# 9.1 Purpose

This chapter records the development history of YEScape.

It provides a complete roadmap of the project from Version 1 through Version 2 and defines the remaining work required before production release.

This chapter should always reflect the latest project status.

---

# 9.2 Project Timeline

```text
Phase 1

↓

Initial MVP

↓

Version 1

↓

Version 2 Backend Rebuild

↓

Phase 5 Integration

↓

Production Release
```

---

# 9.3 Version History

| Version | Status | Description |
|----------|--------|-------------|
| Version 1 | Completed | Initial working Streamlit application with UI and basic verification |
| Version 2 | In Progress | Complete backend redesign using modular architecture |
| Production Version | Planned | Integrated frontend + backend with deployment-ready architecture |

---

# 9.4 Completed Phases

---

## Phase 1

Status

```text
Completed
```

Objectives

- Initial project planning
- MVP creation
- Basic Streamlit application
- Initial UI
- Initial scoring system

---

## Phase 2

Status

```text
Completed
```

Objectives

- Domain verification
- Company verification
- Recruiter verification
- Context analysis
- Modular signal development

---

## Phase 3

Status

```text
Completed
```

Objectives

- Independent verification signals
- Registry database
- Domain verification engine
- Recruiter verification engine
- Context scoring engine

---

## Phase 4

Status

```text
Completed
```

Objectives

- Offer Parser
- Verification Engine
- Signal Factory
- Score Fusion Engine
- Final Verification Result
- Test Framework
- Logging
- Execution Timing
- Documentation

---

# 9.5 Phase 4 Deliverables

The following components are fully implemented.

## Core

```text
Verification Engine

Signal Factory

Score Fusion
```

---

## Signals

```text
Signal 1

Offer Analysis

Signal 2

Domain Verification

Signal 3

Company Verification

Signal 4

Recruiter Verification

Signal 5

Context Analysis
```

---

## Schemas

```text
VerificationRequest

VerificationResult

SignalResult

OfferData
```

---

## Tests

```text
Offer Parser

Offer Engine

Verification Engine

Pipeline

Runner
```

---

## Documentation

Phase 4 documentation completed.

---

# 9.6 Current System Status

Backend

```text
100%

Completed
```

Signal Engine

```text
100%

Completed
```

Verification Engine

```text
100%

Completed
```

Score Fusion

```text
100%

Completed
```

Testing

```text
Completed
```

Documentation

```text
Completed
```

---

# 9.7 Current Frontend Status

The frontend already exists from Version 1.

Available Pages

- Landing Page
- Verification Page
- Processing Screen
- Report Page
- Research Page
- PDF Download

Current Status

```text
Ready for Integration
```

---

# 9.8 Current Deployment

Deployment Platform

```text
Streamlit Cloud
```

Current Application

```text
YEScape Version 1
```

Deployment Entry Point

```text
app.py
```

Current Public URL

```text
https://yescape-ai.streamlit.app/
```

---

# 9.9 Remaining Work

The remaining work belongs entirely to Phase 5.

No backend redevelopment is required.

The backend should only be integrated with the existing frontend.

---

# 9.10 Phase 5 Objectives

Primary Goal

Connect the completed Version 2 backend with the Version 1 frontend.

Subtasks

- Connect UI to Verification Engine
- Replace old scoring system
- Connect report page
- Connect research page
- Connect trust gauge
- Connect PDF generation
- Preserve Streamlit navigation
- Preserve existing UI

---

# 9.11 Future Phases

Potential future development includes

Phase 6

- Chrome Extension
- Browser Plugin
- Real-time Website Verification

Phase 7

- AI Semantic Verification
- LLM Risk Explanation
- Advanced Scam Detection

Phase 8

- Mobile Application
- Android
- iOS

Phase 9

- Enterprise Dashboard
- Recruiter Portal
- Admin Console

---

# 9.12 Current Development Philosophy

The backend is considered stable.

Future work should focus on

- Integration
- User Experience
- Performance
- Deployment
- AI Enhancement

The verification architecture should remain unchanged unless a significant improvement is required.

---

# 9.13 Development Progress Summary

| Component | Completion |
|------------|-----------:|
| Backend Architecture | 100% |
| Verification Signals | 100% |
| Verification Engine | 100% |
| Score Fusion | 100% |
| Test Framework | 100% |
| Documentation | 100% |
| Frontend UI | 100% (Version 1) |
| Backend Integration | 0% |
| Production Release | Pending |

---

# 9.14 Definition of Phase Completion

A phase is considered complete only when

✓ Implementation completed

✓ Testing completed

✓ Documentation completed

✓ Git committed

✓ Stable execution verified

Only then should development proceed to the next phase.

---

# 9.15 End of Chapter

At the completion of Phase 4, YEScape possesses a fully functional modular verification backend and a completed Version 1 frontend.

The project has entered Phase 5, whose sole objective is to integrate these two systems into a single production-ready application without rebuilding either component.

# Chapter 10 — Antigravity AI Development Instructions

---

# 10.1 Purpose

This chapter defines the mandatory working rules for Antigravity AI while developing YEScape.

Antigravity should treat this document as the single source of truth before generating or modifying any code.

The objective is to continue development without breaking the existing architecture.

---

# 10.2 Project Understanding

Before writing any code, Antigravity must understand the following.

YEScape is **NOT** a new project.

It is an existing project with

- Version 1 Frontend
- Version 2 Backend

The backend has already been rebuilt.

The frontend already exists.

Only integration work remains.

---

# 10.3 Primary Objective

The primary objective is

```text
Connect

Version 1 UI

↓

Version 2 Backend
```

Not

```text
Create

New UI

↓

New Backend
```

---

# 10.4 Existing Backend

The following backend modules are complete.

```text
Offer Parser

Offer Engine

Verification Engine

Signal Factory

Score Fusion

Signal 1

Signal 2

Signal 3

Signal 4

Signal 5
```

These modules should be reused.

They should not be recreated.

---

# 10.5 Existing Frontend

The frontend already contains

- Landing Page

- Verification Page

- Research Page

- Report Page

- Trust Gauge

- PDF Download

- Streamlit Navigation

These pages should remain intact.

---

# 10.6 Entry Point

The deployed application uses

```text
app.py
```

This file must remain the application's entry point.

Do not replace it.

Do not rename it.

---

# 10.7 Allowed Modifications

Antigravity is allowed to

✓ Connect frontend to backend

✓ Fix bugs

✓ Improve performance

✓ Improve code readability

✓ Add missing integration

✓ Add documentation

✓ Improve maintainability

---

# 10.8 Forbidden Actions

Antigravity must NEVER

❌ Rewrite the frontend

❌ Rewrite verification logic

❌ Replace Streamlit

❌ Duplicate backend modules

❌ Create parallel implementations

❌ Break folder structure

❌ Rename public interfaces without approval

❌ Change deployed application workflow

---

# 10.9 Integration Workflow

Correct workflow

```text
User

↓

Streamlit UI

↓

VerificationRequest

↓

VerificationEngine.verify()

↓

VerificationResult

↓

Streamlit Report
```

Any other architecture should be avoided.

---

# 10.10 Existing Architecture Must Be Preserved

Current architecture has already been tested.

Do not replace

```text
Verification Engine

↓

Signal Factory

↓

Verification Signals

↓

Score Fusion
```

Instead

extend it when necessary.

---

# 10.11 Code Generation Rules

Before generating any code

Antigravity must

1.

Search existing implementation.

2.

Reuse existing implementation.

3.

Modify only if necessary.

4.

Generate new code only if no implementation exists.

---

# 10.12 Refactoring Rules

Refactoring is allowed only when

- it improves readability

- it removes duplication

- it preserves functionality

Large architectural refactoring is prohibited unless explicitly requested.

---

# 10.13 Testing Rules

Every change should be validated.

If a new feature is added

a corresponding test should also be added.

No feature should remain untested.

---

# 10.14 Documentation Rules

Whenever a feature is completed

documentation should also be updated.

Implementation and documentation should remain synchronized.

---

# 10.15 Debugging Rules

When errors occur

Antigravity should

1.

Identify root cause.

2.

Fix the smallest possible component.

3.

Avoid rewriting unrelated modules.

4.

Preserve existing behavior.

---

# 10.16 Performance Rules

Avoid

- repeated calculations

- duplicate parsing

- duplicate API calls

- unnecessary object creation

Prefer reusable and cached results whenever appropriate.

---

# 10.17 Version Control Rules

Every completed milestone should correspond to a Git commit.

Recommended commit style

```text
Phase 5.1

Phase 5.2

Phase 5.3
```

Large unrelated commits should be avoided.

---

# 10.18 Communication Rules

If the requested modification affects multiple modules,

Antigravity should first explain

- what will change

- why it is required

- which files will be modified

before generating code.

---

# 10.19 Long-Term Vision

YEScape is designed as a scalable AI-powered internship verification platform.

Future additions should fit naturally into the existing modular architecture rather than replacing it.

---

# 10.20 Success Criteria

A task is considered successful only if

✓ Existing functionality remains operational.

✓ No completed module is unnecessarily recreated.

✓ Backend remains modular.

✓ Frontend remains unchanged unless requested.

✓ New functionality integrates cleanly.

✓ Tests continue to pass.

✓ Documentation remains accurate.

---

# 10.21 End of Chapter

Antigravity should always prioritize **integration over recreation**, **extension over replacement**, and **maintainability over unnecessary complexity**.

This chapter defines the mandatory operational rules for all future AI-assisted development of the YEScape project.

# Chapter 11 — Project File Inventory & Module Responsibilities

---

# 11.1 Purpose

This chapter documents the purpose and responsibility of every important folder and module in the YEScape project.

It serves as a navigation guide for developers and AI assistants.

Before modifying any file, developers should understand its role within the overall architecture.

---

# 11.2 Project Root

The current repository documents the Version 2 backend.

Typical structure

```text
YESCAPE-Version2/

├── core/
├── signals/
├── schemas/
├── tests/
├── docs/
├── ui/
├── assets/
├── database/
├── utils/
├── requirements.txt
├── README.md
```

Note

The deployment application (`app.py`) is **NOT** part of this repository.

It exists inside the original **YEScape-AI** project, which contains the Streamlit frontend.
---

# 11.3 app.py (Version 1 Project)

Purpose

The Streamlit application entry point is located inside the **YEScape Version 1** project.

It is **not** part of the Version 2 backend repository.

Responsibilities

- Launch the Streamlit application
- Display the existing UI
- Handle navigation
- Receive user inputs
- Call the Version 2 Verification Engine
- Display the verification report

Current Status

```text
Exists in YEScape Version 1 Project
```

Phase 5 Objective

Connect this existing frontend to the completed Version 2 backend.

Editable

✅ Yes (during Phase 5 integration only)

Restrictions

- Do not recreate this file.
- Do not create another Streamlit entry point.
- Continue using the existing `app.py` from Version 1.

---

# 11.4 core/

Purpose

Contains the central business logic of YEScape.

Responsibilities

- Verification Engine
- Signal Factory
- Score Fusion
- Pipeline Management

Editable

✅ Yes

Restrictions

Do not duplicate existing logic.

---

# 11.5 core/verification_engine.py

Purpose

Coordinates the complete verification workflow.

Responsibilities

- Execute all signals
- Collect results
- Perform score fusion
- Produce VerificationResult

Dependencies

```text
Signal Factory

Score Fusion

Schemas
```

Editable

✅ Yes

Restrictions

Must remain the single verification coordinator.

---

# 11.6 core/signal_factory.py

Purpose

Creates all verification signal objects.

Responsibilities

Instantiate

- Offer
- Domain
- Company
- Recruiter
- Context

Editable

✅ Yes

Restrictions

Must not contain business logic.

---

# 11.7 core/fusion/

Purpose

Final score computation.

Contains

```text
score_fusion.py
```

Responsibilities

- Final Trust Score
- Risk Classification
- Confidence
- Reasons

Editable

✅ Yes

Restrictions

No verification logic should exist here.

---

# 11.8 signals/

Purpose

Contains independent verification signals.

Current Signals

```text
Signal 1

Offer Analysis

Signal 2

Domain Verification

Signal 3

Company Verification

Signal 4

Recruiter Verification

Signal 5

Context Analysis
```

Editable

✅ Yes

Restrictions

Signals must remain independent.

Signals should never directly call one another.

---

# 11.9 schemas/

Purpose

Contains all shared data structures.

Examples

```text
VerificationRequest

VerificationResult

SignalResult

OfferData
```

Editable

✅ Yes

Restrictions

Schemas should remain lightweight.

Avoid embedding business logic.

---

# 11.10 tests/

Purpose

Project testing.

Responsibilities

- Unit Tests
- Integration Tests
- Pipeline Tests
- Regression Tests

Editable

✅ Yes

Restrictions

Every new feature should include corresponding tests.

---

# 11.11 docs/

Purpose

Project documentation.

Contains

- Phase Documentation
- Architecture Notes
- Specifications
- Development Guides

Editable

✅ Yes

Restrictions

Documentation should remain synchronized with implementation.

---

# 11.12 ui/

Purpose

Contains reusable Streamlit UI components.

Examples

- Cards
- Gauge
- Report Components
- Navigation

Editable

✅ Yes

Restrictions

Maintain consistent UI style.

---

# 11.13 assets/

Purpose

Static project resources.

Examples

- Images
- Logos
- Icons
- Backgrounds

Editable

✅ Yes

Restrictions

Do not modify branding without approval.

---

# 11.14 database/

Purpose

Contains local datasets and verification resources.

Examples

- Company Registry
- Scam Keywords
- Domain Lists

Editable

✅ Yes

Restrictions

Preserve existing dataset format.

---

# 11.15 utils/

Purpose

Common utility functions.

Examples

- Formatting
- File Helpers
- Logging
- Validators

Editable

✅ Yes

Restrictions

Keep utilities generic and reusable.

---

# 11.16 requirements.txt

Purpose

Python dependency list.

Editable

✅ Yes

Restrictions

Only add packages when required.

Avoid unnecessary dependencies.

---

# 11.17 README.md

Purpose

Developer introduction.

Responsibilities

- Installation
- Setup
- Running the Project
- Basic Overview

Editable

✅ Yes

---

# 11.18 Protected Modules

The following modules are considered stable.

Avoid rewriting them unless necessary.

```text
Verification Engine

Signal Factory

Score Fusion

Offer Parser

Offer Engine

All Verification Signals
```

---

# 11.19 Integration Modules

Phase 5 will primarily modify the following components.

Version 1 Project

```text
app.py

Existing Streamlit Pages

Verification UI

Report UI

Research Page

Trust Gauge

PDF Download
```

Version 2 Project

```text
Verification Engine

VerificationResult

Score Fusion

Schemas

Session Integration
```

The objective is to connect these two projects without rebuilding either one.

---

# 11.20 Module Dependency Diagram

```text
YEScape Version 1

(Streamlit app.py)

↓

Existing UI

↓

VerificationRequest

↓

YEScape Version 2

Verification Engine

↓

Signal Factory

↓

Signals

↓

Score Fusion

↓

VerificationResult

↓

Back to Version 1 UI

↓

Report Display
```

---

# 11.21 Editable vs Protected Summary

Module              Location	            Editable	     Purpose
app.py	            YEScape Version 1	       ✅	    Streamlit Entry Point
Existing UI Pages	YEScape Version 1	       ✅	    User Interface
core	            YEScape Version 2	       ✅	    Business Logic
signals	            YEScape Version 2	       ✅	    Verification Modules
schemas	            YEScape Version 2	       ✅	    Data Models
tests	            YEScape Version 2	       ✅	    Testing
docs	            YEScape Version 2	       ✅	    Documentation


Protected Components

- Verification Architecture
- Signal Independence
- Score Fusion Design

---

# 11.22 End of Chapter

This inventory provides a complete overview of the YEScape project structure.

Developers and AI assistants should consult this chapter before modifying any project file to ensure that changes remain consistent with the established architecture.

# Chapter 12 — Phase 5 Integration Specification

---

# 12.1 Purpose

The objective of Phase 5 is to integrate the completed Version 2 backend with the existing Version 1 frontend.

No major backend redevelopment is required.

No frontend redesign is required.

The focus is integration.

---

# 12.2 Current Situation

Current System

```text
YEScape Version 1

↓

Complete Streamlit Frontend

↓

Existing UI
```

Current Backend

```text
YEScape Version 2

↓

Verification Engine

↓

Signals

↓

Score Fusion
```

Phase 5 combines these two systems.

---

# 12.3 Overall Goal

Final Architecture

```text
User

↓

Version 1 Streamlit UI

↓

VerificationRequest

↓

Version 2 Verification Engine

↓

VerificationResult

↓

Version 1 Report UI
```

---

# 12.4 Scope

Phase 5 includes

✓ UI Integration

✓ Session Handling

✓ Backend Connection

✓ Report Rendering

✓ PDF Generation

✓ Research Page Integration

✓ Deployment

Phase 5 does NOT include

❌ Rewriting backend

❌ Rewriting frontend

❌ Creating duplicate pages

---

# 12.5 Components to Integrate

Frontend Components

- Landing Page
- Verification Page
- Processing Page
- Report Page
- Research Page
- PDF Download
- Navigation
- Trust Gauge

Backend Components

- Verification Engine
- Verification Request
- Verification Result
- Score Fusion
- All Verification Signals

---

# 12.6 Integration Workflow

Step 1

Collect user input.

↓

Step 2

Create VerificationRequest.

↓

Step 3

Execute

```python
VerificationEngine.verify()
```

↓

Step 4

Receive VerificationResult.

↓

Step 5

Populate Report UI.

↓

Step 6

Generate PDF.

---

# 12.7 Input Mapping

Frontend Field

↓

Backend Field

Company Name

↓

request.company

Recruiter Email

↓

request.recruiter_email

Website

↓

request.website

Offer Letter

↓

request.offer_text

Uploaded PDF

↓

Offer Parser

---

# 12.8 Output Mapping

VerificationResult

↓

Trust Gauge

↓

Final Score

↓

Risk Level

↓

Confidence

↓

Reasons

↓

Signal Cards

↓

Research Page

↓

PDF

---

# 12.9 Streamlit Session State

Session State should contain

```text
VerificationRequest

VerificationResult

Current Page

Upload Status

Processing Status
```

Avoid recalculating results while navigating between pages.

---

# 12.10 Report Page

The report page should display

- Final Trust Score
- Risk Level
- Confidence
- Reasons
- Signal Scores
- Signal Details

The report page should never calculate values itself.

Everything must come from VerificationResult.

---

# 12.11 Gauge Integration

The existing Version 1 gauge should receive

```python
result.final_score
```

Color

```python
result.risk_color
```

Risk Label

```python
result.risk_level
```

No frontend calculations.

---

# 12.12 Research Page

Research page should consume

Signal Details

Examples

- Domain Details
- Company Details
- Recruiter Details
- Context Details

The backend already produces this information.

---

# 12.13 PDF Integration

The PDF should use

VerificationResult

instead of recalculating scores.

PDF should include

- Company
- Recruiter
- Final Score
- Risk
- Confidence
- Signal Summary
- Reasons

---

# 12.14 Error Handling

Frontend errors should never crash the application.

Examples

- Missing company

- Missing email

- Invalid website

- Empty offer letter

Backend exceptions should be displayed as user-friendly messages.

---

# 12.15 Performance Goal

Target

```text
Verification Time

< 10 seconds
```

Reuse backend results whenever possible.

Avoid duplicate verification.

---

# 12.16 Completion Criteria

Phase 5 is complete when

✓ Version 1 UI calls Version 2 backend.

✓ Reports display VerificationResult.

✓ Trust Gauge displays backend score.

✓ PDF uses backend data.

✓ Research page uses backend details.

✓ No duplicate verification logic exists.

✓ Application deploys successfully.

---

# 12.17 End of Chapter

Phase 5 is an integration phase.

The objective is to connect two completed systems into one production-ready application while preserving the architecture already established in Versions 1 and 2.

# Chapter 13 — Development Workflow

---

# 13.1 Purpose

This chapter defines the standard development workflow for YEScape.

Every developer and AI assistant should follow this workflow before implementing any feature.

The objective is to maintain consistency, prevent regressions, and preserve the modular architecture.

---

# 13.2 Development Lifecycle

Every task should follow the sequence below.

```text
Understand Requirement

↓

Analyze Existing Code

↓

Design Solution

↓

Implement

↓

Test

↓

Document

↓

Git Commit

↓

Proceed to Next Task
```

No step should be skipped.

---

# 13.3 Before Writing Code

Before generating or modifying any code,

developers should answer the following questions.

- Does this feature already exist?

- Which module is responsible?

- Can existing code be reused?

- Will this affect other modules?

Only after answering these questions should implementation begin.

---

# 13.4 Feature Development Process

Each new feature should follow this order.

Step 1

Understand the requirement.

↓

Step 2

Locate the responsible module.

↓

Step 3

Modify only the required files.

↓

Step 4

Run tests.

↓

Step 5

Update documentation.

↓

Step 6

Create Git commit.

---

# 13.5 Bug Fix Workflow

When a bug is found,

the workflow should be

```text
Reproduce Bug

↓

Find Root Cause

↓

Fix Smallest Possible Component

↓

Run Regression Tests

↓

Update Documentation

↓

Commit
```

Large rewrites should be avoided.

---

# 13.6 Code Reuse Policy

YEScape follows a reuse-first philosophy.

Preferred order

1.

Reuse existing implementation.

2.

Extend existing implementation.

3.

Create helper functions.

4.

Create new module only when absolutely necessary.

Duplicate implementations are prohibited.

---

# 13.7 Testing Workflow

Every modification should be validated.

Testing order

```text
Unit Test

↓

Integration Test

↓

Pipeline Test

↓

Manual Verification
```

Deployment should occur only after all tests pass.

---

# 13.8 Documentation Workflow

Every completed feature should include

- Documentation update

- Architecture update (if required)

- README update (if applicable)

Implementation and documentation should always remain synchronized.

---

# 13.9 Git Workflow

Each logical milestone should correspond to one Git commit.

Recommended format

```text
Phase 5.1

Backend Integration

Phase 5.2

UI Connection

Phase 5.3

PDF Integration
```

Avoid combining unrelated changes into a single commit.

---

# 13.10 Branch Strategy

Recommended workflow

```text
main

↓

feature branch

↓

testing

↓

merge into main
```

For small personal development,

direct commits to `main` are acceptable after successful testing.

---

# 13.11 AI-Assisted Development Workflow

When using Antigravity AI,

the workflow should be

```text
Read MASTER_PROJECT_SPECIFICATION.md

↓

Understand Current Phase

↓

Analyze Existing Files

↓

Generate Minimal Changes

↓

Run Tests

↓

Update Documentation

↓

Git Commit
```

AI should never skip the analysis step.

---

# 13.12 Phase Completion Checklist

Before declaring any phase complete,

verify

✓ Code implemented

✓ Tests passed

✓ Documentation updated

✓ Git committed

✓ Stable execution confirmed

Only then proceed to the next phase.

---

# 13.13 Long-Term Maintenance

Future updates should

- preserve modularity

- minimize breaking changes

- reuse existing components

- maintain documentation accuracy

The project should become easier to maintain over time rather than more complex.

---

# 13.14 End of Chapter

Following this workflow ensures that YEScape remains maintainable, testable, and scalable throughout its future development lifecycle.

# Chapter 14 — Project Standards, Deployment, Future Roadmap & Final AI Instructions

---

# 14.1 Purpose

This chapter defines the permanent development standards, deployment strategy, troubleshooting procedures, future roadmap, and mandatory AI instructions for the YEScape project.

It serves as the final operational guide for all future development.

---

# 14.2 Coding Standards

YEScape follows consistent coding standards throughout the project.

---

## Python Style

Follow PEP-8 wherever practical.

Example

```python
def verify_offer(request):
    pass
```

Avoid

```python
def VerifyOffer(Request):
    pass
```

---

## Naming Convention

Classes

```text
PascalCase
```

Example

```python
VerificationEngine
OfferParser
ScoreFusion
```

---

Functions

```text
snake_case
```

Example

```python
verify()

calculate()

generate_report()

create_request()
```

---

Variables

```text
snake_case
```

Example

```python
final_score

risk_level

domain_result
```

---

Constants

```text
UPPER_CASE
```

Example

```python
MAX_SCORE

DEFAULT_TIMEOUT
```

---

## File Naming

Always use

```text
snake_case.py
```

Example

```text
verification_engine.py

offer_parser.py

score_fusion.py
```

Avoid

```text
VerificationEngine.py

OfferParser.py
```

---

# 14.3 Project Structure Rules

Every module must have one responsibility.

Correct

```text
Offer Parser

↓

Offer Engine

↓

Verification Engine

↓

Score Fusion
```

Incorrect

```text
One file

↓

Everything
```

---

# 14.4 Reusability Rules

Before writing new code,

always check

- Does this already exist?

- Can this module be reused?

- Can this function be extended?

Duplicate implementations should never be created.

---

# 14.5 Error Handling Standards

All external operations should be protected.

Examples

- DNS lookup

- WHOIS lookup

- HTTPS request

- File upload

- PDF parsing

Always use graceful fallback.

The application should never terminate because of a single failed signal.

---

# 14.6 Logging Standards

Every important operation should be logged.

Example

```text
Verification Started

↓

Offer Parsed

↓

Domain Verified

↓

Company Verified

↓

Recruiter Verified

↓

Context Verified

↓

Score Fusion

↓

Verification Completed
```

Logs should remain readable and chronological.

---

# 14.7 Testing Standards

Every new feature must include testing.

Testing order

```text
Unit Test

↓

Integration Test

↓

Pipeline Test

↓

Manual Test
```

No feature should be merged without successful testing.

---

# 14.8 Documentation Standards

Whenever implementation changes,

documentation must also be updated.

Required updates

- Phase Documentation

- README

- Architecture Documents

- MASTER_PROJECT_SPECIFICATION.md

Implementation and documentation should never become inconsistent.

---

# 14.9 Deployment Guide

Current deployment architecture

```text
YEScape Version 1

↓

app.py

↓

Streamlit Cloud

↓

Public Application
```

Backend

```text
YEScape Version 2

↓

Imported by Version 1

↓

Verification Engine
```

Deployment strategy

The existing Streamlit application remains the deployment entry point.

No second application should be deployed.

---

# 14.10 Deployment Workflow

Standard deployment sequence

```text
Code Complete

↓

Run Tests

↓

Git Commit

↓

Git Push

↓

Streamlit Auto Deploy

↓

Verify Production
```

Deployment should only occur after successful testing.

---

# 14.11 Common Troubleshooting

## ModuleNotFoundError

Verify

```text
__init__.py

Import paths

Virtual Environment
```

---

## DNS Lookup Failed

This usually indicates

- No Internet

- DNS blocked

Verification should continue using fallback values.

---

## HTTPS Connection Failed

Possible causes

- Invalid domain

- Firewall

- Network issue

Fallback scoring should be applied.

---

## WHOIS Failure

WHOIS services occasionally fail.

Use cached or fallback trust score.

---

## PDF Parsing Failure

Verify

- Uploaded file

- OCR extraction

- Offer Parser

---

## Streamlit Error

Verify

```text
Version 1

↓

app.py
```

The deployment entry point must remain unchanged.

---

## Session State Error

Always initialize

```python
st.session_state
```

before accessing values.

---

# 14.12 Performance Guidelines

Target verification time

```text
< 10 seconds
```

Avoid

- Duplicate OCR

- Duplicate parsing

- Duplicate verification

- Duplicate API requests

Reuse cached VerificationResult whenever possible.

---

# 14.13 Future Roadmap

The planned evolution of YEScape is divided into phases.

---

## Phase 5

Frontend Integration

- Connect Version 1 UI

- Report Rendering

- PDF Integration

- Research Page

- Deployment

---

## Phase 6

Artificial Intelligence

- LLM-powered explanations

- AI chatbot

- Scam reasoning

- Personalized recommendations

---

## Phase 7

Browser Extension

- Chrome Extension

- One-click verification

- Website scanning

---

## Phase 8

Cloud Platform

- User Accounts

- Verification History

- Analytics Dashboard

- Admin Panel

---

## Phase 9

Enterprise Version

- University Integration

- Placement Cell Dashboard

- Company Verification Portal

- API Access

---

# 14.14 Long-Term Vision

YEScape aims to become a complete AI-powered internship and job verification platform.

Future versions should prioritize

- Reliability

- Explainability

- Scalability

- Security

- Maintainability

---

# 14.15 Final AI Instructions

Any AI assistant contributing to YEScape must follow these rules.

Always

✓ Read MASTER_PROJECT_SPECIFICATION.md first.

✓ Analyze existing implementation before writing code.

✓ Reuse existing modules whenever possible.

✓ Preserve project architecture.

✓ Generate minimal required changes.

✓ Explain modifications before implementation.

Never

❌ Rewrite the frontend.

❌ Rewrite the backend.

❌ Duplicate verification logic.

❌ Break folder structure.

❌ Introduce unnecessary dependencies.

❌ Remove tested functionality.

---

# 14.16 Project Completion Criteria

A milestone is considered complete only when

✓ Implementation is finished.

✓ Tests pass successfully.

✓ Documentation is updated.

✓ Git commit created.

✓ Git pushed.

✓ Production deployment verified.

Only after satisfying all criteria should development proceed to the next milestone.

---

# 14.17 Final Statement

YEScape has been developed as a modular, extensible, and AI-ready internship verification platform.

The project combines an established Streamlit frontend (Version 1) with a fully modular verification backend (Version 2).

Future development should focus on integration, refinement, intelligent features, and production readiness while preserving the architecture defined in this specification.

---


# END Chapter 14 

# Appendix A — Project Glossary

---

## Purpose

This appendix defines important terms used throughout the YEScape project.

It ensures that developers, AI assistants, and future contributors interpret terminology consistently.

---

## AI

Artificial Intelligence techniques used to assist internship verification and scam detection.

---

## Backend

The business logic responsible for verification.

In YEScape this refers to Version 2.

---

## Frontend

The Streamlit web application.

In YEScape this refers to Version 1.

---

## Verification Engine

The central controller responsible for executing every verification signal.

---

## Signal

An independent verification module responsible for evaluating one aspect of an internship offer.

Current signals include

- Offer Analysis

- Domain Verification

- Company Verification

- Recruiter Verification

- Context Analysis

---

## Score Fusion

The module responsible for combining all signal scores into one Final Trust Score.

---

## VerificationRequest

Input object passed into the Verification Engine.

Contains

- Company

- Website

- Recruiter Email

- Offer Text

---

## VerificationResult

Output object produced by the Verification Engine.

Contains

- Final Score

- Risk Level

- Confidence

- Reasons

- Signals

---

## Trust Score

Overall verification score.

Range

```text
0 – 100
```

---

## Confidence

Represents how complete the extracted internship information is.

---

## Risk Level

Classification generated from the Final Trust Score.

Possible values

```text
SAFE

CAUTION

HIGH RISK
```

---

## OCR

Optical Character Recognition.

Used for extracting text from uploaded offer letters.

---

## PDF Report

Downloadable verification report generated from VerificationResult.

---

## Streamlit

Python framework used for the YEScape frontend.

---

## End of Appendix A

# Appendix B — Project Folder Structure

---

## Purpose

This appendix documents the logical organization of the YEScape project.

---

```text
YEScape Version 1

│

├── app.py

├── Streamlit Pages

├── Assets

├── UI Components

└── Deployment
```

↓

```text
YEScape Version 2

│

├── core

│   ├── verification_engine.py

│   ├── signal_factory.py

│   └── fusion

│

├── signals

│

├── schemas

│

├── tests

│

├── docs

│

├── database

│

├── utils

│

└── assets
```

---

## Relationship

Version 1

↓

User Interface

↓

VerificationRequest

↓

Version 2 Backend

↓

VerificationResult

↓

Version 1 Report

---

## End of Appendix B

# Appendix C — Development Timeline

---

## YEScape Evolution

### Version 1

Completed

Features

- Streamlit UI

- Landing Page

- Verification Page

- Report Page

- Research Page

- Trust Gauge

- PDF Download

Deployment

```text
https://yescape-ai.streamlit.app/
```

---

### Version 2

Completed

Features

- Offer Parser

- Offer Engine

- Verification Engine

- Domain Verification

- Company Verification

- Recruiter Verification

- Context Analysis

- Score Fusion

- Testing Framework

- Documentation

---

### Phase 5

Current Phase

Objectives

- Integrate Version 2 Backend

- Connect Version 1 UI

- Replace existing verification logic

- Use VerificationResult everywhere

- Production Deployment

---

### Future Phases

Phase 6

Artificial Intelligence

Phase 7

Browser Extension

Phase 8

Cloud Platform

Phase 9

Enterprise Platform

---

## End of Appendix C

# Appendix D — Git Commit Standards

---

## Purpose

Maintain a clean and understandable Git history.

---

## Commit Format

```text
Phase X.Y

Short Description
```

Examples

```text
Phase 4.1

Offer Parser Completed

Phase 4.2

Verification Signals Added

Phase 4.3

Score Fusion Completed

Phase 5.1

Frontend Integration Started

Phase 5.2

UI Connected to Backend

Phase 5.3

PDF Integration Completed
```

---

## Rules

Each commit should represent one logical milestone.

Avoid combining unrelated work.

---

## Before Every Commit

Verify

✓ Code executes

✓ Tests pass

✓ Documentation updated

✓ No unused files

✓ Working tree clean

---

## Recommended Workflow

```text
Implement

↓

Test

↓

Document

↓

Git Status

↓

Git Commit

↓

Git Push
```

---

## End of Appendix D

# End of MASTER_PROJECT_SPECIFICATION.md