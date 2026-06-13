import re


def analyze_recruiter(text,company_domain=None):

    score = 0

    positives = []

    negatives = []

    emails = re.findall(

        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",

        text

    )

    if not emails:

        return {

            "score": -15,

            "positives": [],

            "negatives": [

                "No recruiter email found"

            ]

        }

    free_domains = [

        "gmail.com",
        "yahoo.com",
        "outlook.com",
        "hotmail.com"

    ]

    for email in emails:

        domain = email.split("@")[1].lower()

        if company_domain:

            if domain != company_domain.lower():

                score -= 40

                negatives.append(
                    f"Recruiter domain does not match company: {email}"
                )

            else:

                score += 15

                positives.append(
                    f"Recruiter domain matches company: {email}"
                )

        if domain in free_domains:

            score -= 30

            negatives.append(

                f"Recruiter using free email provider: {email}"

            )

        else:

            score += 10

            positives.append(

                f"Professional recruiter email: {email}"

            )

    return {

        "score": score,

        "positives": positives,

        "negatives": negatives

    }