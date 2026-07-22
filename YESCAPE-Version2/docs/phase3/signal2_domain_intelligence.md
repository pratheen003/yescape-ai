# Signal 2 — Domain Intelligence

## Objective

Evaluate the trustworthiness of the company website associated with an internship offer.

Unlike traditional fake job detectors that analyze only textual content, Domain Intelligence validates whether the claimed company website demonstrates characteristics of a legitimate online presence.

The signal contributes one of the five independent trust scores used by the YEScape Fusion Engine.

---

# Input

Company Website URL

Example

```
https://company.com
```

---

# Output

```
Domain Trust Score

0–100
```

---

# Verification Components

## 1. Domain Age

Source

WHOIS

Purpose

Older domains generally indicate greater legitimacy than newly registered domains.

Output

Age in years

---

## 2. Registrar Information

Source

WHOIS

Purpose

Identify whether the domain was registered through a reputable registrar.

Output

Registrar name

---

## 3. HTTPS Availability

Source

SSL Certificate Check

Purpose

Verify whether secure HTTPS communication is enabled.

Output

Available

Not Available

---

## 4. Google Safe Browsing

Source

Google Safe Browsing API

Purpose

Detect whether Google has flagged the website for malware, phishing, or unsafe content.

Output

Safe

Unsafe

---

## 5. Suspicious Top-Level Domain

Source

Internal Rule Engine

Purpose

Identify domains commonly abused in scams.

Examples

.xyz

.top

.click

.gq

.ml

Output

Low Risk

Medium Risk

High Risk

---

## 6. DNS Resolution

Source

DNS Lookup

Purpose

Verify whether the website currently resolves to a valid server.

Output

Valid

Invalid

---

# Final Output

Each verification contributes to an overall Domain Trust Score.

```
0
↓

High Risk

100
↓

Highly Trusted
```

---

# Role Inside YEScape

Signal 2 operates independently from all other signals.

Its output becomes one input for the Fusion Engine during Phase 4.

---

# Status

Documentation Completed

Implementation Pending

---

## WHOIS Trust Scoring

The WHOIS module converts raw registration metadata into a normalized trust score.

### Scoring Rules

| Feature | Maximum Score |
|----------|--------------:|
| Domain Age | 40 |
| Registrar Reputation | 20 |
| Expiration Period | 20 |
| Name Servers | 10 |
| Country Information | 10 |

Maximum WHOIS Trust Score: **100**

This score is passed to the Domain Intelligence module, where it will later be combined with DNS, HTTPS, Safe Browsing, and TLD verification to generate the final Domain Trust Score.

---

# DNS Verification

## Objective

Verify that the company's domain is active and correctly configured.

DNS verification ensures that the website is not merely registered but also operational.

---

## Checks Performed

### A Record

Verify whether the domain resolves to an IPv4 address.

Maximum Score

40

---

### MX Record

Verify whether the company can receive emails.

Maximum Score

30

---

### NS Record

Verify that authoritative name servers exist.

Maximum Score

20

---

### DNS Response

Verify that DNS lookup succeeds without errors.

Maximum Score

10

---

Maximum DNS Trust Score

100

---

# HTTPS Verification

## Objective

Verify whether the internship website uses a secure HTTPS connection with a valid SSL certificate.

HTTPS verification increases confidence that the organization follows modern security practices.

---

## Checks Performed

### HTTPS Availability

Verify that the website supports HTTPS.

Maximum Score

30

---

### SSL Certificate Validation

Verify that the SSL certificate is valid.

Maximum Score

30

---

### Certificate Expiry

Verify that the certificate has not expired.

Maximum Score

20

---

### Trusted Certificate Authority

Verify that the certificate issuer is a trusted Certificate Authority.

Maximum Score

10

---

### TLS Handshake

Verify that a secure TLS connection can be established.

Maximum Score

10

---

Maximum HTTPS Trust Score

100

---

# Google Safe Browsing Verification

## Objective

Verify whether the internship website has been reported by Google Safe Browsing.

Google maintains one of the world's largest malicious website databases.

---

## Threat Types

The module checks for

- Malware
- Phishing
- Social Engineering
- Unwanted Software

---

## Output

Safe Browsing Score

0–100

---

## Scoring

Safe

100

Threat Detected

0

---

This score becomes one of the Domain Intelligence signals.

---

# Domain Trust Fusion

## Objective

Combine all Domain Intelligence signals into one unified trust score.

---

## Input Signals

- WHOIS Score
- DNS Score
- HTTPS Score
- Safe Browsing Score

---

## Output

Domain Trust Score

Range

0–100

---

## Current Weight Distribution

WHOIS

30%

DNS

20%

HTTPS

20%

Google Safe Browsing

30%

---

The Domain Trust Score becomes one input to the YESScore Fusion Engine.