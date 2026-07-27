"""
YEScape 2.0

Offer Data Schema

Phase 4.2.1
"""

from dataclasses import dataclass


@dataclass
class OfferData:

    company: str = ""

    recruiter_email: str = ""

    website: str = ""

    salary: int = 0

    offer_text: str = ""

    contact_email: str = ""

    phone_number: str = ""

    job_role: str = ""

    internship_duration: str = ""

    location: str = ""

    pdf_metadata: dict = None