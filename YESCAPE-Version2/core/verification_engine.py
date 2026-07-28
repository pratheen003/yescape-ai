"""
YEScape 2.0

Verification Engine

Phase 4.1.4
"""

from schemas.verification_request import VerificationRequest
from schemas.verification_result import VerificationResult
from schemas.signal_result import SignalResult
from core.signal_factory import SignalFactory


class VerificationEngine:

    def __init__(self):

        signals = SignalFactory.create()

        self.offer = signals["offer"]

        self.domain = signals["domain"]

        self.company = signals["company"]

        self.recruiter = signals["recruiter"]

        self.context = signals["context"]

    def verify(self, request: VerificationRequest):

        """
        Execute the complete verification pipeline.
        """

        result = VerificationResult()

        signal_results = []

        # --------------------------------------------------
        # Signal 1
        # --------------------------------------------------

        offer_result = self.offer.analyze(
        
            request.offer_text or ""
        
        )
        
        offer = offer_result["offer_data"]

        signal_results.append(

            SignalResult(

                signal_name="Offer Letter Analysis",

                score=offer_result["confidence"],

                success=True,

                reason="Offer Analysis Completed",

                details={

                    "company": offer.company,

                    "website": offer.website,

                    "email": offer.recruiter_email,

                    "salary": offer.salary,

                    "confidence": offer_result["confidence"]

                }

            )

        )

        # --------------------------------------------------
        # Signal 2
        # --------------------------------------------------

        domain_result = self.domain.calculate(

            offer.website or ""

        )

        signal_results.append(

            SignalResult(

                signal_name="Domain Verification",

                score=domain_result["domain_trust_score"],

                success=True,

                reason="Domain Verification Completed",

                details=domain_result

            )

        )

        # --------------------------------------------------
        # Signal 3
        # --------------------------------------------------

        company_result = self.company.calculate(

            offer.company or "",

            offer.website or ""

        )

        signal_results.append(

            SignalResult(

                signal_name="Company Verification",

                score=company_result["company_trust_score"],

                success=True,

                reason="Company Verification Completed",

                details=company_result

            )

        )

        # --------------------------------------------------
        # Signal 4
        # --------------------------------------------------

        recruiter_result = self.recruiter.calculate(

            request.company or "",

            offer.recruiter_email or ""

        )

        signal_results.append(

            SignalResult(

                signal_name="Recruiter Verification",

                score=recruiter_result["recruiter_trust_score"],

                success=True,

                reason="Recruiter Verification Completed",

                details=recruiter_result

            )

        )
        # --------------------------------------------------
        # Signal 5
        # --------------------------------------------------

        context_result = self.context.calculate(

            request.offer_text or ""

        )

        signal_results.append(

            SignalResult(

                signal_name="Context Analysis",

                score=context_result["context_trust_score"],

                success=True,

                reason="Context Verification Completed",

                details=context_result

            )

        )

        result.signals = signal_results

        return result