from core.pipeline.pipeline import VerificationPipeline
from schemas.verification_request import VerificationRequest


pipeline = VerificationPipeline()

request = VerificationRequest(

    company="Google",

    recruiter_email="hr@google.com",

    website="careers.google.com",

    offer_text="""
    Congratulations.

    You have been selected.

    Visit

    https://careers.google.com

    Monthly stipend ₹25000.

    Contact

    hr@google.com
    """

)

result = pipeline.execute(request)

print()

print("Pipeline Executed Successfully")

print()

print(result.final_score)

print(result.risk_level)