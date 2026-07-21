"""
YEScape 2.0

Signal 2
WHOIS Checker

Phase 3.2.3
"""

import whois
from datetime import datetime, timezone


class WhoisChecker:

    def __init__(self):
        pass

    def get_domain_information(self, domain):

        try:

            info = whois.whois(domain)

            return info

        except Exception as e:

            print("WHOIS Error:", e)

            return None
        
    def calculate_whois_score(
        self,
        domain_age,
        registrar,
        expiration_date,
        country,
        name_servers
    ):
        """
        Calculate WHOIS Trust Score (0–100)
        """

        score = 0

        # ------------------------
        # Domain Age
        # ------------------------

        if domain_age is not None:

            if domain_age >= 10:
                score += 40

            elif domain_age >= 5:
                score += 30

            elif domain_age >= 2:
                score += 20

            elif domain_age >= 1:
                score += 10

        # ------------------------
        # Trusted Registrar
        # ------------------------

        trusted_registrars = [

            "MarkMonitor",

            "GoDaddy",

            "Namecheap",

            "Google",

            "Cloudflare",

            "Tucows",

            "Network Solutions"

        ]

        if registrar:

            if any(r.lower() in registrar.lower() for r in trusted_registrars):

                score += 20

            else:

                score += 10

        # ------------------------
        # Expiration
        # ------------------------

        if expiration_date:

            if isinstance(expiration_date, list):

                expiration_date = expiration_date[0]

            if expiration_date.tzinfo is not None:

                expiration_date = expiration_date.replace(tzinfo=None)

            years_left = (expiration_date - datetime.now()).days / 365

            if years_left > 1:

                score += 20

            elif years_left > 0:

                score += 10

        # ------------------------
        # Name Servers
        # ------------------------

        if name_servers:

            if len(name_servers) >= 2:

                score += 10

            else:

                score += 5

        # ------------------------
        # Country
        # ------------------------

        if country:

            score += 10

        return min(score, 100)

    def extract_information(self, domain):

        info = self.get_domain_information(domain)

        if info is None:

            return None

        creation_date = info.creation_date
        expiration_date = info.expiration_date

        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]

        domain_age = None

        if creation_date:

            # Convert timezone-aware datetime to timezone-naive
            if creation_date.tzinfo is not None:
                creation_date = creation_date.replace(tzinfo=None)

            domain_age = (datetime.now() - creation_date).days // 365

        whois_score = self.calculate_whois_score(

            domain_age,

            info.registrar,

            expiration_date,

            info.country,

            info.name_servers

        )

        return {

            "domain": domain,

            "registrar": info.registrar,

            "creation_date": creation_date,

            "expiration_date": expiration_date,

            "domain_age": domain_age,

            "country": info.country,

            "name_servers": info.name_servers,

            "whois_score": whois_score

        }


if __name__ == "__main__":

    checker = WhoisChecker()

    result = checker.extract_information("google.com")

    print(result)