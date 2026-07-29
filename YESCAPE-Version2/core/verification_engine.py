"""
YEScape 2.0

Verification Engine

Phase 4.1.4
"""

from schemas.verification_request import VerificationRequest
from schemas.verification_result import VerificationResult
from schemas.signal_result import SignalResult
from core.signal_factory import SignalFactory
from core.fusion.score_fusion import ScoreFusion


class VerificationEngine:

    def __init__(self):

        signals = SignalFactory.create()

        self.offer = signals["offer"]

        self.domain = signals["domain"]

        self.company = signals["company"]

        self.recruiter = signals["recruiter"]

        self.context = signals["context"]

        self.fusion = ScoreFusion()

    def safe_execute(self, function, *args):
        """
        Execute a signal safely.

        Returns:
            (success, result)
        """

        try:

            return True, function(*args)

        except Exception as e:

            return False, str(e)

    def verify(self, request: VerificationRequest):

        """
        Execute the complete verification pipeline.
        """

        result = VerificationResult()

        signal_results = []

        # --------------------------------------------------
        # Signal 1
        # --------------------------------------------------

        offer_success, offer_result = self.safe_execute(

            self.offer.analyze,

            request.offer_text or ""

        )

        if not offer_success:

            offer_result = {

                "confidence": 0,

                "offer_data": None

            }

            offer = None

        else:

            offer = offer_result["offer_data"]

        if offer_success:

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

        else:

            signal_results.append(

                SignalResult(

                    signal_name="Offer Letter Analysis",

                    score=0,

                    success=False,

                    reason="Offer Analysis Failed",

                    details={

                        "error": "Offer Parser Exception"

                    }

                )

            )

        # --------------------------------------------------
        # Signal 2
        # --------------------------------------------------

        domain_success, domain_result = self.safe_execute(

            self.domain.calculate,

            offer.website if offer else ""

        )

        if not domain_success:

            domain_result = {

                "domain_trust_score": 0

            }

        signal_results.append(

            SignalResult(

                signal_name="Domain Verification",

                score=domain_result["domain_trust_score"],

                success=domain_success,

                reason=(
                    "Domain Verification Completed"
                    if domain_success
                    else "Domain Verification Failed"
                ),

                details=domain_result

            )

        )

        # --------------------------------------------------
        # Signal 3
        # --------------------------------------------------

        company_success, company_result = self.safe_execute(

            self.company.calculate,

            offer.company if offer else "",

            offer.website if offer else ""

        )

        if not company_success:

            company_result = {

                "company_trust_score": 0

            }

        signal_results.append(

            SignalResult(

                signal_name="Company Verification",

                score=company_result["company_trust_score"],

                success=company_success,

                reason=(
                    "Company Verification Completed"
                    if company_success
                    else "Company Verification Failed"
                ),

                details=company_result

            )

        )

        # --------------------------------------------------
        # Signal 4
        # --------------------------------------------------

        recruiter_success, recruiter_result = self.safe_execute(

            self.recruiter.calculate,

            offer.company if offer else "",

            offer.recruiter_email if offer else ""

        )

        if not recruiter_success:

            recruiter_result = {

                "recruiter_trust_score": 0

            }

        signal_results.append(

            SignalResult(

                signal_name="Recruiter Verification",

                score=recruiter_result["recruiter_trust_score"],

                success=recruiter_success,

                reason=(
                    "Recruiter Verification Completed"
                    if recruiter_success
                    else "Recruiter Verification Failed"
                ),

                details=recruiter_result

            )

        )
        # --------------------------------------------------
        # Signal 5
        # --------------------------------------------------

        context_success, context_result = self.safe_execute(

            self.context.calculate,

            request.offer_text or ""

        )

        if not context_success:

            context_result = {

                "context_trust_score": 0

            }

        # -----------------------------------
        # Final Fusion
        # -----------------------------------

        final_score = self.fusion.calculate(

            offer_result["confidence"],

            domain_result["domain_trust_score"],

            company_result["company_trust_score"],

            recruiter_result["recruiter_trust_score"],

            context_result["context_trust_score"]

        )

        risk = self.fusion.classify(final_score)

        confidence = self.fusion.confidence(offer_result)

        reasons = self.fusion.reasons(

            offer_result,

            domain_result,

            company_result,

            recruiter_result,

            context_result

        )

        result.final_score = final_score

        result.risk_level = risk["risk_level"]

        result.risk_color = risk["risk_color"]

        result.confidence = confidence

        result.reasons = reasons

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