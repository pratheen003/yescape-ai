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