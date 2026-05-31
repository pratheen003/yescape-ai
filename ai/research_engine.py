import re


KNOWN_COMPANIES = [

    "google",
    "microsoft",
    "amazon",
    "infosys",
    "tcs",
    "wipro",
    "accenture",
    "zoho",
    "ibm",
    "cognizant",
    "hcl"

]


def analyze_domain(url):

    score = 0

    positives = []

    negatives = []

    url = url.lower().strip()


    if url == "":

        return {

            "score": 0,
            "positives": [],
            "negatives": []

        }


    # domain format

    if "." in url:

        score += 10

        positives.append(
            "Valid company domain format"
        )

    else:

        negatives.append(
            "Invalid website format"
        )


    # https

    if "https://" in url:

        score += 10

        positives.append(
            "Secure HTTPS website"
        )

    else:

        negatives.append(
            "Website not using HTTPS"
        )


    # known companies

    for company in KNOWN_COMPANIES:

        if company in url:

            score += 20

            positives.append(
                f"Recognized company mention: {company.title()}"
            )

            break


    # suspicious patterns

    suspicious = [

        "free",
        "earnfast",
        "cryptojob",
        "instantpay",
        "quickmoney"

    ]

    for word in suspicious:

        if word in url:

            score -= 25

            negatives.append(
                f"Suspicious keyword: {word}"
            )


    return {

        "score": score,
        "positives": positives,
        "negatives": negatives

    }