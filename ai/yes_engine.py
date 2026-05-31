import re
from ai.domain_checker import analyze_domain
from ai.company_checker import analyze_company
from ai.urgency_detector import analyze_urgency
from ai.research_engine import analyze_domain

def analyze_offer(text,url=""):

    text=text.lower()

    score=100

    positives=[]

    negatives=[]

    domain = analyze_domain(url)

    score += domain["score"]

    positives.extend(
        domain["positives"]
    )

    negatives.extend(
        domain["negatives"]
    )


    # -------------------
    # risky phrases
    # -------------------

    risky_words={

    "registration fee":30,

    "training fee":25,

    "security deposit":25,

    "pay now":20,

    "limited slots":10,

    "urgent joining":15,

    "immediate joining":15,

    "guaranteed internship":20,

    "certificate fee":30,

    "payment required":25

    }


    for word,penalty in risky_words.items():

        if word in text:

            score-=penalty

            negatives.append(
            f"Risk phrase found: {word}"
            )


    # -------------------
    # positive indicators
    # -------------------

    if "@" in text:

        positives.append(
        "Professional email detected"
        )

        score+=5


    if len(text)>500:

        positives.append(
        "Detailed internship information found"
        )

        score+=5


    phone_pattern=r"\+91|[0-9]{10}"

    if re.search(
    phone_pattern,
    text
    ):

        positives.append(
        "Contact information available"
        )

        score+=5



    if url:

        positives.append(
        "Company website supplied"
        )

        score+=10


        domain=analyze_domain(url)

        score+=domain["score"]

        positives.extend(
        domain["positives"]
        )

        negatives.extend(
        domain["negatives"]
        )

        company=analyze_company(text)

        score+=company["score"]

        positives.extend(
        company["positives"]
        )

        negatives.extend(
        company["negatives"]
        )

        urgency=analyze_urgency(text)

        score+=urgency["score"]

        positives.extend(
        urgency["positives"]
        )

        negatives.extend(
        urgency["negatives"]
        )



    # -------------------

    score=max(
    0,
    min(score,100)
    )


    # -------------------

    if score>=80:

        status="SAFE"

        trust="HIGH TRUST"

        verdict=(
        "AI found strong legitimacy indicators."
        )


    elif score>=60:

        status="CAUTION"

        trust="MEDIUM TRUST"

        verdict=(
        "Mixed signals detected."
        )


    elif score>=40:

        status="RISKY"

        trust="LOW TRUST"

        verdict=(
        "Several suspicious indicators found."
        )


    else:

        status="SCAM ALERT"

        trust="VERY LOW TRUST"

        verdict=(
        "High probability of internship scam."
        )


    return{

    "score":score,

    "status":status,

    "trust":trust,

    "verdict":verdict,

    "positives":positives,

    "negatives":negatives

    }