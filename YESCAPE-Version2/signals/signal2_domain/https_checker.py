"""
YEScape 2.0

Signal 2

HTTPS Verification

Phase 3.2.5
"""

import socket
import ssl
from datetime import datetime

from utils.url_utils import URLUtils


class HTTPSChecker:

    def __init__(self):
        pass

    def calculate_https_score(

        self,

        https_available,

        ssl_valid,

        not_expired,

        trusted_issuer,

        handshake_success

    ):

        score = 0

        if https_available:
            score += 30

        if ssl_valid:
            score += 30

        if not_expired:
            score += 20

        if trusted_issuer:
            score += 10

        if handshake_success:
            score += 10

        return min(score, 100)

    def check_https(self, url):

        domain = URLUtils.normalize(url)

        result = {

            "domain": domain,

            "https_available": False,

            "ssl_valid": False,

            "certificate_expiry": None,

            "issuer": None,

            "trusted_issuer": False,

            "handshake_success": False,

            "https_score": 0

        }

        try:

            context = ssl.create_default_context()

            with socket.create_connection((domain, 443), timeout=5) as sock:

                with context.wrap_socket(sock, server_hostname=domain) as ssock:

                    cert = ssock.getpeercert()

                    result["https_available"] = True
                    result["ssl_valid"] = True
                    result["handshake_success"] = True

                    issuer = cert.get("issuer", [])

                    issuer_text = ", ".join(
                        "=".join(x) for part in issuer for x in part
                    )

                    result["issuer"] = issuer_text

                    expiry = cert["notAfter"]

                    expiry_date = datetime.strptime(
                        expiry,
                        "%b %d %H:%M:%S %Y %Z"
                    )

                    result["certificate_expiry"] = expiry_date

                    if expiry_date > datetime.utcnow():

                        not_expired = True

                    else:

                        not_expired = False

                    trusted_keywords = [

                        "Google",

                        "Let's Encrypt",

                        "DigiCert",

                        "Sectigo",

                        "GlobalSign",

                        "Amazon",

                        "Microsoft",

                        "Cloudflare"

                    ]

                    trusted = any(

                        keyword.lower() in issuer_text.lower()

                        for keyword in trusted_keywords

                    )

                    result["trusted_issuer"] = trusted

                    result["https_score"] = self.calculate_https_score(

                        result["https_available"],

                        result["ssl_valid"],

                        not_expired,

                        trusted,

                        result["handshake_success"]

                    )

        except Exception as e:

            print("HTTPS connection failed.")

        return result


if __name__ == "__main__":

    checker = HTTPSChecker()

    test_urls = [

        "google.com",

        "amazon.jobs",

        "microsoft.com"

    ]

    for url in test_urls:

        print("\nInput :", url)

        result = checker.check_https(url)

        print(result)