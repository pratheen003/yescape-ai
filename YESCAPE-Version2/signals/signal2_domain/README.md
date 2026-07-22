# Signal 2 — WHOIS Module

## Purpose

Retrieve public registration information about a company's domain.

WHOIS data provides evidence regarding the legitimacy and maturity of a website.

Older domains are generally more trustworthy than recently registered domains.

---

## Inputs

Company Domain

Example

```
google.com
```

---

## Outputs

- Registrar
- Creation Date
- Expiration Date
- Domain Age
- Country
- Name Servers

---

## Usage

```python
checker = WhoisChecker()

result = checker.extract_information("google.com")
```

---

## Current Status

Phase 3.2.3 Completed

Next

DNS Verification

---

## DNS Module

Purpose

Verify that the domain is technically operational.

Checks

- A Record
- MX Record
- NS Record
- DNS Lookup Success

Output

DNS Trust Score

0–100

Status

Phase 3.2.4 Completed

---

## HTTPS Verification Module

Purpose

Verify that the internship website uses a valid HTTPS connection.

Checks

- HTTPS Availability
- SSL Certificate
- Certificate Expiry
- Trusted Certificate Authority
- TLS Handshake

Output

HTTPS Trust Score

0–100

Status

Phase 3.2.5 Completed

---

## Google Safe Browsing Module

Purpose

Verify whether a website has been reported by Google as malicious.

Threat Categories

- Malware
- Phishing
- Social Engineering
- Unwanted Software

Output

Safe Browsing Score

0–100

Status

Phase 3.2.6 Completed

---

## Domain Trust Fusion

Purpose

Combine all Domain Intelligence modules into one score.

Signals

- WHOIS
- DNS
- HTTPS
- Google Safe Browsing

Output

Domain Trust Score

0–100

Status

Phase 3.2.7 Completed