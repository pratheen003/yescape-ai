"""
YEScape 2.0

Signal 3

Official Domain Matching

Phase 3.3.3
"""

from signals.signal3_company.registry_loader import CompanyRegistry
from utils.url_utils import URLUtils


class DomainMatcher:

    def __init__(self):

        self.registry = CompanyRegistry()

    def calculate(self, company_name, internship_url):

        company = self.registry.get_company(company_name)

        if company is None:

            return {

                "company": company_name,

                "match": False,

                "score": 0,

                "reason": "Company not found in registry"

            }

        official_domain = company["official_domain"]

        career_domain = company["career_domain"]

        internship_domain = URLUtils.normalize(internship_url)

        match = (

            internship_domain == official_domain

            or

            internship_domain == career_domain

            or

            internship_domain.endswith("." + official_domain)

        )

        score = 100 if match else 20

        return {

            "company": company_name,

            "internship_domain": internship_domain,

            "official_domain": official_domain,

            "career_domain": career_domain,

            "match": match,

            "score": score

        }


if __name__ == "__main__":

    matcher = DomainMatcher()

    tests = [

        ("Google", "https://google.com"),

        ("Google", "https://careers.google.com/jobs"),

        ("Google", "https://google-careers-job.com"),

        ("Microsoft", "https://careers.microsoft.com"),

        ("Zoho", "https://careers.zohocorp.com"),

        ("Zoho", "https://zoho-jobs.org")

    ]

    for company, url in tests:

        print()

        print(matcher.calculate(company, url))