"""
Phase 4

Verification Engine Test
"""

from core.verification_engine import VerificationEngine
from schemas.verification_request import VerificationRequest


engine = VerificationEngine()

request = VerificationRequest(

    company="Google",

    recruiter_email="hr@google.com",

    website="careers.google.com",

    offer_text="""
    Congratulations.

    You have been selected for Google's Internship Program.

    Official Careers Website:

    https://careers.google.com

    No application fee is required.

    Monthly stipend is ₹25000.

    Recruiter:

    hr@google.com
    """

)

result = engine.verify(request)

print()

print("=" * 60)
print("YESCAPE FINAL VERIFICATION REPORT")
print("=" * 60)

print()

print(f"Final Trust Score : {result.final_score}")

print(f"Risk Level        : {result.risk_level}")

print(f"Confidence        : {result.confidence}%")

print()

print("Reasons")

print("-" * 30)

for reason in result.reasons:

    print("✓", reason)

print()

print("=" * 60)

print("SIGNAL BREAKDOWN")

print("=" * 60)

print()

for signal in result.signals:

    print(f"Signal : {signal.signal_name}")

    print(f"Score  : {signal.score}")

    print(f"Reason : {signal.reason}")

    print("Details:")

    print(signal.details)

    print("-" * 50)