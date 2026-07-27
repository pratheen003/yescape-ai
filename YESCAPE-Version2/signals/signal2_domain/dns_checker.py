"""
YEScape 2.0

Signal 2

DNS Verification

Phase 3.2.4
"""

import dns.resolver


class DNSChecker:

    def __init__(self):
        pass

    def calculate_dns_score(

        self,

        a_records,

        mx_records,

        ns_records,

        lookup_success

    ):

        score = 0

        # A Record

        if len(a_records) > 0:
            score += 40

        # MX Record

        if len(mx_records) > 0:
            score += 30

        # NS Record

        if len(ns_records) > 0:
            score += 20

        # Lookup Success

        if lookup_success:
            score += 10

        return score

    def lookup(self, domain):

        result = {

            "domain": domain,

            "a_records": [],

            "mx_records": [],

            "ns_records": [],

            "lookup_success": False,

            "dns_score": 0

        }

        try:

            # A Records

            answers = dns.resolver.resolve(domain, "A")

            result["a_records"] = [

                str(r) for r in answers

            ]

            # MX Records

            answers = dns.resolver.resolve(domain, "MX")

            result["mx_records"] = [

                str(r.exchange)

                for r in answers

            ]

            # NS Records

            answers = dns.resolver.resolve(domain, "NS")

            result["ns_records"] = [

                str(r.target)

                for r in answers

            ]

            result["lookup_success"] = True

        except Exception as e:

            print("DNS lookup failed.")

        result["dns_score"] = self.calculate_dns_score(

            result["a_records"],

            result["mx_records"],

            result["ns_records"],

            result["lookup_success"]

        )

        return result


if __name__ == "__main__":

    checker = DNSChecker()

    print(checker.lookup("google.com"))