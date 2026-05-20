import re
from urllib.parse import urlparse


def analyze_domain(url):

    result={

    "score":0,

    "positives":[],

    "negatives":[]

    }


    if not url:

        return result


    try:

        domain=urlparse(
        url
        ).netloc.lower()


        trusted_domains=[

        ".com",
        ".org",
        ".edu",
        ".in"

        ]


        if any(
        domain.endswith(x)

        for x in trusted_domains):

            result["score"]+=10

            result["positives"].append(
            "Valid company domain format"
            )


        if "free" in domain:

            result["negatives"].append(
            "Suspicious domain naming"
            )

            result["score"]-=15


    except:

        result["negatives"].append(
        "Domain parsing failed"
        )


    return result