"""
YEScape 2.0

Signal 4

Free Email Detection

Phase 3.4.5
"""
from config.constants import FREE_EMAIL_DOMAINS

class FreeEmailChecker:

    def __init__(self):

        self.free_domains = FREE_EMAIL_DOMAINS

    def check(self, email_domain):

        domain = email_domain.lower().strip()

        if domain in self.free_domains:

            return {

                "email_domain": domain,

                "is_free_email": True,

                "provider": domain,

                "free_email_score": 20,

                "reason": "Public Email Provider"

            }

        return {

            "email_domain": domain,

            "is_free_email": False,

            "provider": None,

            "free_email_score": 100,

            "reason": "Corporate Email Domain"

        }


if __name__ == "__main__":

    checker = FreeEmailChecker()

    test_domains = [

        "google.com",

        "gmail.com",

        "yahoo.com",

        "microsoft.com",

        "outlook.com",

        "amazon.jobs",

        "careers.zohocorp.com"

    ]

    for domain in test_domains:

        print()

        print(checker.check(domain))