"""
YEScape 2.0

Signal 1

Offer Analysis Engine

Phase 4.2.4
"""

from signals.signal1_offer.offer_parser import OfferParser


class OfferAnalysisEngine:

    def __init__(self):

        self.parser = OfferParser()

    def analyze(self, offer_text):

        offer = self.parser.parse(offer_text)

        confidence = self.calculate_confidence(offer)

        return {

            "offer_data": offer,

            "confidence": confidence,

            "fields_found": {

                "company": bool(offer.company),

                "website": bool(offer.website),

                "email": bool(offer.recruiter_email),

                "salary": offer.salary > 0

            }

        }

    def calculate_confidence(self, offer):

        score = 0

        if offer.company:
            score += 25

        if offer.website:
            score += 25

        if offer.recruiter_email:
            score += 25

        if offer.salary > 0:
            score += 25

        return score