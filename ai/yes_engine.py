import re
from ai.domain_checker import analyze_domain
from ai.company_checker import analyze_company
from ai.urgency_detector import analyze_urgency
from ai.scam_database import check_scam_database
from ai.context_analyzer import analyze_context
from ai.recruiter_checker import analyze_recruiter
from ai.trust_engine import calculate_trust
from utils.website_checker import analyze_website
from ai.confidence_engine import calculate_confidence
from ai.reasoning_engine import generate_reasoning
from ai.company_verifier import verify_company_identity

def analyze_offer(text,url=""):

    text=text.lower()

    context = analyze_context(text)
    
    language_trust = 100

    context_trust = 50

    context_trust += len(
        context["safe_contexts"]
    ) * 15

    context_trust -= len(
        context["negative_contexts"]
    ) * 15

    context_trust = max(
        0,
        min(context_trust, 100)
    )

    db_result = check_scam_database(text)

    score=100

    positives=[]

    negatives=[]

    company = {
        "company": None,
        "score": 0,
        "positives": [],
        "negatives": []
    }

    domain = analyze_domain(url)

    score += domain["score"]

    positives.extend(
        domain["positives"]
    )

    negatives.extend(
        domain["negatives"]
    )

    company = analyze_company(text,url)

    score += company["score"]

    positives.extend(
        company["positives"]
    )

    negatives.extend(
        company["negatives"]
    )

    if company["company"]:

        company_trust = 90

    else:

        company_trust = None

    company_check = verify_company_identity(

        text,

        company["company"],

        company["company_domain"]

    )

    score += company_check["score"]

    positives.extend(
        company_check["positives"]
    )

    negatives.extend(
        company_check["negatives"]
    )

    if any(

        "impersonation" in item.lower()

        for item in company_check["negatives"]

    ):

        company_trust = 10

    elif any(

        "verified company email domain" in item.lower()

        for item in company_check["positives"]

    ):

        company_trust = 100

    website_result = analyze_website(url)

    if url:

        website_trust = 50

        if website_result["https"]:

            website_trust += 20

        if website_result["domain_age_days"]:

            if website_result["domain_age_days"] > 365:

                website_trust += 20

            elif website_result["domain_age_days"] > 180:

                website_trust += 10

        website_trust = min(100, website_trust)

    else:

        website_trust = None

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

    "payment required":25,

    "whatsapp only":20,

    "dm for details":15,

    "earn money fast":20,

    "guaranteed placement":20,

    "work from home and earn":15

    }


    for word, penalty in risky_words.items():

        skip_penalty = False

        for safe in context["safe_contexts"]:

            if word in safe:

                skip_penalty = True
                break

        if skip_penalty:
            continue

        if word in text:

            score -= penalty

            negatives.append(
                f"Risk phrase found: {word}"
            )

    valid_matches = []

    for match in db_result["matches"]:

        skip_match = False

        for safe in context["safe_contexts"]:

            if "registration fee" in safe and match == "registration_fee":

                skip_match = True
                break

        if skip_match:
            continue

        valid_matches.append(match)

        negatives.append(
            f"Known scam pattern detected: {match}"
        )

    score -= len(valid_matches) * 8

    language_trust -= len(valid_matches) * 10

    # -------------------
    # positive indicators
    # -------------------

    if len(text)>500:

        positives.append(
        "Detailed internship information found"
        )

        score+=5

    if "internship" in text:

        positives.append(
        "Internship role clearly mentioned"
        )

        score+=5


    if "company" in text:

        positives.append(
        "Company information referenced"
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

        urgency=analyze_urgency(text)

        score+=urgency["score"]

        if urgency["negatives"]:

            language_trust -= 20

        positives.extend(
        urgency["positives"]
        )

        negatives.extend(
        urgency["negatives"]
        )



    # -------------------

    score += context["score"]

    positives.extend(
        context["positives"]
    )

    negatives.extend(
        context["negatives"]
    )

    recruiter = analyze_recruiter(
        text,
        company["company_domain"]
    )

    score += recruiter["score"]

    positives.extend(
        recruiter["positives"]
    )

    negatives.extend(
        recruiter["negatives"]
    )

    if "No recruiter email found" in recruiter["negatives"]:

        recruiter_trust = None

    elif recruiter["score"] > 0:

        recruiter_trust = 90

    elif recruiter["score"] < 0:

        recruiter_trust = 40

    else:

        recruiter_trust = None

    language_trust = max(
        0,
        min(language_trust,100)
    )

    context_trust = max(
        0,
        min(context_trust,100)
    )

    trust_data = calculate_trust(

        company_trust=company_trust,

        recruiter_trust=recruiter_trust,

        website_trust=website_trust,

        language_trust=language_trust,

        context_trust=context_trust

    )

    confidence_data = calculate_confidence(

        score,
        trust_data,
        positives,
        negatives

    )

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

    reasoning = generate_reasoning(

        status,

        positives,

        negatives

    )

    return {

        "score": trust_data["overall_trust"],

        "status":status,

        "trust":trust,

        "verdict":verdict,

        "positives":positives,

        "negatives":negatives,

        "trust_data":trust_data,

        "confidence_data":confidence_data,

        "reasoning": reasoning,

        "domain_age": website_result["domain_age_days"],

        "https_status": website_result["https"]

    }