def calculate_trust(

    company_trust=None,
    recruiter_trust=None,
    website_trust=None,
    language_trust=None,
    context_trust=None

):

    trusts = {

        "company_trust": company_trust,
        "recruiter_trust": recruiter_trust,
        "website_trust": website_trust,
        "language_trust": language_trust,
        "context_trust": context_trust

    }

    available = [

        value

        for value in trusts.values()

        if value is not None

    ]

    if len(available) == 0:

        overall_trust = 0

    else:

        overall_trust = round(

            sum(available) / len(available)

        )

    trusts["overall_trust"] = overall_trust

    return trusts