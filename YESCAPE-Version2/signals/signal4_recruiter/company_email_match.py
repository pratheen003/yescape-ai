"""
YEScape 2.0

Signal 4

Company Email Matching

Phase 3.4.4
"""

from signals.signal3_company.registry_loader import CompanyRegistry


class CompanyEmailMatcher:

    def __init__(self):

        self.registry = CompanyRegistry()

    def verify(self, company_name, email_domain):

        company = self.registry.get_company(company_name)

        if company is None:

            return {

                "company": company_name,

                "email_domain": email_domain,

                "match": False,

                "score": 0,

                "reason": "Company Not Found"

            }

        official = company["official_domain"]

        career = company["career_domain"]

        if email_domain == official:

            return {

                "company": company_name,

                "email_domain": email_domain,

                "match": True,

                "score": 100,

                "reason": "Official Company Domain"

            }

        if email_domain == career:

            return {

                "company": company_name,

                "email_domain": email_domain,

                "match": True,

                "score": 100,

                "reason": "Official Career Domain"

            }

        return {

            "company": company_name,

            "email_domain": email_domain,

            "match": False,

            "score": 0,

            "reason": "Email Domain Does Not Match Company"

        }


if __name__ == "__main__":

    matcher = CompanyEmailMatcher()

    tests = [

        ("Google", "google.com"),

        ("Google", "careers.google.com"),

        ("Google", "gmail.com"),

        ("Google", "google-careers-job.com"),

        ("Microsoft", "microsoft.com"),

        ("Zoho", "careers.zohocorp.com"),

        ("Zoho", "gmail.com")

    ]

    for company, domain in tests:

        print()

        print(matcher.verify(company, domain))