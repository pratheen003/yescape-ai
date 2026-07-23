"""
YEScape 2.0

Signal 3

Career Page Verification

Phase 3.3.4
"""

from signals.signal3_company.registry_loader import CompanyRegistry
from utils.url_utils import URLUtils


class CareerMatcher:

    def __init__(self):

        self.registry = CompanyRegistry()

    def verify(self, company_name, internship_url):

        company = self.registry.get_company(company_name)

        if company is None:

            return {

                "company": company_name,

                "career_match": False,

                "score": 0,

                "reason": "Company not found"

            }

        internship_domain = URLUtils.normalize(internship_url)

        official_domain = company["official_domain"]

        career_domain = company["career_domain"]

        # Official Career Portal

        if internship_domain == career_domain:

            score = 100

            status = "Official Career Portal"

        # Official Company Website

        elif (

            internship_domain == official_domain

            or internship_domain.endswith("." + official_domain)

        ):

            score = 70

            status = "Official Company Website"

        # Fake Website

        else:

            score = 0

            status = "Unknown / Suspicious Website"

        return {

            "company": company_name,

            "internship_domain": internship_domain,

            "career_domain": career_domain,

            "status": status,

            "career_score": score

        }


if __name__ == "__main__":

    matcher = CareerMatcher()

    tests = [

        ("Google","https://careers.google.com/jobs"),

        ("Google","https://google.com"),

        ("Google","https://google-careers-job.com"),

        ("Microsoft","https://careers.microsoft.com"),

        ("Zoho","https://careers.zohocorp.com"),

        ("Zoho","https://zoho.com")

    ]

    for company,url in tests:

        print()

        print(matcher.verify(company,url))