KNOWN_COMPANIES = {

    "google": "google.com",

    "microsoft": "microsoft.com",

    "amazon": "amazon.com",

    "infosys": "infosys.com",

    "tcs": "tcs.com",

    "wipro": "wipro.com",

    "accenture": "accenture.com",

    "zoho": "zoho.com",

    "ibm": "ibm.com",

    "cognizant": "cognizant.com",

    "hcl": "hcltech.com"

}


def analyze_company(text, url):

    data = (text + " " + url).lower()

    score=0

    positives=[]

    negatives=[]

    detected_company = None
    company_domain = None

    found=False


    for company in KNOWN_COMPANIES:

        if company in data:

            found=True

            company_domain = KNOWN_COMPANIES[company]

            detected_company = company

            score+=15

            positives.append(
            f"Recognized company mention: {company.title()}"
            )


    if not found:

        negatives.append(
        "Company identity not clearly detected"
        )


    return {

    "company": detected_company.title() if found else None,

    "company_domain": company_domain,

    "score": score,

    "positives": positives,

    "negatives": negatives

}