"""
YEScape 2.0

Signal 4

Recruiter Trust Score

Phase 3.4.6
"""

from signals.signal4_recruiter.email_parser import EmailParser
from signals.signal4_recruiter.email_domain import EmailDomainVerifier
from signals.signal4_recruiter.company_email_match import CompanyEmailMatcher
from signals.signal4_recruiter.free_email_checker import FreeEmailChecker


class RecruiterTrustScore:

    def __init__(self):

        self.parser = EmailParser()
        self.domain = EmailDomainVerifier()
        self.matcher = CompanyEmailMatcher()
        self.free = FreeEmailChecker()

    def calculate(self, company_name, recruiter_email):

        parsed = self.parser.parse(recruiter_email)

        if parsed is None:

            return {

                "company": company_name,

                "email": recruiter_email,

                "recruiter_trust_score": 0,

                "reason": "Invalid Email"

            }

        domain = parsed["domain"]

        domain_result = self.domain.verify(domain)

        match_result = self.matcher.verify(company_name, domain)

        free_result = self.free.check(domain)

        format_score = 100

        final_score = (

            domain_result["domain_trust_score"] * 0.35 +

            match_result["score"] * 0.35 +

            free_result["free_email_score"] * 0.20 +

            format_score * 0.10

        )

        return {

            "company": company_name,

            "email": recruiter_email,

            "domain_trust_score": domain_result["domain_trust_score"],

            "company_match_score": match_result["score"],

            "free_email_score": free_result["free_email_score"],

            "recruiter_trust_score": round(final_score, 2)

        }


if __name__ == "__main__":

    fusion = RecruiterTrustScore()

    tests = [

        ("Google", "john@google.com"),

        ("Google", "john@gmail.com"),

        ("Google", "john@yahoo.com"),

        ("Google", "john@google-careers-job.com"),

        ("Microsoft", "hr@microsoft.com"),

        ("Zoho", "careers@careers.zohocorp.com")

    ]

    for company, email in tests:

        print()

        print(fusion.calculate(company, email))