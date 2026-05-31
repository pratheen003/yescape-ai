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


def detect_company(text, url):

    data = (text + " " + url).lower()

    for company in KNOWN_COMPANIES:

        if company in data:

            return company.title()

    return "Unknown"


def detect_domain_reputation(url):

    if url == "":

        return "No Website"

    url = url.lower()

    if "https://" in url:

        return "Trusted"

    return "Needs Verification"


def generate_research_summary(text, url):

    company = detect_company(
        text,
        url
    )

    reputation = detect_domain_reputation(
        url
    )

    if company != "Unknown":

        company_status = "Recognized Company"

    else:

        company_status = "Company Not Verified"

    return {

        "company": company,

        "domain_reputation": reputation,

        "company_status": company_status

    }