"""
YEScape 2.0

Signal 2

Domain Trust Fusion

Phase 3.2.7
"""

from signals.signal2_domain.whois_checker import WhoisChecker
from signals.signal2_domain.dns_checker import DNSChecker
from signals.signal2_domain.https_checker import HTTPSChecker
from signals.signal2_domain.safe_browsing import SafeBrowsingChecker


class DomainTrustScore:

    def __init__(self):

        self.whois = WhoisChecker()
        self.dns = DNSChecker()
        self.https = HTTPSChecker()
        self.safe = SafeBrowsingChecker()

    def calculate(self, url):

        whois_result = self.whois.extract_information(url)

        if not whois_result["success"]:

            whois_result = {

                "whois_score": 0

            }

        if whois_result is None:

            whois_result = {

                "whois_score": 0

            }

        dns_result = self.dns.lookup(url)

        if dns_result is None:

            dns_result = {

                "dns_score": 0

            }

        https_result = self.https.check_https(url)

        if https_result is None:

            https_result = {

                "https_score": 0

            }

        safe_result = self.safe.check_url(url)

        if safe_result is None:

            safe_result = {

                "safe_browsing_score": 0

            }

        final_score = (

            whois_result["whois_score"] * 0.30 +

            dns_result["dns_score"] * 0.20 +

            https_result["https_score"] * 0.20 +

            safe_result["safe_browsing_score"] * 0.30

        )

        return {

            "url": url,

            "whois_score": whois_result["whois_score"],

            "dns_score": dns_result["dns_score"],

            "https_score": https_result["https_score"],

            "safe_browsing_score": safe_result["safe_browsing_score"],

            "domain_trust_score": round(final_score,2)

        }


if __name__ == "__main__":

    fusion = DomainTrustScore()

    test_urls = [

        "google.com",

        "amazon.jobs",

        "microsoft.com"

    ]

    for url in test_urls:

        print()

        print(fusion.calculate(url))