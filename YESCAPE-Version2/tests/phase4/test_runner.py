from pathlib import Path

from core.verification_engine import VerificationEngine
from schemas.verification_request import VerificationRequest

engine = VerificationEngine()


def run_test(file_path, company, email, website):

    print("=" * 70)
    print(f"TEST CASE : {Path(file_path).stem}")
    print("=" * 70)

    offer_text = Path(file_path).read_text(encoding="utf-8")

    request = VerificationRequest(

        company=company,

        recruiter_email=email,

        website=website,

        offer_text=offer_text

    )

    result = engine.verify(request)

    print(f"Final Score : {result.final_score}")
    print(f"Risk Level  : {result.risk_level}")
    print(f"Confidence  : {result.confidence}%")

    print("\nReasons")

    for reason in result.reasons:

        print(reason)

    print("\n")


if __name__ == "__main__":

    run_test(

        "tests/phase4/test_cases/genuine_google.txt",

        "Google",

        "hr@google.com",

        "careers.google.com"

    )

    run_test(

        "tests/phase4/test_cases/fake_google.txt",

        "Google",

        "googlejobsrecruitment@gmail.com",

        "google-careers-job.net"

    )

    run_test(

        "tests/phase4/test_cases/unknown_company.txt",

        "ABC Technologies",

        "careers@abctechnologies.in",

        "abctechnologies.in"

    )