from ai.keyword_detector import detect_keywords


def calculate_score(text,url):

    score=100

    positives=[]

    negatives=[]


    scam_terms=detect_keywords(text)


    if scam_terms:

        penalty=len(scam_terms)*10

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



    score=max(
    0,
    min(score,100)
    )



    return{

    "score":score,

    "positives":positives,

    "negatives":negatives

    }