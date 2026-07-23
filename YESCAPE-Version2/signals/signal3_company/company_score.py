"""
YEScape 2.0

Signal 3

Company Trust Score

Phase 3.3.5
"""

from signals.signal3_company.registry_loader import CompanyRegistry
from signals.signal3_company.domain_match import DomainMatcher
from signals.signal3_company.career_match import CareerMatcher


class CompanyScore:

    def __init__(self):

        self.registry = CompanyRegistry()
        self.domain = DomainMatcher()
        self.career = CareerMatcher()

    def calculate(self, company_name, internship_url):

        registry = self.registry.get_company(company_name)

        registry_score = 20 if registry else 0

        domain_result = self.domain.calculate(
            company_name,
            internship_url
        )

        career_result = self.career.verify(
            company_name,
            internship_url
        )

        # Domain contribution (40)
        if domain_result["match"]:
            domain_score = 40
        else:
            domain_score = 0

        # Career contribution (40)
        career_score = (career_result["career_score"] / 100) * 40

        total = registry_score + domain_score + career_score

        return {

            "company": company_name,

            "registry_score": registry_score,

            "domain_score": domain_score,

            "career_score": round(career_score,2),

            "company_trust_score": round(total,2)

        }


if __name__ == "__main__":

    scorer = CompanyScore()

    tests = [

        ("Google","https://careers.google.com/jobs"),

        ("Google","https://google.com"),

        ("Google","https://google-careers-job.com"),

        ("Zoho","https://careers.zohocorp.com"),

        ("Zoho","https://zoho.com"),

        ("Zoho","https://zoho-jobs.org")

    ]

    for company,url in tests:

        print()

        print(scorer.calculate(company,url))