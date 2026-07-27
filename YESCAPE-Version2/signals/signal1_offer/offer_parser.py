"""
YEScape 2.0

Signal 1

Offer Parser

Phase 4.2.2
"""

import re

from schemas.offer_data import OfferData
from signals.signal3_company.registry_loader import CompanyRegistry


class OfferParser:

    def __init__(self):

        self.registry = CompanyRegistry()

    def parse(self, text: str):

        offer = OfferData()

        offer.offer_text = text

        # --------------------------
        # Email
        # --------------------------

        email = re.search(

            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",

            text

        )

        if email:

            offer.recruiter_email = email.group()

            offer.contact_email = email.group()

        # --------------------------
        # Website
        # --------------------------

        # --------------------------
        # Website
        # --------------------------

        websites = re.findall(

            r"(https?://[^\s]+|www\.[^\s]+|[A-Za-z0-9.-]+\.(?:com|org|net|jobs|in))",

            text,

            re.IGNORECASE

        )

        if websites:

            websites = sorted(

                websites,

                key=len,

                reverse=True

            )

            offer.website = websites[0]

        # --------------------------
        # Salary
        # --------------------------

        salary = re.search(

            r"(₹|\$)?\s?([0-9]{4,7})",

            text

        )

        if salary:

            offer.salary = int(salary.group(2))

        # --------------------------
        # Company
        # --------------------------

        for company in self.registry.registry["company"]:

            if company.lower() in text.lower():

                offer.company = company

                break

        return offer