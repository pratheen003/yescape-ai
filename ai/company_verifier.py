import re


FREE_EMAIL_PROVIDERS = [

    "gmail.com",
    "yahoo.com",
    "outlook.com",
    "hotmail.com",
    "proton.me",
    "protonmail.com"

]


def verify_company_identity(

    text,
    company_name,
    company_domain

):

    score = 0

    positives = []

    negatives = []

    emails = re.findall(

        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",

        text

    )

    if not company_name:

        return {

            "score": score,

            "positives": positives,

            "negatives": negatives

        }

    for email in emails:

        domain = email.split("@")[1].lower()

        # Exact company match

        if company_domain and domain == company_domain:

            score += 15

            positives.append(

                f"Verified company email domain: {email}"

            )

        # Free email pretending to be company

        elif company_name.lower() in email.lower():

            if domain in FREE_EMAIL_PROVIDERS:

                score -= 25

                negatives.append(

                    f"Possible {company_name} impersonation: {email}"

                )

        # Wrong corporate domain

        elif company_domain and company_name.lower() in email.lower():

            score -= 20

            negatives.append(

                f"Company name used with non-official domain: {email}"

            )

    return {

        "score": score,

        "positives": positives,

        "negatives": negatives

    }