from ai.keyword_detector import detect_keywords
from utils.website_checker import analyze_website
from ai.scam_database import check_scam_database


def calculate_score(text,url):

    score=100

    positives=[]

    negatives=[]

    website_result = analyze_website(url)


    scam_terms=detect_keywords(text)

    db_result = check_scam_database(text)


    if scam_terms:

        penalty=len(scam_terms)*5

        score-=penalty

        negatives.append(
            f"Detected risky terms: {', '.join(scam_terms)}"
        )



    if "@" in text:

        positives.append(
            "Professional contact structure detected"
        )



    if len(text)>500:

        positives.append(
            "Detailed internship description found"
        )


    urgency_words=[

    "urgent",
    "immediately",
    "today only"

    ]


    for word in urgency_words:

        if word in text.lower():

            score-=8

            negatives.append(
            f"Urgency wording: {word}"
            )


    score -= website_result["score_penalty"]

    for item in website_result["penalties"]:

        negatives.append(item)

    for match in db_result["matches"]:

        negatives.append(
            f"Known scam pattern detected: {match}"
        )

    for item in website_result["positives"]:

        positives.append(item)

    score -= db_result["score_penalty"]

    score=max(
    0,
    min(score,100)
    )



    return{

    "score":score,

    "positives":positives,

    "negatives":negatives

    }