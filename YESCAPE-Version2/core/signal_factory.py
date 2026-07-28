"""
YEScape 2.0

Signal Factory

Phase 4.2.9
"""

from signals.signal1_offer.offer_engine import OfferAnalysisEngine
from signals.signal2_domain.domain_score import DomainTrustScore
from signals.signal3_company.company_score import CompanyScore
from signals.signal4_recruiter.recruiter_score import RecruiterTrustScore
from signals.signal5_context.context_score import ContextTrustScore


class SignalFactory:

    @staticmethod
    def create():

        return {

            "offer": OfferAnalysisEngine(),

            "domain": DomainTrustScore(),

            "company": CompanyScore(),

            "recruiter": RecruiterTrustScore(),

            "context": ContextTrustScore()

        }