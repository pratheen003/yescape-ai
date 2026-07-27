"""
YEScape 2.0

Verification Request Schema

Phase 4.1.1
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class VerificationRequest:
    """
    Input object passed to the Verification Engine.
    """

    company: Optional[str] = None

    recruiter_email: Optional[str] = None

    website: Optional[str] = None

    offer_text: Optional[str] = None

    pdf_path: Optional[str] = None