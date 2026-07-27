"""
YEScape 2.0

Verification Engine

Phase 4.1.4
"""

from schemas.verification_request import VerificationRequest
from schemas.verification_result import VerificationResult
from schemas.signal_result import SignalResult
from signals.signal5_context.context_score import ContextTrustScore
from signals.signal2_domain.domain_score import DomainTrustScore
from signals.signal3_company.company_score import CompanyScore
from signals.signal4_recruiter.recruiter_score import RecruiterTrustScore


class VerificationEngine:

    def __init__(self):

        self.context = ContextTrustScore()

        self.domain = DomainTrustScore()

        self.company = CompanyScore()

        self.recruiter = RecruiterTrustScore()

    def verify(self, request: VerificationRequest):

        """
        Execute the complete verification pipeline.
        """

        result = VerificationResult()

        signal_results = []

        # --------------------------------------------------
        # Signal 1
        # --------------------------------------------------
        # Reserved for Phase 4.2
        # Offer Letter Analysis Engine

        # --------------------------------------------------
        # Signal 2
        # --------------------------------------------------

        domain_result = self.domain.calculate(

            request.website or ""

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

            request.company or "",

            request.website or ""

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

            request.recruiter_email or ""

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