KNOWN_COMPANIES=[

"google",
"microsoft",
"amazon",
"tcs",
"infosys",
"wipro",
"zoho",
"accenture",
"ibm",
"openai"

]


def analyze_company(text):

    text=text.lower()

    score=0

    positives=[]

    negatives=[]


    found=False


    for company in KNOWN_COMPANIES:

        if company in text:

            found=True

            score+=15

            positives.append(
            f"Recognized company mention: {company.title()}"
            )


    if not found:

        negatives.append(
        "Company identity not clearly detected"
        )


    return{

    "score":score,

    "positives":positives,

    "negatives":negatives

    }