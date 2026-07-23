# Signal 3 — Company Trust

## Objective

Evaluate whether an internship is genuinely associated with the claimed company.

Unlike many verification systems that rely on search engine results, YEScape uses a **verified Company Registry** as the reference source.

This design improves reproducibility, execution speed, and research reliability while eliminating dependency on external search APIs.

---

## Architecture

Company Name

↓

Company Registry

↓

Official Domain Matching

↓

Career Portal Verification

↓

Company Trust Score

---

## Modules

### Phase 3.3.1

Company Name Extraction

Extracts the company name from the internship posting.

---

### Phase 3.3.2

Company Registry

A curated registry containing

- Company Name
- Official Domain
- Official Career Portal
- Country

The registry replaces search-engine based discovery.

Advantages

- Offline
- Deterministic
- Faster
- Research-friendly
- Easily expandable

---

### Phase 3.3.3

Official Domain Matching

Compares the internship URL with the official company domain.

Output

- Domain Match
- Domain Score

---

### Phase 3.3.4

Career Portal Verification

Verifies whether the internship belongs to the company's official recruitment portal.

Examples

Official

- careers.google.com
- amazon.jobs
- careers.microsoft.com

Suspicious

- google-careers-job.com
- microsoft-jobs.net

Output

Career Verification Score

---

### Phase 3.3.5

Company Trust Score

Combines

- Registry Verification
- Domain Matching
- Career Portal Verification

into a single Company Trust Score (0–100).

Weight Distribution

Registry Verification → 20%

Official Domain Match → 40%

Career Portal Verification → 40%

Output

Company Trust Score