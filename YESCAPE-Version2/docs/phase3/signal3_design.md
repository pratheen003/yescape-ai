# Signal 3 — Company Trust Signal

## Phase

Phase 3.3

---

# Objective

The Company Trust Signal evaluates whether an internship offer genuinely belongs to the company that it claims to represent.

Unlike traditional internship verification systems that rely on search engine results or manual verification, YEScape uses a deterministic Company Registry combined with domain verification techniques to produce a reproducible Company Trust Score.

The objective is to detect fake company websites, unofficial recruitment pages, impersonation domains, and suspicious internship portals.

---

# Research Motivation

Many internship scams impersonate legitimate organizations.

Examples include:

- google-careers-job.com
- microsoft-careers.net
- amazon-internship.org

These websites appear trustworthy but are not owned by the respective companies.

Traditional search-engine-based verification is unsuitable because:

- Search rankings change over time.
- Results differ across users and regions.
- External APIs reduce reproducibility.
- Internet dependency increases latency.

To overcome these limitations, YEScape introduces a verified Company Registry that serves as a trusted reference dataset.

---

# Signal Architecture

Internship Offer

↓

Company Name Extraction

↓

Company Registry Lookup

↓

Official Domain Matching

↓

Career Portal Verification

↓

Company Trust Score

---

# Components

## 3.3.1 Company Name Extraction

### Objective

Extract the organization name from the internship offer.

### Input

Internship description

### Output

Company Name

Example

Input

Google Software Engineering Internship

Output

Google

---

## 3.3.2 Company Registry

### Objective

Maintain a verified database of legitimate companies.

### Stored Information

- Company Name
- Official Domain
- Official Career Portal
- Country

Example

| Company | Official Domain | Career Portal |
|----------|-----------------|---------------|
| Google | google.com | careers.google.com |
| Microsoft | microsoft.com | careers.microsoft.com |
| Amazon | amazon.jobs | amazon.jobs |
| Zoho | zoho.com | careers.zohocorp.com |

### Advantages

- Offline verification
- Deterministic
- Faster than web search
- Reproducible experiments
- Easily expandable

---

## 3.3.3 Official Domain Matching

### Objective

Compare the internship URL with the company's official domain.

Example

Official

google.com

↓

Match

↓

100

Fake

google-careers-job.com

↓

Mismatch

↓

20

### Output

Domain Match Score

---

## 3.3.4 Career Portal Verification

### Objective

Determine whether the internship is hosted on the official recruitment portal.

Examples

Official

careers.google.com

amazon.jobs

careers.microsoft.com

Official Company Website

google.com

zoho.com

Suspicious

google-careers-job.com

amazon-job-online.org

Output

Career Verification Score

Scoring

Official Career Portal

100

Official Company Website

70

Unknown Website

0

---

## 3.3.5 Company Trust Score

### Objective

Combine all company verification modules into one explainable trust score.

The score integrates:

- Registry Verification
- Domain Matching
- Career Portal Verification

---

# Weight Design

| Component | Weight |
|-----------|---------|
| Registry Verification | 20% |
| Official Domain Matching | 40% |
| Career Portal Verification | 40% |

Total

100%

---

# Final Formula

Company Trust Score

=

Registry Score

+

Domain Score

+

Career Score

---

# Example

## Official Career Portal

Company

Google

URL

https://careers.google.com/jobs

Result

Registry

20

Domain

40

Career

40

Company Trust Score

100

---

## Official Website

Company

Google

URL

https://google.com

Registry

20

Domain

40

Career

28

Company Trust Score

88

---

## Fake Website

Company

Google

URL

https://google-careers-job.com

Registry

20

Domain

0

Career

0

Company Trust Score

20

---

# Why Company Registry Instead of Search Engines?

Originally, the system considered using search engines such as DuckDuckGo to discover official company websites.

This approach was rejected because search results are dynamic, depend on ranking algorithms, require internet access, and cannot guarantee reproducible research experiments.

The Company Registry provides a deterministic reference database that ensures every experiment produces identical results while eliminating dependency on third-party search services.

---

# Advantages of the Proposed Design

- Fully reproducible
- Offline capable
- Faster execution
- Independent of search engines
- Easily maintainable
- Suitable for academic research
- Scalable for thousands of companies

---

# Current Status

Completed

Modules Implemented

- Company Name Extraction
- Company Registry
- Official Domain Matching
- Career Portal Verification
- Company Trust Score

Signal Status

Completed

Output

Company Trust Score (0–100)

Version

YEScape 2.0