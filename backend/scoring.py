def calculate_yescore(text):

    score = 100
    reasons = []

    text = text.lower()

    scam_keywords = {
    "registration fee": 30,
    "payment required": 25,
    "pay fee": 25,
    "limited seats": 10,
    "guaranteed job": 20,
    "guaranteed internship": 20,
    "instant joining": 15,
    "certificate charge": 20,
    "whatsapp only": 15,
    "no interview": 20,
    "certificate fee": 20,
    "pay now": 15,
}

    for keyword, penalty in scam_keywords.items():
        if keyword in text:
            score -= penalty
            reasons.append(f"Detected suspicious keyword: '{keyword}'")

    if score >= 80:
        status = "SAFE"
        color = "green"

    elif score >= 50:
        status = "MODERATE RISK"
        color = "orange"

    else:
        status = "HIGH RISK"
        color = "red"

    score = max(score, 0)

    return {
        "score": score,
        "status": status,
        "color": color,
        "reasons": reasons
    }