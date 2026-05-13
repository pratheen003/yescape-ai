import whois
from urllib.parse import urlparse
import requests


def analyze_website(url):

    results = {
        "domain_age_days": None,
        "https": False,
        "suspicious_email": False,
        "penalties": [],
        "score_penalty": 0
    }

    try:

        # HTTPS Check
        if url.startswith("https://"):
            results["https"] = True
        else:
            results["penalties"].append("Website is not using HTTPS")
            results["score_penalty"] += 10

        # Domain Info
        domain = urlparse(url).netloc

        domain_info = whois.whois(domain)

        creation_date = domain_info.creation_date

        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        if creation_date:

            from datetime import datetime

            from datetime import datetime, timezone

            creation_date = creation_date.replace(tzinfo=None)

            age = (
                 datetime.now() - creation_date
            ).days

            results["domain_age_days"] = age

            if age < 180:
                results["penalties"].append(
                    "Domain is less than 6 months old"
                )
                results["score_penalty"] += 25

        # Website Reachability Check
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            results["penalties"].append(
                "Website appears unreliable"
            )
            results["score_penalty"] += 10

    except Exception as e:

        results["penalties"].append(
            f"Website analysis failed: {str(e)}"
        )

        results["score_penalty"] += 15

    return results