"""
YEScape 2.0

Score Fusion Engine

Phase 4.3.3
"""

from config.fusion_weights import FUSION_WEIGHTS


class ScoreFusion:

    def __init__(self):

        self.weights = FUSION_WEIGHTS

    def calculate(

        self,

        offer,

        domain,

        company,

        recruiter,

        context

    ):
        

        final_score = (

            offer * self.weights["offer"] +

            domain * self.weights["domain"] +

            company * self.weights["company"] +

            recruiter * self.weights["recruiter"] +

            context * self.weights["context"]

        )

        return round(final_score, 2)

    def classify(self, final_score):

        if final_score >= 85:

            return {

                "risk_level": "SAFE",

                "risk_color": "GREEN"

            }

        elif final_score >= 60:

            return {

                "risk_level": "CAUTION",

                "risk_color": "YELLOW"

            }

        else:

            return {

                "risk_level": "HIGH RISK",

                "risk_color": "RED"

            }

    def confidence(self, offer_result):

        offer = offer_result["offer_data"]

        fields = [

            offer.company,

            offer.website,

            offer.contact_email,

            offer.salary

        ]

        available = sum(

            value not in [None, "", 0]

            for value in fields

        )

        confidence = (available / len(fields)) * 100

        return round(confidence, 2)

    def reasons(

        self,

        offer,

        domain,

        company,

        recruiter,

        context

    ):

        reasons = []

        # -----------------------
        # Offer
        # -----------------------

        if offer["confidence"] >= 75:

            reasons.append("Offer contains sufficient information.")

        else:

            reasons.append("Offer is missing important information.")

        # -----------------------
        # Domain
        # -----------------------

        if domain["domain_trust_score"] >= 80:

            reasons.append("Website domain appears trustworthy.")

        else:

            reasons.append("Website domain appears suspicious.")

        # -----------------------
        # Company
        # -----------------------

        if company["company_trust_score"] >= 80:

            reasons.append("Company verified in registry.")

        else:

            reasons.append("Company verification is weak.")

        # -----------------------
        # Recruiter
        # -----------------------

        if recruiter["recruiter_trust_score"] >= 80:

            reasons.append("Recruiter email is trustworthy.")

        else:

            reasons.append("Recruiter email is suspicious.")

        # -----------------------
        # Context
        # -----------------------

        if context["context_trust_score"] >= 80:

            reasons.append("Offer content appears legitimate.")

        else:

            reasons.append("Offer content contains suspicious indicators.")

        return reasons


if __name__ == "__main__":

    fusion = ScoreFusion()

    offer = {

        "company": "Google",

        "website": "https://careers.google.com",

        "email": "hr@google.com",

        "salary": 25000,

        "confidence": 100

    }

    domain = {

        "domain_trust_score": 80

    }

    company = {

        "company_trust_score": 100

    }

    recruiter = {

        "recruiter_trust_score": 100

    }

    context = {

        "context_trust_score": 94

    }

    score = fusion.calculate(

        100,

        80,

        100,

        100,

        94

    )

    risk = fusion.classify(score)

    confidence = fusion.confidence(offer)

    reasons = fusion.reasons(

        offer,

        domain,

        company,

        recruiter,

        context

    )

    print()

    print("Final Score :", score)

    print("Risk Level  :", risk["risk_level"])

    print("Color       :", risk["risk_color"])

    print("Confidence  :", confidence)

    print()

    print("Reasons")

    print("-" * 30)

    for reason in reasons:

        print("✓", reason)