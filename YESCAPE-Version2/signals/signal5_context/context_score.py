"""
YEScape 2.0

Signal 5

Context Trust Score

Phase 3.5.7
"""

from signals.signal5_context.scam_keywords import ScamKeywordDetector
from signals.signal5_context.urgency_detector import UrgencyDetector
from signals.signal5_context.advance_fee_detector import AdvanceFeeDetector
from signals.signal5_context.salary_validator import SalaryValidator
from signals.signal5_context.contact_validator import ContactValidator
from signals.signal5_context.grammar_checker import GrammarChecker
from config.config import *


class ContextTrustScore:

    def __init__(self):

        self.scam = ScamKeywordDetector()
        self.urgency = UrgencyDetector()
        self.fee = AdvanceFeeDetector()
        self.salary = SalaryValidator()
        self.contact = ContactValidator()
        self.grammar = GrammarChecker()

    def calculate(self, text):

        scam = self.scam.analyze(text)

        urgency = self.urgency.analyze(text)

        fee = self.fee.analyze(text)

        salary = self.salary.analyze(text)

        contact = self.contact.analyze(text)

        grammar = self.grammar.analyze(text)

        final_score = (

            scam["scam_keyword_score"] * SCAM_KEYWORD_WEIGHT +

            urgency["urgency_score"] * URGENCY_WEIGHT +

            fee["advance_fee_score"] * ADVANCE_FEE_WEIGHT +

            salary["salary_score"] * SALARY_WEIGHT +

            contact["contact_score"] * CONTACT_WEIGHT +

            grammar["grammar_score"] * GRAMMAR_WEIGHT

        )

        return {

            "scam_keyword_score": scam["scam_keyword_score"],

            "urgency_score": urgency["urgency_score"],

            "advance_fee_score": fee["advance_fee_score"],

            "salary_score": salary["salary_score"],

            "contact_score": contact["contact_score"],

            "grammar_score": grammar["grammar_score"],

            "context_trust_score": round(final_score, 2)

        }


if __name__ == "__main__":

    fusion = ContextTrustScore()

    samples = [

        """
        Google Internship

        Visit careers.google.com

        Contact:

        hr@google.com

        +91 9876543210

        Stipend ₹20000 per month

        No registration fee required.
        """,

        """
        Congratulations Candidate!!!

        Hurry!!

        Offer expires today!!

        Pay registration fee immediately.

        Transfer money through UPI.

        Earn ₹100000 per month.

        Reply now.
        """

    ]

    for sample in samples:

        print()

        print(fusion.calculate(sample))