# Signal Architecture

## Overview

YEScape evaluates every internship using five independent verification signals.

Each signal operates independently and produces a normalized trust score.

The signals never communicate with one another directly.

The Fusion Engine combines them only after all signals have completed execution.

---

## Signal Flow

```
Internship Offer
        │
        ▼
Signal 1
ML Scam Probability
        │
        ▼
Signal 2
Domain Intelligence
        │
        ▼
Signal 3
Recruiter Identity
        │
        ▼
Signal 4
Company Verification
        │
        ▼
Signal 5
Context Intelligence
        │
        ▼
Fusion Engine
        │
        ▼
YESScore
```

---

## Design Principles

- Independent execution
- Modular implementation
- Replaceable components
- Explainable outputs
- Standardized trust scores