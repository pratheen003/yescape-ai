"""
YEScape 2.0

Signal 4

Email Domain Verification

Phase 3.4.3
"""

from signals.signal2_domain.domain_score import DomainTrustScore


class EmailDomainVerifier:

    def __init__(self):

        self.domain_fusion = DomainTrustScore()

    def verify(self, email_domain):

        result = self.domain_fusion.calculate(email_domain)

        return {

            "email_domain": email_domain,

            "domain_trust_score": result["domain_trust_score"],

            "details": result

        }


if __name__ == "__main__":

    verifier = EmailDomainVerifier()

    domains = [

        "google.com",

        "gmail.com",

        "amazon.jobs",

        "yahoo.com",

        "microsoft.com"

    ]

    for domain in domains:

        print()

        print(verifier.verify(domain))